"""Package the bundle as a single ZIP — Etsy allows at most 5 files per listing."""
import os, zipfile, catalog

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "..", "dist")
OUT = os.path.join(DIST, "09-Complete-Finance-Bundle.zip")

README = """THE COMPLETE FINANCE BUNDLE
Joshi Finance Templates — Kartik Joshi, MBA
Financial Analyst & Banking Professional, Cornwall, Ontario

Thank you. All eight products are in this folder.

SPREADSHEETS (open in Excel, Google Sheets, Numbers or LibreOffice)
  01  Canadian Budget & Cash-Flow Tracker
  02  TFSA vs RRSP Contribution Planner
  03  Debt Payoff Planner — Snowball & Avalanche
  04  Investment Portfolio Tracker
  05  Small Business 12-Month Cash Flow Forecast
  06  3-Statement Financial Model Template

GUIDES (PDF — read on any device, or print)
  07  Newcomer to Canada — Money Starter Kit
  08  Finance & Banking Interview Prep Pack

WHERE TO START
Every spreadsheet opens on a Start Here tab. Read it first — it takes two
minutes and explains exactly which cells to type in. Yellow cells are yours.
Grey cells are formulas; leave them alone.

To open a spreadsheet in Google Sheets, upload the .xlsx to Google Drive and
open it with Sheets. Every formula carries over. Drop-down lists may need to
be re-applied and chart styling can shift slightly.

LICENCE
Single-user licence for your own personal or business use. Edit and print it
however you like. You may not resell it, share it, or include it in a product
of your own. All rights reserved.

IMPORTANT
These are educational planning tools, not financial, tax, investment or legal
advice, and buying them does not create an advisor relationship. Contribution
limits and tax rules change — confirm current figures with the CRA or a
licensed advisor before acting on anything a file tells you.

Something not working, or a question about your own situation? Message me
through Etsy. I answer my own messages.
"""


def build():
    files = [f for f in catalog.BUNDLE_FILES]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("READ ME FIRST.txt", README)
        for f in files:
            src = os.path.join(DIST, f)
            assert os.path.exists(src), src
            z.write(src, f)
    mb = os.path.getsize(OUT) / 1024 / 1024
    print("wrote %s (%d files, %.2f MB)" % (os.path.basename(OUT), len(files) + 1, mb))
    assert mb < 20, "Etsy caps a single digital file at 20 MB"


if __name__ == "__main__":
    build()
