"""Round glowing Freeze button, off/on (96x96). docker python:3.11-slim + pillow."""
import math
from PIL import Image, ImageDraw, ImageFilter
S = 96
def make(on):
    im = Image.new("RGBA", (S * 4, S * 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = S * 2
    if on:
        g = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((c - 150, c - 150, c + 150, c + 150), fill=(180, 128, 255, 200))
        im = Image.alpha_composite(im, g.filter(ImageFilter.GaussianBlur(24))); d = ImageDraw.Draw(im)
    d.ellipse((c - 150, c - 150, c + 150, c + 150), fill=(14, 8, 28, 255), outline=(106, 85, 200, 255), width=10)
    top, bot = ((196, 160, 255), (110, 60, 210)) if on else ((70, 56, 120), (28, 20, 56))
    for i in range(120, 0, -1):
        t = i / 120; col = tuple(int(bot[k] * t + top[k] * (1 - t)) for k in range(3)) + (255,)
        d.ellipse((c - i - 20 + (1 - t) * 18, c - i - 20 + (1 - t) * 18, c + i + 20 - (1 - t) * 6, c + i + 20 - (1 - t) * 6), fill=col)
    ink = (255, 255, 255, 255) if on else (190, 170, 240, 255)
    for k in range(6):                                   # snowflake
        a = math.radians(60 * k + 90); x, y = c + 92 * math.cos(a), c - 92 * math.sin(a)
        d.line((c, c, x, y), fill=ink, width=9)
        for s in (-1, 1):
            b = a + s * math.radians(40); mx, my = c + 56 * math.cos(a), c - 56 * math.sin(a)
            d.line((mx, my, mx + 30 * math.cos(b), my - 30 * math.sin(b)), fill=ink, width=7)
    return im.resize((S, S), Image.LANCZOS)
make(False).save("images/freeze_off.png"); make(True).save("images/freeze_on.png")
