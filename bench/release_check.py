#!/usr/bin/env python3
"""公開前の版ズレ検査。

**Zenodo は `.zenodo.json` を権威として読む。**CITATION.cff だけ上げて
`.zenodo.json` を放置すると、Zenodo は古いメタデータで新しい中身を登録する。
ai-reach-paper で実際に起きた: v1.3.0 の zip が **1.2.0 として** DOI を取った。

このリポでは `.zenodo.json` に `version` 欄を置いていない（Zenodo がタグから
版を採る）ので、ズレるのは**要旨の側**である。だからここでは要旨を見る。

**関門にする条件は誤検出の率で決めてある。**
「現行版が要旨に出てこない」だけを条件にすると、版段落を持たない初版
（v1.0.0）で必ず鳴る。**毎回鳴る警報は無視する癖を作る**ので、そうしない。

  落とす: 要旨が版に言及しているのに、**現行版だけが無い**（追随漏れ）
  落とす: 初版でないのに、要旨が版に一度も言及していない（版段落の書き漏れ）
  通す  : 初版で、版への言及が無い（正常）

**上の3条件は末尾しか見ていない。**bim-bench で中抜けが見つかった: タグは
v1.0.0 v1.1.0 v1.2.0 v1.2.1 の4本あるのに、要旨の版段落は 1.2.0 と 1.2.1 の
2つだけだった。**v1.1.0 は v1.0.0 の主要結論を撤回した版**で、シリーズ最大の
撤回が正本に載っていなかった。現行版 1.2.1 は要旨にあるので上の検査は通る。

  落とす: タグがあるのに、その版の**版段落が無い**（中抜け）

**「言及」と「版段落」は別物である。**上の3条件は本文中のどこかに版番号が
あれば良しとしており、bim は "repairing the v1.1.0 defect" という他版の段落の
中の参照で通っていた。中抜け検査のほうは**段落の先頭が `Version X.Y.Z`**
であることを要求する。この規約は9リポで較正済み（誤検出ゼロ・取りこぼしゼロ）。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VER = re.compile(r"\b\d+\.\d+\.\d+\b")
BLOCK = re.compile(r"<p>.*?</p>", re.S)
HEAD = re.compile(r"^\s*Version\s+(\d+\.\d+\.\d+)")


def key(v: str):
    return [int(x) for x in v.split(".")]


def version_paragraphs(desc: str) -> set:
    """段落の先頭が `Version X.Y.Z` のものだけを拾う。本文中の言及は数えない。"""
    out = set()
    for m in BLOCK.finditer(desc):
        text = re.sub("<[^>]+>", "", m.group(0))
        h = HEAD.match(text)
        if h:
            out.add(h.group(1))
    return out


def released_versions() -> set | None:
    """git のタグから公開済みの版を採る。取れなければ None（検査を飛ばす）。"""
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "tag"],
                           capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    tags = {t.lstrip("v") for t in r.stdout.split() if VER.fullmatch(t.lstrip("v"))}
    return tags or None


def main() -> int:
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    m = re.search(r'^version:\s*"?([^"\s]+)"?', cff, re.M)
    if not m:
        print("[NG] CITATION.cff に version が無い")
        return 1
    cur = m.group(1)

    zj = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))

    # .zenodo.json が版を明示しているなら、そちらが優先されるので厳密に一致させる
    pinned = zj.get("version")
    if pinned is not None and pinned != cur:
        print(f"[NG] 版がズレている。CITATION.cff={cur} / .zenodo.json={pinned}")
        print(f"     **このまま release を切ると Zenodo は {pinned} として登録する。**")
        return 1

    desc = re.sub("<[^>]+>", " ", zj.get("description", ""))
    seen = sorted(set(VER.findall(desc)))

    if not seen:
        if cur == "1.0.0":
            print(f"[OK] 公開メタデータ  v{cur}（初版。版段落なしで正常）")
            return 0
        print(f"[NG] v{cur} なのに .zenodo.json の要旨が版に一度も触れていない")
        print("     **初版でない公開は、何が変わったかを要旨に書く。**")
        return 1

    if cur not in seen:
        print(f"[NG] .zenodo.json の要旨が v{cur} に追随していない（記載: {', '.join(seen)}）")
        print("     **Zenodo はこの要旨で登録する。中身より古い説明が DOI に付く。**")
        return 1

    # ── 中抜け検査 ───────────────────────────────────────────
    # タグごとに版段落があるか。初版は版段落を持たないのが正常なので除く。
    tags = released_versions()
    if tags is None:
        print(f"[OK] 公開メタデータ  v{cur} が要旨に記載あり")
        print("     （git のタグが読めないので中抜け検査は飛ばした）")
        return 0

    paras = version_paragraphs(zj.get("description", ""))
    expected = {v for v in tags if v != min(tags, key=key)}
    expected.add(cur) if cur not in tags and cur != min(tags | {cur}, key=key) else None
    missing = sorted(expected - paras, key=key)

    if missing:
        print(f"[NG] 版段落が無い版がある: {', '.join('v' + v for v in missing)}")
        print(f"     タグ: {', '.join('v' + v for v in sorted(tags, key=key))}")
        print(f"     版段落: {', '.join('v' + v for v in sorted(paras, key=key)) or '無し'}")
        print("     **撤回した版が抜けると、DOI を辿った読者に撤回が届かない。**")
        print("     要旨に `<p><strong>Version X.Y.Z ...` の段落を足す。")
        return 1

    print(f"[OK] 公開メタデータ  v{cur} が要旨に記載あり")
    if expected:
        print(f"     版段落も揃っている（{', '.join('v' + v for v in sorted(expected, key=key))}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
