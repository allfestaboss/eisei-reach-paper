# No error was raised

[![DOI](https://zenodo.org/badge/DOI/PENDING.svg)](https://doi.org/PENDING)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

> **No error was raised: twenty-six broken measurements from a cross-domain
> audit of free satellite data**
> Boss Ohkubo (Allfesta Corp.) — ORCID 0009-0007-8300-0039

衛星データの応用について公開されているものは、ごく一部を除いて**成功の集まり**である。
無料の地球観測で何ができないのか、そして「できるかどうかを測る試み」がどこで壊れるのかは、
ほとんど記録に残っていない。その空白を埋めるために組んだ横断測定の報告。
**主たる所見は衛星についてではなく、測定についてのものである。**

```
15業種を福岡に固定して全部実装 → 9業種を公費調達の参照解で採点
技術の壁 7種（金で解けるのは1種だけ） ＋ 制度の壁 4種
測り方が壊れていた 26件 ── 全部エラーを出さず、うち 10件は「良い結果」を返した
```

## 読む

| | |
|---|---|
| 英語本文 | `build/paper.md` / `build/paper.html`（約8,000語） |
| 日本語完全版 | `build/paper-ja.md` / `build/paper-ja.html` |
| 実装・測定記録・26件の台帳 | 別リポジトリ [`eisei-bench`](https://github.com/allfestaboss/eisei-bench) |
| 公開サイト | https://satellite.dx-fukuoka.com/ |

```bash
python3 build.py                # 節から2言語ぶんの原稿を組む
python3 build.py --verify       # build/ が節ファイルより古くないか（release の前に）
python3 bench/release_check.py  # 公開前の版ズレ検査
```

## 構成

```
00-abstract-and-title.md   表題と投稿版 Abstract（作業メモを含む。原稿には入らない）
sections/01..09            英語本文
ja/00..09                  日本語完全版
build.py                   両方を build/ に組み上げる
```

**節ファイルが正本で、`build/` は生成物。**原稿を直すときは `sections/` か `ja/` を直す。
生成物も commit してあるのは、DOI から来た読者に節ファイルを順に開かせないためで、
ズレは `python3 build.py --verify` が落とす。

## 主張

1. **分母が間違っていた。** 15業種のうち国が発注しているのは9業種だけで、
   4業種は13年度・312,584件で解析系ゼロ、2業種はキーワードの誤マッチだった。
2. **技術の壁7種のうち、金で解けるのは1種だけ。** 2種は測定器の性質で、1種は
   そもそも技術の壁ではない（正しく測れているのに人口統計に上積みしない）。
3. **測り方が壊れていた26件。** 全部エラーを出さずにそれらしい値を返し、
   **10件は「良い結果」を返した。** 悪い結果は疑われ良い結果は疑われないという非対称が、
   自分を測る研究の最大の脅威である。

## 引用

```bibtex
@article{ohkubo_no_error_was_raised,
  author = {Ohkubo, Boss},
  title  = {No error was raised: twenty-six broken measurements from a
            cross-domain audit of free satellite data},
  year   = {2026},
  doi    = {PENDING},
  note   = {Preprint}
}
```

引用には **Concept DOI**（常に最新版に解決する）を使う。正確な版は `CITATION.cff`。

## ライセンス

文章と組み上げスクリプトは **CC BY 4.0**（[LICENSE](LICENSE)）。
測定データは別リポジトリにあり MIT ＋ 第三者条件。[NOTICE](NOTICE) を参照。

**プレプリント。査読を受けていない。**
