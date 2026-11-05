"""Editorial Grid 렌더러 — HTML → PDF + 검수용 PNG.

사용: python3 render.py <file.html> [out_dir]
  - .slide 가 있으면 DECK: 1280×720 다페이지 PDF + 슬라이드별 PNG + 전체 한눈에 보기(contact sheet)
  - 없으면 DOC: 900px 폭 한 장짜리 롱 PDF + 전체 스크린샷
필요: pip install playwright pillow && python3 -m playwright install chromium
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else src.parent).resolve()
shots = out / f"_check_{src.stem}"
shots.mkdir(parents=True, exist_ok=True)
pdf = out / f"{src.stem}.pdf"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=2)
    pg.goto(src.as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    n = pg.evaluate("document.querySelectorAll('.slide').length")
    if n:
        for i in range(n):
            pg.locator(".slide").nth(i).screenshot(path=str(shots / f"s{i+1:02d}.png"))
        pg.pdf(path=str(pdf), width="1280px", height="720px", print_background=True, prefer_css_page_size=True)
        try:
            from PIL import Image
            ims = [Image.open(x).resize((640, 360)) for x in sorted(shots.glob("s??.png"))]
            sheet = Image.new("RGB", (640 * 3, 360 * ((len(ims) + 2) // 3)), "white")
            for i, im in enumerate(ims):
                sheet.paste(im, ((i % 3) * 640, (i // 3) * 360))
            sheet.save(shots / "sheet.png")
        except ImportError:
            pass
        print(f"DECK {n} slides → {pdf}\ncheck: {shots}")
    else:
        pg.set_viewport_size({"width": 900, "height": 1000})
        h = pg.evaluate("document.documentElement.scrollHeight")
        pg.pdf(path=str(pdf), width="900px", height=f"{h + 2}px", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        pg.screenshot(path=str(shots / "full.png"), full_page=True)
        print(f"DOC {h}px → {pdf}\ncheck: {shots}/full.png")
    b.close()
