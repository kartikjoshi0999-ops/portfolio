"""Etsy listing images for every product. 2000x2000, brand-consistent, content-accurate."""
import os, re, textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "dist", "images")
FD = "/usr/share/fonts/truetype/"
SERIF_B = FD + "dejavu/DejaVuSerif-Bold.ttf"
SANS = FD + "liberation/LiberationSans-Regular.ttf"
SANS_B = FD + "liberation/LiberationSans-Bold.ttf"
SANS_I = FD + "liberation/LiberationSans-Italic.ttf"

NAVY, MID, GOLD, TEAL = "#0A1628", "#0D1F3C", "#C9A84C", "#00B4A6"
PAPER, INK, MUTED, LINE, BAND = "#F4F6F9", "#16202E", "#8A97AB", "#C7D0DB", "#EDF1F6"
S = 2000
CAP = "Live formulas — every grey cell updates itself."

f = lambda p, s: ImageFont.truetype(p, s)


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(d, text, font, x, y, max_w, fill, leading):
    for ln in wrap(d, text, font, max_w):
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def fit_row_h(top, n, bottom=1740, lo=64, hi=126):
    return int(max(lo, min(hi, (bottom - top - 274) / max(1, n))))


def grid_card(img, d, x, y, w, headers, rows, col_w, title, accent=TEAL, row_h=64,
              caption="Live formulas — every grey cell updates itself."):
    """A clean, readable spreadsheet-style card using the product's real content."""
    hdr_h, pad, tab_h = 84, 34, 76
    h = tab_h + hdr_h + row_h * len(rows) + pad * 2 + 46
    d.rounded_rectangle([x, y, x + w, y + h], 22, fill="white", outline=LINE, width=3)
    d.rounded_rectangle([x, y, x + w, y + tab_h], 22, fill=MID)
    d.rectangle([x, y + tab_h - 24, x + w, y + tab_h], fill=MID)
    d.text((x + pad, y + 22), title, font=f(SANS_B, 32), fill="white")
    d.ellipse([x + w - 130, y + 28, x + w - 108, y + 50], fill="#E8635A")
    d.ellipse([x + w - 96, y + 28, x + w - 74, y + 50], fill=GOLD)
    d.ellipse([x + w - 62, y + 28, x + w - 40, y + 50], fill=TEAL)
    cx, cy = x + pad, y + tab_h + pad
    d.rectangle([cx, cy, cx + sum(col_w), cy + hdr_h], fill=accent)
    ox = cx
    for hd, cw in zip(headers, col_w):
        for i, ln in enumerate(wrap(d, hd, f(SANS_B, 26), cw - 22)[:2]):
            d.text((ox + 14, cy + 16 + i * 32), ln, font=f(SANS_B, 26), fill="white")
        ox += cw
        d.line([ox, cy, ox, cy + hdr_h + row_h * len(rows)], fill="white", width=2)
    ry = cy + hdr_h
    for r, row in enumerate(rows):
        d.rectangle([cx, ry, cx + sum(col_w), ry + row_h], fill=("white" if r % 2 else BAND))
        ox = cx
        for i, (cell, cw) in enumerate(zip(row, col_w)):
            bold = cell.startswith("*")
            txt = cell.lstrip("*")
            fo = f(SANS_B if bold else SANS, 27)
            align_r = i > 0 and bool(re.fullmatch(r"[-+$(]?[\d,.\s]+%?\)?", txt))
            tw = d.textlength(txt, font=fo)
            px = ox + cw - 16 - tw if align_r else ox + 14
            d.text((px, ry + row_h // 2 - 17), txt, font=fo, fill=INK if bold else "#3B4757")
            ox += cw
        d.line([cx, ry + row_h, cx + sum(col_w), ry + row_h], fill=LINE, width=1)
        ry += row_h
    d.text((cx, ry + 16), caption, font=f(SANS_I, 25), fill=MUTED)
    return y + h


def badge(d, x, y, text, fg, bg, fs=30, pad=(26, 16)):
    fo = f(SANS_B, fs)
    w = d.textlength(text, font=fo) + pad[0] * 2
    d.rounded_rectangle([x, y, x + w, y + fs + pad[1] * 2], (fs + pad[1] * 2) // 2, fill=bg)
    d.text((x + pad[0], y + pad[1] - 2), text, font=fo, fill=fg)
    return x + w + 22


def footer(d, dark=True):
    c = "#7E8CA0" if dark else MUTED
    d.text((110, S - 108), "JOSHI FINANCE TEMPLATES", font=f(SANS_B, 30), fill=GOLD)
    d.text((110, S - 66), "Kartik Joshi, MBA  ·  Financial Analyst & Banking Professional  ·  Cornwall, Ontario",
           font=f(SANS, 26), fill=c)


def img_main(p):
    im = Image.new("RGB", (S, S), NAVY); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, S, 22], fill=GOLD)
    d.rectangle([0, S - 14, S, S], fill=TEAL)
    d.text((110, 120), p["kicker"].upper(), font=f(SANS_B, 34), fill=TEAL)
    y = draw_block(d, p["title"], f(SERIF_B, 96), 110, 190, S - 220, "white", 116)
    y = draw_block(d, p["subtitle"], f(SANS, 40), 110, y + 18, S - 300, "#C8D2E0", 54)
    x = 110
    for t in p["badges"]:
        x = badge(d, x, y + 34, t, NAVY, GOLD)
    top = y + 150
    grid_card(im, d, 110, top, S - 220, p["headers"], p["rows"], p["col_w"], p["card_title"],
              row_h=fit_row_h(top, len(p["rows"])), caption=p.get("caption", CAP))
    footer(d)
    return im


def img_preview(p):
    im = Image.new("RGB", (S, S), PAPER); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, S, 22], fill=TEAL)
    d.text((110, 110), "WHAT YOU GET", font=f(SANS_B, 34), fill=TEAL)
    y = draw_block(d, p["preview_head"], f(SERIF_B, 74), 110, 168, S - 220, MID, 90)
    top = y + 60
    grid_card(im, d, 110, top, S - 220, p["headers2"], p["rows2"], p["col_w2"], p["card_title2"],
              row_h=fit_row_h(top, len(p["rows2"])), caption=p.get("caption", CAP))
    footer(d, dark=False)
    return im


def img_inside(p):
    im = Image.new("RGB", (S, S), MID); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, S, 22], fill=GOLD)
    d.text((110, 120), "INSIDE THE FILE", font=f(SANS_B, 34), fill=TEAL)
    y = draw_block(d, p["inside_head"], f(SERIF_B, 76), 110, 180, S - 220, "white", 92)
    y += 46
    n = len(p["inside"])
    step = int(max(140, min(200, (1740 - y) / n)))
    bh = step - 20
    for tab, desc in p["inside"]:
        d.rounded_rectangle([110, y, S - 110, y + bh], 18, fill="#132845", outline="#22385A", width=2)
        cy = y + bh // 2
        d.ellipse([146, cy - 22, 190, cy + 22], fill=TEAL)
        d.line([157, cy, 166, cy + 10], fill=MID, width=6)
        d.line([166, cy + 10, 180, cy - 11], fill=MID, width=6)
        d.text((222, y + bh // 2 - 46), tab, font=f(SANS_B, 38), fill=GOLD)
        d.text((222, y + bh // 2 + 4), desc, font=f(SANS, 30), fill="#C8D2E0")
        y += step
    footer(d)
    return im


def img_details(p):
    im = Image.new("RGB", (S, S), PAPER); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, S, 22], fill=TEAL)
    d.text((110, 110), "HOW IT WORKS", font=f(SANS_B, 34), fill=TEAL)
    draw_block(d, "Instant digital download. No shipping, no waiting.",
               f(SERIF_B, 72), 110, 168, S - 220, MID, 86)
    y = 330
    for i, (t, s_) in enumerate(p["steps"], 1):
        d.ellipse([110, y, 190, y + 80], fill=MID)
        w = d.textlength(str(i), font=f(SANS_B, 42))
        d.text((150 - w / 2, y + 16), str(i), font=f(SANS_B, 42), fill=GOLD)
        d.text((230, y + 4), t, font=f(SANS_B, 40), fill=INK)
        draw_block(d, s_, f(SANS, 30), 230, y + 56, S - 380, "#41505F", 40)
        y += 170
    y = max(y + 10, 1380)
    d.rounded_rectangle([110, y, S - 110, y + 300], 20, fill="white", outline=LINE, width=3)
    d.text((160, y + 40), "WORKS WITH", font=f(SANS_B, 30), fill=TEAL)
    d.text((160, y + 92), p["compat"], font=f(SANS, 32), fill=INK)
    d.text((160, y + 150), "LICENCE", font=f(SANS_B, 30), fill=TEAL)
    draw_block(d, "Personal, single-user licence. Print and edit for yourself or your own business. "
                  "Not for resale or redistribution.", f(SANS, 28), 160, y + 200, S - 360, "#41505F", 38)
    footer(d, dark=False)
    return im


def build(p):
    folder = os.path.join(OUT, p["slug"])
    os.makedirs(folder, exist_ok=True)
    for name, fn in (("1-main", img_main), ("2-preview", img_preview),
                     ("3-inside", img_inside), ("4-details", img_details)):
        fp = os.path.join(folder, f"{name}.png")
        fn(p).save(fp, optimize=True)
    print("images:", p["slug"])


def shop_banner():
    W, H = 1600, 400
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 8], fill=GOLD)
    d.rectangle([0, H - 6, W, H], fill=TEAL)
    for i in range(0, W, 48):
        d.line([i, 0, i, H], fill="#101F35", width=1)
    for j in range(0, H, 48):
        d.line([0, j, W, j], fill="#101F35", width=1)
    d.text((70, 96), "JOSHI FINANCE TEMPLATES", font=f(SANS_B, 30), fill=GOLD)
    d.text((70, 146), "Spreadsheets that do the thinking", font=f(SERIF_B, 62), fill="white")
    d.text((70, 232), "Built by a Canadian banking professional  ·  Budgeting · TFSA & RRSP · Debt · Investing · Business cash flow",
           font=f(SANS, 26), fill="#C8D2E0")
    x = 70
    for t in ["Instant download", "Excel & PDF", "No subscription", "Made in Canada"]:
        x = badge(d, x, 292, t, NAVY, GOLD, fs=22, pad=(18, 11))
    return im


def shop_icon():
    W = 500
    im = Image.new("RGB", (W, W), NAVY); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=GOLD)
    d.rectangle([0, W - 10, W, W], fill=TEAL)
    d.text((0, 0), "", font=f(SANS, 10))
    fo = f(SERIF_B, 210)
    t = "JF"
    w = d.textlength(t, font=fo)
    d.text(((W - w) / 2, 118), t, font=fo, fill=GOLD)
    sub = "FINANCE TEMPLATES"
    fs = f(SANS_B, 26)
    d.text(((W - d.textlength(sub, font=fs)) / 2, 372), sub, font=fs, fill="#C8D2E0")
    return im


def build_brand():
    folder = os.path.join(OUT, "00-shop")
    os.makedirs(folder, exist_ok=True)
    shop_banner().save(os.path.join(folder, "shop-banner-1600x400.png"), optimize=True)
    shop_icon().save(os.path.join(folder, "shop-icon-500x500.png"), optimize=True)
    print("images: 00-shop (banner + icon)")
