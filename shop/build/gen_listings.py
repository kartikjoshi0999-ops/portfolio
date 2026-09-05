# -*- coding: utf-8 -*-
"""Generate the copy-and-paste Etsy listing kit from the catalog."""
import os, catalog

HERE = os.path.dirname(os.path.abspath(__file__))
ETSY = os.path.join(HERE, "..", "etsy")
os.makedirs(ETSY, exist_ok=True)

TRANSACTION, PROCESS_PC, PROCESS_FLAT = 0.065, 0.03, 0.25
LISTING_USD, FX = 0.20, 1.36
OFFSITE = 0.15


def net(price, offsite=False):
    fees = price * TRANSACTION + price * PROCESS_PC + PROCESS_FLAT + LISTING_USD * FX
    if offsite:
        fees += price * OFFSITE
    return price - fees, fees


ABOUT = (
    "ABOUT THE MAKER\n"
    "I am Kartik Joshi, a Financial Analyst and Banking Professional based in Cornwall, Ontario. "
    "I have worked in retail banking at BMO, in payments and audit at Deutsche Bank, and in AML, KYC "
    "and FINTRAC compliance in Canada and India. I hold an MBA in Finance and Marketing (WES-evaluated "
    "as a Canadian Master's equivalent), the CBCA and FMVA designations from the Corporate Finance "
    "Institute, and the Canadian Investment Funds Course.\n"
    "Everything in this shop is something I built for my own work first, then cleaned up so somebody "
    "else could use it. If you get stuck, message me — I answer my own messages."
)

DELIVERY = (
    "HOW DELIVERY WORKS\n"
    "This is a digital download. Nothing is shipped.\n"
    "1. Buy the listing.\n"
    "2. Etsy emails you a download link as soon as payment clears, and the files also appear under "
    "Purchases and Reviews in your Etsy account.\n"
    "3. Download, open, and start using it. The file is yours to keep — no subscription, no login, no expiry."
)

TERMS = (
    "LICENCE AND TERMS\n"
    "This is a single-user licence for your own personal or business use. You may edit it and print it "
    "for yourself. You may not resell it, share it, or include it in a product of your own.\n"
    "Because this is an instant digital download, it cannot be returned once it has been delivered. "
    "That said, I care more about a fair shop than a single sale: if a file will not open, is corrupted, "
    "or is not what the listing described, message me and I will fix it or refund you."
)

DISCLAIMER = (
    "IMPORTANT\n"
    "These templates and guides are educational planning tools. They are not financial, tax, investment, "
    "immigration or legal advice, and buying one does not create an advisor relationship. Contribution "
    "limits, tax rates and rules change — confirm current figures with the CRA or a licensed professional "
    "before acting on any output."
)


def description(p):
    L = []
    L.append(p["desc_open"])
    L.append("")
    L.append("WHAT YOU GET")
    for h in p["highlights"]:
        L.append("✓ " + h)
    L.append("")
    L.append("WHO IT IS FOR")
    L.append(p["desc_who"])
    L.append("")
    if p.get("inside"):
        L.append("WHAT IS IN THE FILE")
        for tab, desc in p["inside"]:
            L.append("• %s — %s" % (tab, desc))
        L.append("")
    L.append("WHAT YOU NEED")
    L.append(p["compat"])
    L.append("")
    L.append(DELIVERY); L.append("")
    L.append(TERMS); L.append("")
    L.append(DISCLAIMER); L.append("")
    L.append(ABOUT)
    return "\n".join(L)


def listing_file(p):
    n, f = net(p["price"])
    n_ads, _ = net(p["price"], offsite=True)
    files = "\n".join("   - shop/dist/%s" % x for x in p["files"])
    imgs = "\n".join("   %d. shop/dist/images/%s/%s.png" % (i, p["slug"], nm) for i, nm in
                     enumerate(["1-main", "2-preview", "3-inside", "4-details"], 1))
    body = f"""# Listing {p['num']} — {p['name']}

## 1. Title (copy exactly — {len(p['etsy_title'])}/140 characters)

{p['etsy_title']}

## 2. Price

**CAD ${p['price']:.2f}**  ·  Quantity: 999  ·  Type: **Digital** (instant download)

Estimated net after Etsy fees: **${n:.2f}** per sale (${n_ads:.2f} if the sale comes through Offsite Ads).
See PRICING-AND-FEES.md for the full working.

## 3. Description (paste into the Description box exactly as written)

```
{description(p)}
```

## 4. Tags (13 of 13 used — paste one per tag box)

{", ".join(p['tags'])}

## 5. Digital files to upload

{files}

## 6. Photos to upload, in this order

{imgs}

## 7. Listing settings

- Who made it: **I did**
- What is it: **A finished product**
- When was it made: **2020 – 2026**
- Category: **{p.get('category', 'Paper & Party Supplies > Paper > Stationery > Design & Templates')}**
- Type: **Digital** — this removes shipping entirely
- Renewal: **Automatic**
- Personalisation: **Off**
- Materials (optional): {p.get('materials', 'Microsoft Excel, spreadsheet formulas, financial modelling' if p.get('kind') != 'pdf' else 'PDF, original writing, financial guidance')}
"""
    return body


def main():
    for p in catalog.ALL:
        path = os.path.join(ETSY, "%s-%s.md" % (p["num"], p["slug"].split("-", 1)[1]))
        open(path, "w").write(listing_file(p))
        print("wrote", os.path.basename(path))

    # ---- pricing & fees ----
    rows = []
    for p in catalog.ALL:
        n, f = net(p["price"])
        na, fa = net(p["price"], offsite=True)
        rows.append("| {} | ${:.2f} | ${:.2f} | **${:.2f}** | ${:.2f} | **${:.2f}** |".format(
            p["name"], p["price"], f, n, fa, na))
    fees_md = f"""# Pricing and Etsy fees

All prices are **Canadian dollars**. Set your shop currency to CAD — you are based in Cornwall,
Ontario, and being billed in your own currency avoids Etsy's 2.5% currency conversion fee.

## The fee stack on a digital sale

| Fee | Rate used here |
|---|---|
| Listing fee | US$0.20 per listing, charged again each time an item sells (assumed FX {FX} → CAD ${LISTING_USD*FX:.2f}) |
| Transaction fee | {TRANSACTION*100:.1f}% of the item price |
| Payment processing (Canada) | {PROCESS_PC*100:.0f}% + CAD ${PROCESS_FLAT:.2f} |
| Offsite Ads | {OFFSITE*100:.0f}% of the order, **only** when a buyer arrives through an Etsy-placed ad |
| Regulatory operating fee | Does not apply to Canadian sellers today |

⚠️ **Verify these before you rely on them.** Etsy changes its fee schedule; the numbers above were
correct as a general structure but the authoritative source is etsy.com/legal/fees. The maths below
is what matters — plug in the current rates and the shape of the answer will not change.

## What you actually keep

| Product | Price | Fees | Net | Fees with Offsite Ads | Net with Offsite Ads |
|---|---|---|---|---|---|
{chr(10).join(rows)}

## Why these prices

- **Nothing under $7.99.** Below that, the flat CAD $0.25 processing fee plus the listing fee eats more
  than 8% of the sale, and cheap digital listings attract the most demanding buyers.
- **The three personal-finance templates sit at $7.99 – $9.99.** That is the band Etsy shoppers expect
  for a budget or debt spreadsheet, and it is where impulse purchases happen.
- **The portfolio tracker is $12.99** because the buyer already has money invested — the price is trivial
  next to what they are tracking.
- **The business cash flow model is $16.99 and the 3-statement model is $27.99.** These are professional
  tools bought with business money, and pricing them like consumer templates signals they are toys.
  The 3-statement model is comparable to templates sold for far more elsewhere.
- **The bundle at $49.99** is the listing you want people to buy: it is 52% off the ${sum(p['price'] for p in catalog.PRODUCTS):.2f}
  it would cost to buy all eight, and it more than doubles your average order value.

## Do not discount in the first 60 days

Run the shop at full price until you have 10 sales and 5 reviews. Discounting before you have social
proof trains buyers to wait for a sale and tells Etsy's search algorithm your listings are low value.
After that, a 15% off coupon for buyers who favourite the shop is the one promotion worth running.

## Raising prices later

Etsy rewards conversion, not cheapness. Once a listing has 10+ sales and a 4.8+ rating, raise it by
$2 – $3 and watch the conversion rate for two weeks. If it holds, keep the new price.
"""
    open(os.path.join(ETSY, "PRICING-AND-FEES.md"), "w").write(fees_md)
    print("wrote PRICING-AND-FEES.md")


if __name__ == "__main__":
    main()
