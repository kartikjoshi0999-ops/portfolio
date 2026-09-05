import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import LineChart, Reference
from kjstyle import *

OUT = os.path.join(os.path.dirname(__file__), "..", "dist")
TFSA = [(2009,5000),(2010,5000),(2011,5000),(2012,5000),(2013,5500),(2014,5500),(2015,10000),
        (2016,5500),(2017,5500),(2018,5500),(2019,6000),(2020,6000),(2021,6000),(2022,6000),
        (2023,6500),(2024,7000),(2025,7000),(2026,7000)]
RRSP = [(2019,26500),(2020,27230),(2021,27830),(2022,29210),(2023,30780),(2024,31560),
        (2025,32490),(2026,33810)]

wb = Workbook(); wb.remove(wb.active)

# ---------- Inputs ----------
i = wb.create_sheet("Your Numbers")
title_block(i, "Your Numbers", "Fill in the yellow cells. Everything else calculates.", 5)
section(i, 4, "ABOUT YOU", 5)
labels = [
    ("Your name", "", None),
    ("Current age", 30, '0'),
    ("Year you turned 18", 2013, '0'),
    ("Planning year", 2026, '0'),
    ("Province / territory", "Ontario", None),
]
r = 5
for lab, val, fmt in labels:
    i.cell(row=r, column=1, value=lab).font = Font(bold=True)
    input_cell(i, f"B{r}", val, fmt); r += 1
note(i, r, "TFSA room only starts building the year you turn 18 AND become a Canadian resident.")
r += 2
section(i, r, "INCOME & TAX", 5); r += 1
tax = [
    ("Gross earned income this year", 78000, '$#,##0'),
    ("Marginal tax rate NOW (combined fed + prov)", 0.2965, '0.00%'),
    ("Expected marginal tax rate IN RETIREMENT", 0.2005, '0.00%'),
    ("Employer pension adjustment (from box 52 of your T4)", 0, '$#,##0'),
]
INC_ROW = r
for lab, val, fmt in tax:
    i.cell(row=r, column=1, value=lab).font = Font(bold=True)
    input_cell(i, f"B{r}", val, fmt); r += 1
note(i, r, "Marginal rate = the tax you pay on your NEXT dollar of income, not your average rate.")
r += 2
section(i, r, "WHAT YOU HAVE ALREADY", 5); r += 1
have = [
    ("Total TFSA contributions made to date", 21000, '$#,##0'),
    ("Total TFSA withdrawals in PREVIOUS years", 0, '$#,##0'),
    ("Unused RRSP room from your latest CRA notice", 44000, '$#,##0'),
    ("RRSP contributions already made this year", 3000, '$#,##0'),
]
HAVE_ROW = r
for lab, val, fmt in have:
    i.cell(row=r, column=1, value=lab).font = Font(bold=True)
    input_cell(i, f"B{r}", val, fmt); r += 1
note(i, r, "Your CRA My Account notice of assessment is the authoritative source for both room figures.")
r += 2
section(i, r, "PLANNING ASSUMPTIONS", 5); r += 1
ass = [
    ("Amount you can save per year", 12000, '$#,##0'),
    ("Expected annual investment return", 0.06, '0.00%'),
    ("Years until you draw the money", 25, '0'),
]
ASS_ROW = r
for lab, val, fmt in ass:
    i.cell(row=r, column=1, value=lab).font = Font(bold=True)
    input_cell(i, f"B{r}", val, fmt); r += 1
widths(i, {"A": 52, "B": 18})
i.sheet_view.showGridLines = False

AGE, T18, PY = "'Your Numbers'!$B$6", "'Your Numbers'!$B$7", "'Your Numbers'!$B$8"
INC, MTR_NOW, MTR_RET, PA = [f"'Your Numbers'!$B${INC_ROW+k}" for k in range(4)]
TFSA_MADE, TFSA_WD, RRSP_ROOM, RRSP_MADE = [f"'Your Numbers'!$B${HAVE_ROW+k}" for k in range(4)]
SAVE, RET, YRS = [f"'Your Numbers'!$B${ASS_ROW+k}" for k in range(3)]

# ---------- TFSA ----------
t = wb.create_sheet("TFSA Room")
title_block(t, "TFSA Room", "Year-by-year contribution room from 2009 to today.", 4)
header_row(t, 4, ["Year", "Annual TFSA limit", "Counts for you?", "Room earned"])
r = 5
for yr, lim in TFSA:
    t.cell(row=r, column=1, value=yr).border = BOX
    t.cell(row=r, column=2, value=lim).border = BOX; t["B%d" % r].number_format = '$#,##0'
    calc_cell(t, f"C{r}", f'=IF(AND(A{r}>={T18},A{r}<={PY}),"Yes","No")')
    calc_cell(t, f"D{r}", f'=IF(C{r}="Yes",B{r},0)', '$#,##0')
    r += 1
END = r - 1
r += 1
t.cell(row=r, column=1, value="Total room earned").font = Font(bold=True)
calc_cell(t, f"B{r}", f"=SUM(D5:D{END})", '$#,##0', bold=True); TOTROOM = r; r += 1
t.cell(row=r, column=1, value="Less: contributions made").font = Font(bold=True)
calc_cell(t, f"B{r}", f"={TFSA_MADE}", '$#,##0'); r += 1
t.cell(row=r, column=1, value="Add back: prior-year withdrawals").font = Font(bold=True)
calc_cell(t, f"B{r}", f"={TFSA_WD}", '$#,##0'); r += 1
t.cell(row=r, column=1, value="ROOM AVAILABLE TODAY").font = Font(bold=True, size=12, color=MID)
calc_cell(t, f"B{r}", f"=B{TOTROOM}-B{TOTROOM+1}+B{TOTROOM+2}", '$#,##0', bold=True)
TFSA_AVAIL = f"'TFSA Room'!$B${r}"; r += 2
note(t, r, "2026 limit shown as $7,000 — confirm on canada.ca before you rely on it; the limit is indexed each year.")
note(t, r+1, "Money withdrawn from a TFSA comes back as room on January 1 of the FOLLOWING year, never the same year.")
note(t, r+2, "Over-contributing costs 1% of the excess per month. Check CRA My Account if you are close to the line.")
widths(t, {"A": 12, "B": 22, "C": 18, "D": 16})
t.sheet_view.showGridLines = False

# ---------- RRSP ----------
q = wb.create_sheet("RRSP Room")
title_block(q, "RRSP Room", "18% of earned income, capped at the annual dollar limit.", 4)
header_row(q, 4, ["Year", "Annual RRSP dollar limit"])
r = 5
for yr, lim in RRSP:
    q.cell(row=r, column=1, value=yr).border = BOX
    q.cell(row=r, column=2, value=lim).border = BOX; q[f"B{r}"].number_format = '$#,##0'
    r += 1
LIMEND = r - 1; r += 1
section(q, r, "THIS YEAR'S ROOM", 4); r += 1
q.cell(row=r, column=1, value="18% of earned income").font = Font(bold=True)
calc_cell(q, f"B{r}", f"=0.18*{INC}", '$#,##0'); P = r; r += 1
q.cell(row=r, column=1, value=f"Dollar limit for the planning year").font = Font(bold=True)
calc_cell(q, f"B{r}", f'=IFERROR(VLOOKUP({PY},A5:B{LIMEND},2,FALSE),MAX(B5:B{LIMEND}))', '$#,##0'); r += 1
q.cell(row=r, column=1, value="New room earned (lesser of the two)").font = Font(bold=True)
calc_cell(q, f"B{r}", f"=MIN(B{P},B{P+1})", '$#,##0'); r += 1
q.cell(row=r, column=1, value="Less: pension adjustment").font = Font(bold=True)
calc_cell(q, f"B{r}", f"={PA}", '$#,##0'); r += 1
q.cell(row=r, column=1, value="Plus: unused room carried forward").font = Font(bold=True)
calc_cell(q, f"B{r}", f"={RRSP_ROOM}", '$#,##0'); r += 1
q.cell(row=r, column=1, value="Less: contributions already made").font = Font(bold=True)
calc_cell(q, f"B{r}", f"={RRSP_MADE}", '$#,##0'); r += 1
q.cell(row=r, column=1, value="ROOM AVAILABLE TODAY").font = Font(bold=True, size=12, color=MID)
calc_cell(q, f"B{r}", f"=B{P+2}-B{P+3}+B{P+4}-B{P+5}", '$#,##0', bold=True)
RRSP_AVAIL = f"'RRSP Room'!$B${r}"; r += 1
q.cell(row=r, column=1, value="Tax refund if you contribute it all").font = Font(bold=True)
calc_cell(q, f"B{r}", f"=MAX(0,B{P+6})*{MTR_NOW}", '$#,##0', bold=True); r += 2
note(q, r, "Dollar limits are as published by CRA; the 2026 figure is indexed — verify before filing.")
note(q, r+1, "You have a $2,000 lifetime over-contribution cushion, but it is not deductible. Do not lean on it.")
widths(q, {"A": 46, "B": 20})
q.sheet_view.showGridLines = False

# ---------- Compare ----------
c = wb.create_sheet("TFSA vs RRSP")
title_block(c, "TFSA vs RRSP", "Same dollars, both accounts, side by side after tax.", 6)
section(c, 4, "IF YOU PUT THIS YEAR'S SAVINGS IN ONE ACCOUNT", 6)
header_row(c, 5, ["", "TFSA route", "RRSP route", "What this line means"])
rows = [
    ("Amount contributed", f"={SAVE}", f"={SAVE}", "The same out-of-pocket dollars either way."),
    ("Immediate tax refund", "0", f"={SAVE}*{MTR_NOW}", "RRSP contributions are deductible; TFSA contributions are not."),
    ("Refund reinvested at the same return", "0", f"=C7*(1+{RET})^{YRS}", "Only counts if you actually invest the refund."),
    ("Value at the end of the horizon", f"=B6*(1+{RET})^{YRS}", f"=C6*(1+{RET})^{YRS}", "Growth before any tax on withdrawal."),
    ("Tax on withdrawal", "0", f"=-C9*{MTR_RET}", "RRSP/RRIF withdrawals are fully taxable as income."),
    ("Refund pot after tax (non-registered, simplified)", "0", f"=C8*(1-{MTR_RET}*0.5)", "Assumes the refund grows in a taxable account."),
    ("AFTER-TAX VALUE", "=B9", "=C9+C10+C11", "The number that actually matters."),
]
r = 6
for lab, bf, cf, why in rows:
    c.cell(row=r, column=1, value=lab).font = Font(bold=(lab == "AFTER-TAX VALUE"))
    calc_cell(c, f"B{r}", bf, '$#,##0', bold=(lab == "AFTER-TAX VALUE"))
    calc_cell(c, f"C{r}", cf, '$#,##0', bold=(lab == "AFTER-TAX VALUE"))
    c.cell(row=r, column=4, value=why).font = Font(size=9, italic=True, color=GREY)
    r += 1
r += 1
c.cell(row=r, column=1, value="WHICH ONE WINS FOR YOU").font = Font(bold=True, size=12, color=MID)
r += 1
calc_cell(c, f"A{r}", f'=IF({MTR_NOW}>{MTR_RET},"RRSP first — you deduct at a higher rate than you will pay on withdrawal.",'
                      f'IF({MTR_NOW}<{MTR_RET},"TFSA first — you would deduct at a low rate and pay tax at a higher one later.",'
                      f'"Close call — your rate now equals your expected rate later, so use the TFSA for flexibility."))')
c.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
c[f"A{r}"].font = Font(bold=True, size=11, color=MID)
c[f"A{r}"].alignment = Alignment(wrap_text=True, vertical="center")
c.row_dimensions[r].height = 32
r += 2
section(c, r, "YOUR ROOM, PULLED FROM THE OTHER TABS", 6); r += 1
c.cell(row=r, column=1, value="TFSA room available").font = Font(bold=True)
calc_cell(c, f"B{r}", f"={TFSA_AVAIL}", '$#,##0', bold=True); r += 1
c.cell(row=r, column=1, value="RRSP room available").font = Font(bold=True)
calc_cell(c, f"B{r}", f"={RRSP_AVAIL}", '$#,##0', bold=True); r += 1
c.cell(row=r, column=1, value="Total room available").font = Font(bold=True)
calc_cell(c, f"B{r}", f"=B{r-2}+B{r-1}", '$#,##0', bold=True)
widths(c, {"A": 46, "B": 18, "C": 18, "D": 52})
c.sheet_view.showGridLines = False

# ---------- Projection ----------
p = wb.create_sheet("Projection")
title_block(p, "Projection", "What steady contributions look like over time.", 5)
header_row(p, 4, ["Year", "Contributed this year", "Cumulative contributed", "Growth", "Balance"])
for k in range(30):
    r = 5 + k
    p.cell(row=r, column=1, value=k + 1).border = BOX
    calc_cell(p, f"B{r}", f'=IF(A{r}<={YRS},{SAVE},0)', '$#,##0')
    calc_cell(p, f"C{r}", (f"=B{r}" if k == 0 else f"=C{r-1}+B{r}"), '$#,##0')
    prev = "0" if k == 0 else f"E{r-1}"
    calc_cell(p, f"D{r}", f"=({prev}+B{r})*{RET}", '$#,##0')
    calc_cell(p, f"E{r}", f"={prev}+B{r}+D{r}", '$#,##0', bold=True)
ch = LineChart(); ch.title = "Projected balance"; ch.height = 9; ch.width = 20
ch.add_data(Reference(p, min_col=5, min_row=4, max_row=34), titles_from_data=True)
ch.set_categories(Reference(p, min_col=1, min_row=5, max_row=34))
p.add_chart(ch, "G5")
widths(p, {"A": 8, "B": 20, "C": 22, "D": 14, "E": 16})
p.sheet_view.showGridLines = False

start_here(wb, "TFSA vs RRSP Contribution Planner (Canada)",
    "Know your real room, and know which account to fill first.",
    ["Fill in the yellow cells on the Your Numbers tab — that is the only typing you do.",
     "Open TFSA Room: it builds your room year by year from the date you turned 18.",
     "Open RRSP Room: 18% of earned income against the annual cap, plus your carry-forward.",
     "Open TFSA vs RRSP for the side-by-side after-tax answer and a plain-English verdict.",
     "Use Projection to see what steady contributions turn into over your time horizon."],
    ["Your Numbers — every input in one place.",
     "TFSA Room — 2009-2026 limits table with your personal room calculated.",
     "RRSP Room — 18% rule, dollar cap, pension adjustment and carry-forward.",
     "TFSA vs RRSP — after-tax comparison with an automatic verdict line.",
     "Projection — 30-year contribution and growth schedule with a chart."])
finish(wb, os.path.join(OUT, "02-TFSA-vs-RRSP-Contribution-Planner.xlsx"))
