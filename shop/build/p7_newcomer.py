import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak
from kjpdf import *

OUT = os.path.join(os.path.dirname(__file__), "..", "dist")
P = lambda t: Paragraph(t, S["p"])
H1 = lambda t: Paragraph(t, S["h1"])
H2 = lambda t: Paragraph(t, S["h2"])
H3 = lambda t: Paragraph(t, S["h3"])
SM = lambda t: Paragraph(t, S["small"])

doc = Doc(os.path.join(OUT, "07-Newcomer-to-Canada-Money-Starter-Kit.pdf"),
          "Newcomer to Canada — Money Starter Kit", "First 12 months")
e = cover_page(
    "Newcomer to Canada<br/>Money Starter Kit",
    "Your first 12 months of Canadian money, in order",
    "Written by a personal banker who arrived in Canada as a newcomer, worked the front line at a<br/>"
    "Canadian bank, and has opened hundreds of first accounts.",
    ["Week-one checklist · Banking · Credit · Taxes · TFSA, RRSP, FHSA, RESP",
     "Newcomer benefits and credits · Scams to refuse · A 12-month plan"])

e += [H1("How to use this kit"),
      P("You do not need to read this in one sitting. It runs in the order things actually happen: the "
        "documents you need first, then a bank account, then credit, then taxes, then saving and investing. "
        "Work through it section by section as each one becomes relevant to you."),
      P("Every section ends with something you can do this week. The last two pages are a printable "
        "12-month plan and a one-page checklist — print those and stick them somewhere you will see them."),
      box("A note on what this is not", [
          "This is a guide from a banking professional, not advice from your advisor. It explains how the "
          "Canadian system works so you can ask better questions and avoid expensive mistakes. Numbers such "
          "as contribution limits are stated with the year they apply to — always confirm the current figure "
          "on canada.ca before you act."]),
      SM(LICENCE), SM(DISCLAIM), PageBreak(),

      H1("1 · Your first two weeks"),
      P("Almost everything in Canadian financial life keys off two things: a Social Insurance Number (SIN) "
        "and a permanent address. Get those two sorted and the rest opens up."),
      H2("The documents to secure first"),
      numbered([
          "<b>Social Insurance Number (SIN).</b> Free, from Service Canada, in person or online. You cannot "
          "be paid legally, open most registered accounts, or file taxes without it. Temporary residents get "
          "a SIN starting with 9 and an expiry date — renew it when your permit is renewed.",
          "<b>Proof of address.</b> A lease, a utility bill, or a letter from your landlord. Banks ask for it, "
          "and so do phone and insurance companies.",
          "<b>Photo ID.</b> Your passport plus one more piece. A provincial photo card or driver's licence is "
          "worth getting early — many places will not accept a foreign licence as primary ID.",
          "<b>Immigration documents.</b> Keep your COPR, PR card, work permit or study permit together, plus "
          "digital copies in cloud storage you can reach from any device.",
          "<b>Health card.</b> Apply the day you are eligible in your province. Some provinces have a waiting "
          "period — buy private coverage for the gap if yours does.",
      ]),
      box("Do this week", [
          "Apply for your SIN. Photograph every document you own, front and back, and store the images in "
          "cloud storage. Write down the phone number of the nearest Service Canada office."]),

      H2("What things actually cost in month one"),
      P("Newcomers are routinely caught out by the deposits and up-front costs nobody mentions. Budget for "
        "these before you budget for anything else:"),
      table([["Cost", "Typical range", "Notes"],
             ["Rent deposit", "First and last month's rent", "Ontario landlords can ask for last month's rent, not a damage deposit."],
             ["Utility deposits", "$100 – $400", "Often waived once you have a Canadian credit history."],
             ["Phone plan", "$35 – $70 / month", "A postpaid plan may need a credit check or a deposit at first."],
             ["Internet", "$50 – $95 / month", "Ask for the new-customer promotional rate; it is rarely offered."],
             ["Tenant insurance", "$18 – $35 / month", "Many leases require it. It is cheap and worth it regardless."],
             ["Transit or car", "$100 – $700 / month", "Insurance for a new Canadian driver is the expensive part, not the car."],
             ["Winter clothing", "$250 – $600 once", "One good coat and proper boots. Do not economise here."]],
            [1.5 * inch, 1.5 * inch, 3.6 * inch]),
      PageBreak(),

      H1("2 · Opening your first bank account"),
      P("Every large Canadian bank runs a newcomer package. They exist because banks compete hard for "
        "newcomer clients — which means you have more negotiating room than you think in your first year."),
      H2("What to bring"),
      bullets(["Passport, plus your immigration document (COPR, PR card, work or study permit).",
               "Your SIN — legally optional for a chequing account, required for any account that earns interest "
               "or for registered accounts.",
               "Proof of address if you have one. Many banks will open an account without it and update later.",
               "If you are employed, a job offer letter or a recent pay stub helps with credit products."]),
      H2("What a newcomer package normally includes"),
      bullets(["<b>No monthly chequing fee</b> for 6 to 12 months. Ask exactly when the fee starts and set a "
               "calendar reminder for one month before that date.",
               "<b>A credit card with no or limited credit history required</b> — sometimes secured, sometimes not.",
               "<b>A free safety deposit box or free drafts</b> for the first year.",
               "<b>Waived transfer fees</b> on your first international transfer."]),
      box("The three questions that save you the most money", [
          "1. What is the monthly fee after the promotional period ends, and what balance waives it permanently?",
          "2. Is the credit card you are offering secured or unsecured, and does it report to both Equifax and TransUnion?",
          "3. What is your foreign-exchange spread on transfers — not the fee, the spread? A '$0 fee' transfer with "
          "a 3% spread is far more expensive than a $15 transfer at 0.5%."]),
      H2("Fees worth knowing before they hit you"),
      table([["Fee", "Typical", "How to avoid it"],
             ["Monthly account fee", "$4 – $17", "Keep the minimum balance, or use a no-fee online bank for day-to-day."],
             ["Non-network ATM", "$3 – $6 plus the ATM's own fee", "Use your own bank's machines, or get cash back at a grocery till."],
             ["Overdraft", "$5 monthly plus ~21% interest", "Turn it off unless you genuinely need it."],
             ["NSF / returned payment", "$45 – $50", "Keep a $200 buffer. This single fee is the most common newcomer cost."],
             ["Foreign transaction", "2.5% of the purchase", "A no-FX-fee card pays for itself if you shop in USD."],
             ["Wire transfer in", "$15 – $30", "Ask whether the intermediary bank also deducts a fee."]],
            [1.6 * inch, 1.7 * inch, 3.3 * inch]),
      SM("Fee ranges are indicative of major Canadian banks and change; check your own bank's current fee schedule."),
      PageBreak(),

      H1("3 · Building Canadian credit from zero"),
      P("Your credit history from another country does not come with you. On day one in Canada you have no "
        "score — which is not the same as a bad score, but lenders treat it cautiously. Landlords, insurers, "
        "phone companies and lenders all look at it. Building it is slow, simple, and almost entirely "
        "mechanical."),
      H2("What a Canadian credit score is made of"),
      table([["Factor", "Weight (approx.)", "What to actually do"],
             ["Payment history", "~35%", "Never miss a payment. Automate the minimum, then pay the rest manually."],
             ["Credit utilisation", "~30%", "Keep balances under 30% of your limit — ideally under 10%."],
             ["Length of history", "~15%", "Never close your oldest card. Age is something you cannot buy back."],
             ["Credit mix", "~10%", "A card plus one instalment loan beats three cards."],
             ["New enquiries", "~10%", "Hard checks sting for a few months. Do not apply for four cards in a week."]],
            [1.5 * inch, 1.2 * inch, 3.9 * inch]),
      H2("The first-year credit plan that works"),
      numbered([
          "Get one card in month one — secured if that is all you qualify for. A secured card is a normal card "
          "backed by a deposit you get back; it reports to the bureaus exactly like any other card.",
          "Put one small recurring bill on it, such as your phone or a streaming subscription. Nothing else.",
          "Set up autopay for the full statement balance, not the minimum. Interest at 20%+ destroys any reward.",
          "Wait six months without applying for anything else. Enquiries in a cluster look like distress.",
          "At month seven, ask for a limit increase rather than a second card. A higher limit with the same "
          "spending lowers your utilisation, which raises your score.",
          "At month twelve, ask your bank to convert a secured card to unsecured and refund the deposit.",
      ]),
      box("Two mistakes that cost newcomers years", [
          "<b>Paying the minimum.</b> The minimum keeps you current but leaves a balance that compounds at over "
          "20%. It also keeps your utilisation high, which caps your score.",
          "<b>Closing the first card once a better one arrives.</b> That card is your longest history. Downgrade "
          "it to a no-fee version instead and keep it open forever."]),
      P("Both Equifax and TransUnion give you a free copy of your own report. Check both once a year — errors "
        "on newcomer files are common, especially when a name is transliterated differently across institutions."),
      PageBreak(),

      H1("4 · Taxes in Canada — the short version"),
      P("If you were resident in Canada for any part of the year, you file. File even with no income: benefits "
        "and credits are paid out based on a filed return, so not filing simply means not being paid."),
      H2("The calendar"),
      table([["When", "What happens"],
             ["January – March", "T4s, T4As and T5s arrive from employers and banks. Keep every slip."],
             ["Late February", "CRA opens electronic filing for the previous tax year."],
             ["April 30", "Filing and payment deadline for most individuals."],
             ["June 15", "Filing deadline if you or your spouse are self-employed (tax still due April 30)."],
             ["Within weeks of filing", "Notice of Assessment arrives — this document holds your RRSP room. Keep it."]],
            [1.7 * inch, 4.9 * inch]),
      H2("Credits and benefits newcomers most often miss"),
      bullets([
          "<b>GST/HST credit</b> — a quarterly payment for low and modest income households. Newcomers apply "
          "with form RC151 for the first year rather than waiting for a return.",
          "<b>Canada Child Benefit (CCB)</b> — monthly, tax-free, per child. Apply with RC66 as soon as you arrive; "
          "it is not automatic for newcomers.",
          "<b>Provincial credits</b> — for example the Ontario Trillium Benefit, which covers energy and property "
          "tax costs including rent paid.",
          "<b>Canada Workers Benefit</b> — a refundable credit for lower-income working people.",
          "<b>Moving expenses</b> — deductible if you moved <i>within</i> Canada at least 40 km closer to work or "
          "school. Moving to Canada from abroad does not qualify.",
          "<b>Tuition amounts</b> — carry forward and reduce tax in later, higher-income years.",
      ]),
      box("Set up CRA My Account in your first year", [
          "It shows your TFSA and RRSP room, your benefit payment dates, your Notices of Assessment and your "
          "filed returns. Registering takes a few days because CRA mails you a security code — start it early, "
          "and never pay a third party to do it for you."]),
      P("<b>Departure and world income.</b> Once you are a Canadian resident for tax purposes you report your "
        "<i>worldwide</i> income, not just Canadian income. If you hold foreign property costing more than "
        "CAD $100,000 in total, form T1135 applies. If you have income, property or pensions abroad, pay for one "
        "hour with an accountant in your first year. It is the cheapest insurance in this guide."),
      PageBreak(),

      H1("5 · The registered accounts, plainly"),
      P("Canada gives you several tax-sheltered accounts. They are containers, not investments — you choose "
        "what goes inside. Fill them in the order that fits your situation."),
      table([["Account", "What it does", "Best used for"],
             ["<b>TFSA</b>", "Grows tax-free; withdrawals are tax-free and come back as room the following January.",
              "Everything from an emergency fund to long-term investing. The most flexible account in the country."],
             ["<b>RRSP</b>", "Contributions are deductible now; withdrawals are taxed as income later.",
              "When your income today is higher than the income you expect in retirement."],
             ["<b>FHSA</b>", "Deductible like an RRSP <i>and</i> tax-free on qualifying withdrawal like a TFSA.",
              "A first home. If you qualify, this is usually the strongest account available to you."],
             ["<b>RESP</b>", "Government grants 20% of contributions (CESG), up to $500 per child each year.",
              "Children's education. The grant is free money — few things beat a guaranteed 20%."]],
            [0.85 * inch, 2.6 * inch, 3.15 * inch]),
      H2("Rules newcomers get caught by"),
      bullets([
          "<b>TFSA room starts when you become a Canadian resident</b>, not when you turn 18 abroad. Arriving in "
          "2026 at age 35 means one year of room, not seventeen.",
          "<b>Over-contributing to a TFSA costs 1% of the excess per month</b>, and CRA does find it. Check your "
          "room in CRA My Account, not from memory.",
          "<b>Re-contributing a withdrawal in the same year is the classic error.</b> Withdraw in March, "
          "re-contribute in June, and you have over-contributed. The room returns on January 1.",
          "<b>RRSP room needs Canadian earned income first.</b> Your first year of employment generates the room "
          "you can use the following year.",
          "<b>US citizens and green-card holders:</b> TFSAs are often a poor choice because the IRS does not "
          "recognise the shelter. Get cross-border advice before opening one.",
      ]),
      PageBreak(),

      H1("6 · Sending money home without losing 4%"),
      P("The advertised fee is rarely the cost. The cost is the exchange-rate spread — the gap between the rate "
        "you are given and the real mid-market rate. A transfer with a $0 fee and a 3% spread costs $30 on "
        "$1,000; a $12 transfer at a 0.5% spread costs $17."),
      numbered([
          "Look up today's real mid-market rate for the currency pair before you start.",
          "Ask the provider for the exact rate they will apply, then calculate the gap as a percentage.",
          "Add the stated fee and any receiving-bank fee at the other end.",
          "Compare that total across a bank wire, a licensed money transfer operator, and a low-cost digital "
          "provider. For most corridors, the bank wire is the most expensive option.",
      ]),
      box("Refuse these, always", [
          "Anyone who calls claiming to be CRA, immigration, or the police and asks for payment in gift cards, "
          "cryptocurrency, or an e-transfer to keep your status. Every one of these is a scam. CRA does not "
          "threaten arrest or deportation over the phone, and no Canadian government body has ever asked for "
          "payment in gift cards.",
          "Anyone offering to 'hold' money in your account for a fee, or to pay you to receive transfers. That is "
          "money laundering, and the account holder is the one who is charged.",
          "Job offers that require you to pay first, or that pay you by cheque and ask you to wire part of it back."]),
      PageBreak(),

      H1("7 · Your 12-month money plan"),
      table([["Month", "What to do"],
             ["1", "SIN. Bank account. Tenant insurance. Photograph every document. Set a phone budget."],
             ["2", "One credit card, one small recurring bill on it, autopay the full balance."],
             ["3", "Health card. Provincial ID or driver's licence process started. Register for CRA My Account."],
             ["4", "Build a one-month emergency fund in a separate high-interest savings account."],
             ["5", "Review every subscription and bank fee. Cancel or renegotiate two of them."],
             ["6", "Check your credit report at both bureaus. Correct any errors in your name or address."],
             ["7", "Ask for a credit limit increase — do not open a second card."],
             ["8", "Open a TFSA and automate a small monthly contribution, even $50."],
             ["9", "If you have children, apply for CCB and open an RESP to capture the grant."],
             ["10", "Grow the emergency fund toward three months of expenses."],
             ["11", "Gather tax slips. Book an accountant now if you have foreign income or property."],
             ["12", "File your return. Convert a secured card to unsecured. Review the whole year and reset."]],
            [0.7 * inch, 5.9 * inch]),
      PageBreak(),

      H1("Printable checklist"),
      H2("Documents"), checklist([
          "SIN received and stored securely",
          "Passport and immigration documents photographed and backed up to the cloud",
          "Proof of address obtained",
          "Provincial health card applied for",
          "Provincial photo ID or driver's licence started"]),
      H2("Banking"), checklist([
          "Chequing account opened under a newcomer package",
          "Date the monthly fee begins written in my calendar",
          "High-interest savings account opened for the emergency fund",
          "Overdraft protection switched off unless genuinely needed",
          "Direct deposit set up with my employer"]),
      H2("Credit"), checklist([
          "First credit card opened",
          "One recurring bill placed on it",
          "Autopay set to the full statement balance",
          "Credit report checked at Equifax and at TransUnion",
          "Limit increase requested at month seven"]),
      H2("Tax and benefits"), checklist([
          "CRA My Account registered",
          "GST/HST credit applied for (RC151 in the first year)",
          "Canada Child Benefit applied for, if applicable",
          "All tax slips collected",
          "Return filed by April 30"]),
      H2("Saving"), checklist([
          "One month of expenses saved",
          "TFSA opened and automated",
          "FHSA opened if buying a first home",
          "RESP opened if I have children",
          "Three months of expenses saved"]),
      Spacer(1, 0.2 * inch),
      SM("Written by Kartik Joshi, MBA — Financial Analyst and Banking Professional, Cornwall, Ontario. "
         "Questions about this guide? Message me through Etsy and I will answer personally."),
      SM(LICENCE), SM(DISCLAIM)]

def _flat(seq):
    out = []
    for x in seq:
        (out.extend if isinstance(x, list) else out.append)(x)
    return out


doc.build(_flat(e))
print("wrote 07 newcomer kit")
