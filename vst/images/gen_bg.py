"""Procedural grunge plate for the Boris Granular skin (1280x628): dark, purple-tinted, scratched, vignetted.
Run: docker run --rm -v "$PWD":/w -w /w python:3.11-slim bash -c "pip install -q pillow numpy; python3 images/gen_bg.py" """
import numpy as np
from PIL import Image, ImageFilter
W, H = 1280, 628
rng = np.random.default_rng(7)
def octave(scale, amp):
    n = rng.random((H // scale + 2, W // scale + 2)).astype("f4")
    im = Image.fromarray((n * 255).astype("u1")).resize((W, H), Image.BICUBIC)
    return np.asarray(im, "f4") / 255 * amp
t = octave(2, .35) + octave(8, .5) + octave(32, .7) + octave(120, .9)
t = (t - t.min()) / (t.max() - t.min())
# fine scratches: faint long strokes
sc = np.zeros((H, W), "f4")
for _ in range(260):
    x, y = rng.integers(0, W), rng.integers(0, H); l = rng.integers(40, 260); a = rng.normal(0, .25)
    for i in range(l):
        xx, yy = int(x + i), int(y + i * a)
        if 0 <= xx < W and 0 <= yy < H: sc[yy, xx] = max(sc[yy, xx], rng.random() * .5)
sc = np.asarray(Image.fromarray((sc * 255).astype("u1")).filter(ImageFilter.GaussianBlur(.6)), "f4") / 255
g = 0.07 + 0.20 * t + 0.12 * sc
yy, xx = np.mgrid[0:H, 0:W]
vig = 1 - 0.55 * (((xx - W / 2) / (W / 1.6)) ** 2 + ((yy - H / 2) / (H / 1.4)) ** 2)
g = g * np.clip(vig, .25, 1)
rgb = np.stack([g * 1.05, g * .92, g * 1.35], -1)          # cold purple cast
Image.fromarray((np.clip(rgb, 0, 1) * 255).astype("u1")).save("images/bg.png")
