#!/usr/bin/env python3
"""
render.py — Renderiza una plantilla HTML de Horizonte Sostenible a PDF + PNG (QA).

Uso:
    python scripts/render.py templates/carrusel-madre.html --width 1080 --height 1350
    python scripts/render.py templates/onepager-propuesta.html --width 816 --height 1056

Requisitos:
    pip install playwright pdf2image
    playwright install chromium
    (Linux, para los PNG de QA) sudo apt-get install poppler-utils

Salida: out/<nombre>.pdf  y  out/<nombre>.png
"""
import argparse
import asyncio
import os
import sys
from pathlib import Path


async def render(html_path: Path, width: int, height: int, out_dir: Path):
    from playwright.async_api import async_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = html_path.stem
    pdf_out = out_dir / f"{stem}.pdf"
    png_out = out_dir / f"{stem}.png"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        await page.goto(html_path.resolve().as_uri())
        # Espera de carga de fuentes (Google Fonts)
        await page.wait_for_timeout(2500)
        await page.pdf(
            path=str(pdf_out),
            width=f"{width}px",
            height=f"{height}px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()

    print(f"PDF  → {pdf_out}")

    # Vista PNG de QA (primera página) si poppler está disponible
    try:
        from pdf2image import convert_from_path
        imgs = convert_from_path(str(pdf_out), dpi=90)
        imgs[0].save(png_out, "PNG")
        print(f"PNG  → {png_out}  (QA, {len(imgs)} pág.)")
    except Exception as e:
        print(f"(PNG de QA omitido: {e})", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description="Renderiza una plantilla HS a PDF + PNG.")
    ap.add_argument("html", type=Path, help="Ruta a la plantilla HTML")
    ap.add_argument("--width", type=int, default=1080, help="Ancho del viewport en px")
    ap.add_argument("--height", type=int, default=1350, help="Alto del viewport en px")
    ap.add_argument("--out", type=Path, default=Path("out"), help="Carpeta de salida")
    args = ap.parse_args()

    if not args.html.exists():
        sys.exit(f"No existe: {args.html}")

    asyncio.run(render(args.html, args.width, args.height, args.out))


if __name__ == "__main__":
    main()
