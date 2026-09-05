"""Shared PDF builder for Joshi Finance Templates guides."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate)

NAVY = colors.HexColor("#0A1628")
MID = colors.HexColor("#0D1F3C")
GOLD = colors.HexColor("#C9A84C")
TEAL = colors.HexColor("#00B4A6")
GREY = colors.HexColor("#5A6879")
LIGHT = colors.HexColor("#EDF1F6")
WHITE = colors.white

BRAND = "Joshi Finance Templates"
AUTHOR = "Kartik Joshi, MBA"

S = {
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=19, leading=23,
                         textColor=MID, spaceBefore=6, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                         textColor=TEAL, spaceBefore=13, spaceAfter=5),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
                         textColor=MID, spaceBefore=9, spaceAfter=3),
    "p": ParagraphStyle("p", fontName="Helvetica", fontSize=9.7, leading=14.4,
                        textColor=colors.HexColor("#24303F"), spaceAfter=6, alignment=TA_LEFT),
    "li": ParagraphStyle("li", fontName="Helvetica", fontSize=9.7, leading=14.2,
                         textColor=colors.HexColor("#24303F"), spaceAfter=3),
    "small": ParagraphStyle("small", fontName="Helvetica-Oblique", fontSize=8.2, leading=11.5,
                            textColor=GREY, spaceAfter=5),
    "cover_t": ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=30, leading=35,
                              textColor=WHITE, alignment=TA_CENTER),
    "cover_s": ParagraphStyle("cs", fontName="Helvetica", fontSize=12.5, leading=18,
                              textColor=GOLD, alignment=TA_CENTER),
    "cover_b": ParagraphStyle("cb", fontName="Helvetica", fontSize=10, leading=15,
                              textColor=colors.HexColor("#C8D2E0"), alignment=TA_CENTER),
    "quote": ParagraphStyle("q", fontName="Helvetica-Oblique", fontSize=9.7, leading=14,
                            textColor=MID, leftIndent=10, spaceAfter=6),
}


def _marker_list(items, markers, style="li"):
    rows = [[Paragraph(m, ParagraphStyle("mk", fontName="Helvetica-Bold", fontSize=9.7,
                                         leading=14.2, textColor=TEAL)),
             Paragraph(t, S[style])] for m, t in zip(markers, items)]
    t = Table(rows, colWidths=[0.28 * inch, 6.32 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 6), ("LEFTPADDING", (1, 0), (1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def bullets(items, style="li"):
    return _marker_list(items, ["\u2022"] * len(items), style)


def numbered(items):
    return _marker_list(items, [f"{i}." for i in range(1, len(items) + 1)])


def box(title, body_items, color=LIGHT):
    inner = [Paragraph(f"<b>{title}</b>", S["h3"])]
    for t in body_items:
        inner.append(Paragraph(t, S["p"]))
    t = Table([[inner]], colWidths=[6.6 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#C7D0DB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([Spacer(1, 4), t, Spacer(1, 8)])


def table(rows, widths, header=True):
    data = [[Paragraph(f"<b>{c}</b>" if header and r == 0 else c,
                       S["li"] if not (header and r == 0) else
                       ParagraphStyle("th", parent=S["li"], textColor=WHITE))
             for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#C7D0DB")),
             ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
             ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
             ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#F6F8FB")])]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), TEAL))
    t.setStyle(TableStyle(style))
    return [Spacer(1, 3), t, Spacer(1, 8)]


def checklist(items):
    rows = [["", it] for it in items]
    t = Table(rows, colWidths=[0.3 * inch, 6.3 * inch])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (0, -1), 0.8, MID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (1, 0), (1, -1), 9.7),
        ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#24303F")),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (1, 0), (1, -1), 10),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]


class Doc(BaseDocTemplate):
    def __init__(self, path, title, subtitle):
        super().__init__(path, pagesize=LETTER, title=title, author=f"{AUTHOR} — {BRAND}",
                         leftMargin=0.95 * inch, rightMargin=0.95 * inch,
                         topMargin=0.95 * inch, bottomMargin=0.85 * inch)
        self.doc_title, self.doc_sub = title, subtitle
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="n")
        cover = Frame(0.7 * inch, 0.7 * inch, LETTER[0] - 1.4 * inch, LETTER[1] - 1.4 * inch, id="c")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover], onPage=self._cover),
            PageTemplate(id="body", frames=[frame], onPage=self._chrome),
        ])

    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, LETTER[1] - 0.28 * inch, LETTER[0], 0.28 * inch, fill=1, stroke=0)
        canv.setFillColor(TEAL)
        canv.rect(0, 0, LETTER[0], 0.16 * inch, fill=1, stroke=0)
        canv.restoreState()

    def _chrome(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, LETTER[1] - 0.42 * inch, LETTER[0], 0.42 * inch, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.setFont("Helvetica-Bold", 8)
        canv.drawString(0.95 * inch, LETTER[1] - 0.28 * inch, BRAND.upper())
        canv.setFillColor(colors.HexColor("#8A97AB"))
        canv.setFont("Helvetica", 8)
        canv.drawRightString(LETTER[0] - 0.95 * inch, LETTER[1] - 0.28 * inch, self.doc_title)
        canv.setStrokeColor(colors.HexColor("#C7D0DB"))
        canv.setLineWidth(0.5)
        canv.line(0.95 * inch, 0.62 * inch, LETTER[0] - 0.95 * inch, 0.62 * inch)
        canv.setFillColor(GREY)
        canv.setFont("Helvetica", 7.6)
        canv.drawString(0.95 * inch, 0.45 * inch,
                        f"{BRAND} · single-user licence · not financial, tax or legal advice")
        canv.drawRightString(LETTER[0] - 0.95 * inch, 0.45 * inch, f"Page {doc.page - 1}")
        canv.restoreState()


def cover_page(title, subtitle, blurb, bullets_):
    els = [Spacer(1, 2.1 * inch),
           Paragraph(title, S["cover_t"]), Spacer(1, 0.22 * inch),
           Paragraph(subtitle, S["cover_s"]), Spacer(1, 0.5 * inch),
           Paragraph(blurb, S["cover_b"]), Spacer(1, 0.4 * inch)]
    for b in bullets_:
        els.append(Paragraph(b, S["cover_b"]))
    els += [Spacer(1, 0.9 * inch),
           NextPageTemplate("body"),
            Paragraph(f"{AUTHOR} &nbsp;·&nbsp; {BRAND}", S["cover_b"]),
            Paragraph("Financial Analyst &amp; Banking Professional &nbsp;·&nbsp; Cornwall, Ontario", S["cover_b"]),
            PageBreak()]
    return els


LICENCE = (
    "<b>Licence.</b> This guide is sold for the personal use of a single buyer. You may print it and use it "
    "for yourself. You may not resell it, share it, upload it anywhere, or reproduce it in any product of "
    "your own. All rights reserved."
)
DISCLAIM = (
    "<b>Important.</b> This guide is educational only. It is not financial, tax, immigration, investment or "
    "legal advice, and it does not create an advisor relationship. Rules, limits and rates change — confirm "
    "anything you plan to act on with the relevant authority (CRA, your bank, a licensed advisor) first."
)
