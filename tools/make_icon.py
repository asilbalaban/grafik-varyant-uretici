# -*- coding: utf-8 -*-
"""Uygulama logosunu çizer: assets/logo.png (1024 px) ve assets/app.ico. Gerekli: Pillow."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 2048  # çizim boyutu; kenar yumuşatma için sonradan küçültülür
OUT = Path(__file__).resolve().parent.parent / "assets"

TOP, BOTTOM = (99, 72, 241), (168, 54, 214)   # çivit → mor
INK = (67, 45, 190)
ACCENT = (255, 170, 44)


def rounded(size, box, radius, fill):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius=radius, fill=fill)
    return layer


def background():
    # Döndürünce köşeler boş kalmasın diye iki kat büyük çizip ortasını kırp.
    grad = Image.linear_gradient("L").resize((S, S)).resize((2 * S, 2 * S), box=(0, S // 4, S, 3 * S // 4))
    grad = grad.rotate(-35, resample=Image.BICUBIC).crop((S // 2, S // 2, S // 2 + S, S // 2 + S))
    img = Image.composite(Image.new("RGB", (S, S), BOTTOM), Image.new("RGB", (S, S), TOP), grad).convert("RGBA")
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.225), fill=255)
    img.putalpha(mask)
    return img, mask


def build():
    img, mask = background()
    w, h, r = int(S * 0.47), int(S * 0.60), int(S * 0.075)
    cx, cy = S // 2 + int(S * 0.045), S // 2 + int(S * 0.01)
    box = (cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2)
    pivot = (cx, cy + h // 2)

    # Arkadaki kartlar: aynı şablonun diğer varyantları
    for angle, alpha in ((22, 80), (11, 150)):
        card = rounded((S, S), box, r, (255, 255, 255, alpha)).rotate(angle, resample=Image.BICUBIC, center=pivot)
        img = Image.alpha_composite(img, card)

    shadow = rounded((S, S), (box[0], box[1] + int(S * 0.02), box[2], box[3] + int(S * 0.02)), r, (30, 10, 90, 110))
    img = Image.alpha_composite(img, shadow.filter(ImageFilter.GaussianBlur(S * 0.022)))
    img = Image.alpha_composite(img, rounded((S, S), box, r, (255, 255, 255, 255)))

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(r"C:\Windows\Fonts\seguibl.ttf", int(S * 0.40))
    l, t, rgt, b = d.textbbox((0, 0), "A", font=font)
    ty = cy - int(S * 0.055)
    d.text((cx - (l + rgt) / 2, ty - (t + b) / 2), "A", font=font, fill=INK)
    bw, bh = int(S * 0.27), int(S * 0.042)
    by = cy + int(S * 0.185)
    d.rounded_rectangle((cx - bw // 2, by, cx + bw // 2, by + bh), radius=bh // 2, fill=ACCENT)

    img.putalpha(Image.composite(img.getchannel("A"), Image.new("L", (S, S), 0), mask))
    return img


def main():
    OUT.mkdir(exist_ok=True)
    big = build()
    big.resize((1024, 1024), Image.LANCZOS).save(OUT / "logo.png")
    big.resize((256, 256), Image.LANCZOS).save(
        OUT / "app.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("yazıldı:", OUT / "logo.png", OUT / "app.ico")


if __name__ == "__main__":
    main()
