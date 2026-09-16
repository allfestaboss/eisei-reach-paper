#!/usr/bin/env python3
"""節を1本の原稿に組み上げる。英語版と日本語完全版の両方。

00-abstract-and-title.md には作業メモ（表題の代案、重心の記録）が混ざっている。
原稿に入れるのは表題と投稿版 Abstract だけなので、ここで抜き出す。
手で消すと、次に Abstract を直したとき同期が切れる。

**版の検査を先に走らせる。** Zenodo はメタデータの権威として `.zenodo.json` を読むので、
CITATION.cff だけ上げて `.zenodo.json` を放置すると、古い説明で新しい中身が登録される。
先行リポで実際に起きた（v1.3.0 の zip が 1.2.1 として DOI を取った）。

**組み上げた原稿は commit する。** DOI を辿って来た読者が最初に開くのは
Zenodo のレコードであって、節ファイルを順に開かせるのは不親切だからである。
正本はあくまで節ファイルなので、ズレを防ぐために `--verify` を用意した
（生成し直して現物と比較し、違えば落ちる）。release の前に走らせる。

出力:
  build/paper.md      英語本文（作業メモを含まない）
  build/paper.html    素の HTML（pandoc が無い環境でも読める）
  build/paper-ja.md   日本語完全版
  build/paper-ja.html 同上
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "build"

SECTIONS = [
    "01-introduction.md",
    "02-design.md",
    "03-walls.md",
    "04-ledger.md",
    "05-threats.md",
    "06-related-work.md",
    "07-discussion.md",
    "08-availability.md",
    "09-references.md",
]

# (出力名, 節のあるディレクトリ, 表題の見出し, Abstract の見出し, 著者行)
EDITIONS = [
    ("paper", ".", r"\*\*Title\*\*", r"## Abstract — 投稿版[^\n]*",
     "Boss Ohkubo (Allfesta Corp.)  \nORCID 0009-0007-8300-0039", "Abstract"),
    ("paper-ja", "ja", r"\*\*表題\*\*", r"## 要旨[^\n]*",
     "大久保（Allfesta Corp.）  \nORCID 0009-0007-8300-0039", "要旨"),
]


def front_matter(src_dir: str, title_head: str, abst_head: str,
                 byline: str, abst_label: str) -> str:
    src = (ROOT / src_dir / "00-abstract-and-title.md").read_text(encoding="utf-8")

    m = re.search(title_head + r"\s*\n\n> (.+?)\n\n", src, re.S)
    if not m:
        raise SystemExit(f"{src_dir}/00 の表題が見つからない。書式が変わっている")
    title = " ".join(x.strip("> ").strip() for x in m.group(1).split("\n"))

    m = re.search(abst_head + r"\n+(.*?)\n+(?=\*[(（]|## |---)", src, re.S)
    if not m:
        raise SystemExit(f"{src_dir}/00 の Abstract が見つからない。書式が変わっている")
    abstract = m.group(1).strip()

    return f"# {title}\n\n{byline}\n\n## {abst_label}\n\n{abstract}\n"


def body(src_dir: str) -> str:
    out = []
    for name in SECTIONS:
        p = ROOT / src_dir / ("sections/" + name if src_dir == "." else name)
        if not p.exists():
            raise SystemExit(f"欠落: {p}")
        out.append(p.read_text(encoding="utf-8").rstrip())
    return "\n\n---\n\n".join(out)


def to_html(md: str, title: str) -> str:
    """依存を足さずに読める形にする。整形が目的で、厳密な変換ではない。

    **原稿は手で折り返してある。**1行ずつ `<p>` にすると段落が
    ばらばらの塊になり、行をまたいだ `**強調**` も変換されない
    （画面で見るまで気づかなかった）。空行か構造行まで貯めてから流す。
    """
    out, in_code, in_table, in_list = [], False, False, False
    para: list[str] = []

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"(?<![\"'>=])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', s)
        return s

    def join(buf: list[str]) -> str:
        """和文は行末で連結し、欧文は空白1つでつなぐ。"""
        s = ""
        for i, x in enumerate(buf):
            if i and not (s[-1:] and ord(s[-1]) > 0x2000 and ord(x[:1] or " ") > 0x2000):
                s += " "
            s += x
        return s

    def flush() -> None:
        if para:
            out.append(f"<p>{inline(join(para))}</p>")
            para.clear()

    def flush_li() -> None:
        nonlocal in_list
        if para:
            out.append(f"<li>{inline(join(para))}</li>")
            para.clear()

    mode = "p"   # 貯めている塊が段落か箇条書き項目か

    def flush_any() -> None:
        flush_li() if mode == "li" else flush()

    for ln in md.split("\n"):
        if ln.startswith("```"):
            flush_any()
            in_code = not in_code
            out.append("<pre>" if in_code else "</pre>")
            continue
        if in_code:
            out.append(html.escape(ln))
            continue
        if ln.startswith("|"):
            flush_any()
            if in_list:
                out.append("</ul>"); in_list = False
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if not in_table:
                out.append("<table>")
                in_table = True
                out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells) + "</tr>")
            else:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>"); in_table = False

        if not ln.strip():                      # 空行が塊の終わり
            flush_any()
            if in_list:
                out.append("</ul>"); in_list = False
            mode = "p"
            continue
        if m := re.match(r"^(#{1,4}) (.+)", ln):
            flush_any()
            if in_list:
                out.append("</ul>"); in_list = False
            mode = "p"
            out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>")
            continue
        if ln.strip() == "---":
            flush_any()
            if in_list:
                out.append("</ul>"); in_list = False
            mode = "p"
            out.append("<hr>")
            continue
        if ln.startswith("> "):
            flush_any(); mode = "p"
            out.append(f"<blockquote>{inline(ln[2:])}</blockquote>")
            continue
        if re.match(r"^[-*] |^\d+\. ", ln):    # 箇条書きの先頭行
            flush_any()
            if not in_list:
                out.append("<ul>"); in_list = True
            mode = "li"
            para.append(re.sub(r"^([-*]|\d+\.) ", "", ln).strip())
            continue
        # 続きの行。**折り返しただけ**なので今の塊に足す
        para.append(ln.strip())

    flush_any()
    if in_table:
        out.append("</table>")
    if in_list:
        out.append("</ul>")

    css = """body{max-width:46em;margin:3em auto;padding:0 1.5em;
  font:16px/1.85 "Hiragino Kaku Gothic ProN","Yu Gothic",system-ui,sans-serif;color:#17222b}
h1{font-size:1.85em;line-height:1.35}h2{margin-top:2.2em;border-bottom:1px solid #c7c0ae;padding-bottom:.3em}
h3{margin-top:1.7em}h4{margin-top:1.2em;font-size:1em}
pre{background:#f4f1e9;padding:1em;overflow-x:auto;font-size:.85em;border:1px solid #ddd6c6}
code{background:#f4f1e9;padding:1px 4px;font-size:.9em}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.88em;display:block;overflow-x:auto}
th,td{border:1px solid #c7c0ae;padding:.5em .7em;text-align:left;vertical-align:top}
th{background:#f4f1e9;white-space:nowrap}
blockquote{border-left:3px solid #1f4a6b;margin:1em 0;padding:.3em 1em;color:#404c58}
hr{border:0;border-top:1px solid #ddd6c6;margin:2.5em 0}li{margin:.3em 0}
a{color:#1f4a6b}"""
    return (f"<!doctype html><meta charset=utf-8><title>{html.escape(title)}</title>"
            f"<style>{css}</style>\n" + "\n".join(out))


def check_versions() -> None:
    """**Zenodo はメタデータの権威として .zenodo.json を読む。**
    version 欄を持たせていないので版はタグから採られる。ここでは
    CITATION.cff 側に version があることと、両者が矛盾しないことだけ見る。"""
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"?([^"\s]+)"?', cff, re.M)
    if not m:
        raise SystemExit("CITATION.cff に version が無い")
    zen = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8")).get("version")
    if zen is not None and zen != m.group(1):
        raise SystemExit(
            f"版がズレている。CITATION.cff={m.group(1)} / .zenodo.json={zen}\n"
            f"  **このまま release を切ると Zenodo は {zen} として登録する。**")
    print(f"  版           CITATION.cff = {m.group(1)}"
          + ("（.zenodo.json は版を持たずタグから採る）" if zen is None else ""))


def render() -> dict[str, str]:
    """節から2言語ぶんを組む。ファイルには書かない。"""
    made = {}
    for name, src_dir, th, ah, byline, label in EDITIONS:
        fm = front_matter(src_dir, th, ah, byline, label)
        md = fm + "\n---\n\n" + body(src_dir) + "\n"
        title = re.match(r"# (.+)", fm).group(1)
        made[f"{name}.md"] = md
        made[f"{name}.html"] = to_html(md, title)
        made[f"__title__{name}"] = title
    return made


def main(verify: bool = False) -> int:
    check_versions()
    made = render()
    if verify:
        # **正本は節ファイル。**commit された build/ が古いまま release を切ると、
        # DOI の付いた原稿だけが現行の主張と食い違う。
        stale = [k for k, v in made.items() if not k.startswith("__title__")
                 and (not (OUT / k).exists()
                      or (OUT / k).read_text(encoding="utf-8") != v)]
        if stale:
            print("[NG] build/ が節ファイルより古い: " + ", ".join(stale))
            print("     python3 build.py を走らせて commit すること。")
            return 1
        print("  build/      節ファイルと一致している")
        return 0

    OUT.mkdir(exist_ok=True)
    for k, v in made.items():
        if k.startswith("__title__"):
            continue
        (OUT / k).write_text(v, encoding="utf-8")
    for name, *_ in EDITIONS:
        md = made[f"{name}.md"]
        words = len(re.findall(r"[A-Za-z0-9'’\-]+", md))
        print(f"  build/{name}.md    {len(md):>7,} 文字 / 英単語 約{words:,}")
        print(f"  build/{name}.html  {(OUT / (name + '.html')).stat().st_size:>7,} バイト")
        print(f"    表題: {made['__title__' + name]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(verify="--verify" in sys.argv))
