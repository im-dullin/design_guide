"""루트 README의 디자인 갤러리를 다시 만든다.

각 디자인 폴더에 design.json 과 preview/thumbnail.png 가 있으면 갤러리에 올라간다.
README.md 의 <!-- GALLERY:START --> ~ <!-- GALLERY:END --> 사이만 교체한다.

사용: python3 scripts/update_gallery.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COLS = 2

items = []
for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith((".", "_")) and p.name != "scripts"):
    meta_f, thumb = d / "design.json", d / "preview" / "thumbnail.png"
    if not (meta_f.exists() and thumb.exists()):
        continue
    m = json.loads(meta_f.read_text())
    items.append({**m, "dir": d.name, "added": m.get("added", "")})
items.sort(key=lambda x: x["added"], reverse=True)  # 최신 추가순

cells = []
for it in items:
    cells.append(
        f'<td width="50%" valign="top"><a href="{it["dir"]}/"><img src="{it["dir"]}/preview/thumbnail.png" width="100%"></a>'
        f'<br><b><a href="{it["dir"]}/">{it["name"]}</a></b>'
        f'<br><sub>{it.get("summary", "")}</sub></td>'
    )
rows = ["<tr>" + "".join(cells[i:i + COLS]) + "</tr>" for i in range(0, len(cells), COLS)]
table = "<table>\n" + "\n".join(rows) + "\n</table>" if cells else "_아직 등록된 디자인이 없습니다._"

index = "\n".join(
    f'| [{it["name"]}]({it["dir"]}/) | `{it["dir"]}` | {" · ".join(it.get("best_for", []))} | {it["added"]} |'
    for it in items
)
block = (
    "<!-- GALLERY:START -->\n"
    f"{table}\n\n"
    "| 디자인 | 폴더 | 잘 맞는 문서 | 추가일 |\n|---|---|---|---|\n"
    f"{index}\n"
    "<!-- GALLERY:END -->"
)

readme = ROOT / "README.md"
s = readme.read_text()
a, b = s.index("<!-- GALLERY:START -->"), s.index("<!-- GALLERY:END -->") + len("<!-- GALLERY:END -->")
readme.write_text(s[:a] + block + s[b:])
print(f"gallery: {len(items)} designs")
