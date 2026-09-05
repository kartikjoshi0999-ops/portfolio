# Joshi Finance Templates — Etsy shop

Everything needed to run the Etsy shop: the products themselves, the listing images, and the
copy-and-paste listing kit.

```
shop/
├── build/          Python generators — the source of truth for every product
│   ├── kjstyle.py      shared Excel styling
│   ├── kjpdf.py        shared PDF layout
│   ├── catalog*.py     product data: prices, titles, tags, descriptions, image content
│   ├── p1..p8_*.py     one script per product
│   ├── mockups.py      listing images, shop banner and icon
│   └── gen_listings.py builds the Etsy listing kit from the catalog
├── dist/           what you actually upload to Etsy
│   ├── *.xlsx / *.pdf      the 8 products
│   └── images/             4 listing images per listing, plus shop banner and icon
└── etsy/           the listing kit
    ├── 00-SHOP-SETUP.md      shop identity, about, policies, FAQs, message to buyers
    ├── 01..09-*.md           one file per listing: title, price, description, tags, files, images
    ├── PRICING-AND-FEES.md   the fee stack and what you keep on every sale
    └── LAUNCH-CHECKLIST.md   the order to do it in
```

## The nine listings

| # | Product | Price (CAD) | File |
|---|---|---|---|
| 01 | Canadian Budget & Cash-Flow Tracker | $9.99 | xlsx |
| 02 | TFSA vs RRSP Contribution Planner | $8.99 | xlsx |
| 03 | Debt Payoff Planner — Snowball & Avalanche | $7.99 | xlsx |
| 04 | Investment Portfolio Tracker | $12.99 | xlsx |
| 05 | Small Business 12-Month Cash Flow Forecast | $16.99 | xlsx |
| 06 | 3-Statement Financial Model Template | $27.99 | xlsx |
| 07 | Newcomer to Canada — Money Starter Kit | $7.99 | pdf, 13 pages |
| 08 | Finance & Banking Interview Prep Pack | $11.99 | pdf, 12 pages |
| 09 | The Complete Finance Bundle — all 8 | $49.99 | 8 files |

Buying all eight separately costs $104.92, so the bundle saves $54.93 (52%).

## Rebuilding the products

```bash
cd shop/build
pip install openpyxl reportlab pillow
python3 p1_budget.py && python3 p2_tfsa_rrsp.py && python3 p3_debt.py && python3 p4_portfolio.py
python3 p5_cashflow.py && python3 p6_model.py && python3 p7_newcomer.py && python3 p8_interview.py
python3 -c "import catalog, mockups; [mockups.build(p) for p in catalog.ALL]; mockups.build_brand()"
python3 gen_listings.py
```

Change a price or a tag in `catalog_a.py` / `catalog_b.py`, re-run `gen_listings.py` and `mockups.py`,
and the listing kit and the images both update.

## A note on the spreadsheets

Every workbook is written with `fullCalcOnLoad` set, so Excel, Google Sheets, Numbers and LibreOffice
all recalculate the moment the file opens — a buyer never sees an empty template. The formulas in
products 02, 03, 04, 05 and 06 were verified numerically by recalculating the built files and checking
the results (the 3-statement model balances in every forecast year and its cash flow ties back to the
balance sheet).
