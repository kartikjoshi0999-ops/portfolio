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
Q = lambda t: Paragraph(t, S["quote"])

doc = Doc(os.path.join(OUT, "08-Finance-and-Banking-Interview-Prep-Pack.pdf"),
          "Finance & Banking Interview Prep Pack", "prep")
e = cover_page(
    "Finance &amp; Banking<br/>Interview Prep Pack",
    "120 questions, 22 worked model answers, and the framework behind them",
    "Written by a Financial Analyst and Personal Banker who has sat on both sides of the table —<br/>"
    "at BMO in Canada and Deutsche Bank in India.",
    ["40 behavioural · 22 core finance · 20 AML, KYC and FINTRAC · 18 credit · 20 payments and operations",
     "STAR answer builder · Questions to ask · 30-60-90 plan · Follow-up templates"])

e += [H1("How to use this pack"),
      P("Interviews for finance and banking roles are more predictable than candidates expect. The same "
        "twenty behavioural themes and the same forty technical concepts come up again and again, because "
        "hiring managers are testing for the same things: can you be trusted with money, can you follow a "
        "control, and can you explain a number to someone who is not an analyst."),
      P("Work through it in this order:"),
      numbered(["Read section 1 and write out six STAR stories. This is 80% of the work and the part people skip.",
                "Skim the technical section for your role and mark anything you cannot explain out loud in 60 seconds.",
                "Rehearse those out loud. Not in your head — out loud, timed.",
                "The night before, read only your six stories and your questions to ask.",
                "After the interview, send the follow-up from section 9 within 24 hours."]),
      box("The rule that matters most", [
          "In finance interviews, the wrong answer delivered with a clear structure beats the right answer "
          "delivered as a ramble. Structure signals how you will handle a client, a regulator, or an auditor. "
          "Every framework in this pack exists to give you structure under pressure."]),
      SM(LICENCE), SM(DISCLAIM), PageBreak(),

      H1("1 · The STAR method, properly"),
      P("STAR is not a formula for sounding rehearsed. It is a way to stop yourself from telling a five-minute "
        "story with no point. Keep each answer to 90 seconds — roughly 15 / 20 / 45 / 20 seconds per part."),
      table([["Part", "What goes in it", "The mistake to avoid"],
             ["<b>Situation</b>", "Two sentences of context: where, when, your role.", "Spending a minute on background nobody asked for."],
             ["<b>Task</b>", "What specifically was yours to solve.", "Describing what the team did instead of what you owned."],
             ["<b>Action</b>", "What <i>you</i> did, step by step, in the first person.", "Saying 'we' throughout so the interviewer cannot score you."],
             ["<b>Result</b>", "The outcome, quantified, plus what you changed afterwards.", "Ending with 'and it worked out well'."]],
            [0.9 * inch, 2.9 * inch, 2.8 * inch]),
      H2("The six stories to prepare"),
      P("Almost every behavioural question in banking maps to one of these six. Write them out once and you "
        "can answer forty questions from them."),
      numbered(["A time you caught an error or a risk that others had missed.",
                "A time you handled an angry or distressed client.",
                "A time you had to say no — to a client, or to a colleague who wanted a shortcut.",
                "A time you hit or missed a target, and what you did about it.",
                "A time you improved a process or automated something manual.",
                "A time you worked under a hard deadline with incomplete information."]),
      box("Quantify or it did not happen", [
          "Every result needs a number: dollars, percentage, hours saved, error rate, queue size, client count, "
          "SLA. If you do not have exact figures, use an honest estimate and say it is an estimate — "
          "'roughly a quarter of the queue, about 60 items a day'. Never invent precision."]),
      PageBreak(),

      H1("2 · Behavioural questions"),
      P("Forty questions, grouped by what they are actually testing. Mark the ones your six stories do not cover."),
      H2("Reliability and integrity"),
      bullets(["Tell me about a time you made a mistake with financial data. What happened next?",
               "Describe a situation where you were asked to do something you thought was wrong.",
               "Have you ever had to report a colleague's error? How did you handle it?",
               "Tell me about a time you were trusted with confidential information.",
               "When did you last miss a deadline, and what did you change afterwards?",
               "Describe a time you found a discrepancy nobody else had noticed.",
               "Tell me about a control you follow even when it slows you down.",
               "How do you handle it when a client asks you to bend a rule slightly?"]),
      H2("Client handling"),
      bullets(["Tell me about the most difficult client you have dealt with.",
               "Describe a time you had to explain something technical to someone with no financial background.",
               "How did you handle a client who was refused a product or a loan?",
               "Tell me about a time you turned an unhappy client into a satisfied one.",
               "Describe a time you identified a need the client had not asked about.",
               "How do you build trust with a client in the first five minutes?",
               "Tell me about a time you had to deliver bad news about someone's money.",
               "Describe a time you dealt with a vulnerable or elderly client."]),
      H2("Pressure, volume and accuracy"),
      bullets(["How do you prioritise when everything on your desk is urgent?",
               "Tell me about your highest-volume day. How did you keep quality up?",
               "Describe a time you worked with incomplete information under a deadline.",
               "How do you check your own work? Walk me through your actual process.",
               "Tell me about a time a system went down mid-process.",
               "Describe a month-end or quarter-end close that went badly.",
               "How do you handle interruptions when you are doing detailed reconciliation work?",
               "Tell me about a time you had to redo work because of an upstream error."]),
      H2("Teamwork and initiative"),
      bullets(["Tell me about a time you disagreed with your manager.",
               "Describe a process you improved without being asked.",
               "How have you helped a new team member get up to speed?",
               "Tell me about a time you had to influence someone with no authority over them.",
               "Describe a cross-functional project you worked on.",
               "When have you taken on work outside your job description?",
               "Tell me about feedback that was hard to hear.",
               "How do you handle a teammate who is not pulling their weight?"]),
      H2("Motivation and fit"),
      bullets(["Why banking? Why this bank specifically?",
               "Why are you leaving your current role?",
               "Where do you want to be in three years?",
               "What is the most interesting thing you have read about this industry recently?",
               "What part of this job do you expect to dislike?",
               "Tell me about a professional goal you set and did not reach.",
               "How do you keep current with regulation and product changes?",
               "What would your last manager say is your biggest weakness?"]),
      PageBreak(),

      H1("3 · Technical — core finance"),
      P("Twenty-two questions across the four technical sections carry a full worked answer. Each is "
        "deliberately short: say this much, then stop and let them ask a follow-up. Over-explaining is the "
        "most common way candidates talk themselves into trouble. Every section then lists the rest of the "
        "questions that come up, for you to rehearse in your own words."),
      H3("Walk me through the three financial statements and how they link."),
      Q("The income statement shows profitability over a period. The balance sheet is a snapshot of assets, "
        "liabilities and equity at a point in time. The cash flow statement reconciles profit to actual cash. "
        "They link in two places: net income flows into retained earnings on the balance sheet and starts the "
        "cash flow statement, and the closing cash on the cash flow statement is the cash line on the balance "
        "sheet. That second link is why the balance sheet balancing is a genuine check on the model."),
      H3("If depreciation increases by $10, what happens across all three statements?"),
      Q("Assume a 25% tax rate. Income statement: EBIT falls $10, tax falls $2.50, net income falls $7.50. "
        "Cash flow: start at net income down $7.50, add back the $10 non-cash depreciation, so cash rises "
        "$2.50. Balance sheet: cash up $2.50, net PP&amp;E down $10, so assets fall $7.50; retained earnings "
        "fall $7.50. It balances."),
      H3("What is working capital and why does an analyst care?"),
      Q("Current assets less current liabilities — in practice, receivables plus inventory less payables. "
        "Growth consumes cash through working capital: a business can be profitable and still fail because "
        "its cash is tied up in receivables and stock. That is why we forecast it with DSO, DIO and DPO "
        "rather than as a percentage of revenue."),
      H3("NPV or IRR — which do you trust, and why?"),
      Q("NPV. It is stated in dollars of value created and it uses your actual cost of capital. IRR assumes "
        "interim cash flows are reinvested at the IRR itself, which is usually unrealistic, and it can produce "
        "multiple answers when cash flows change sign. I use IRR as a communication tool because executives "
        "like a percentage, but the decision goes to NPV."),
      H3("Explain WACC in one breath."),
      Q("The blended cost of the money a company uses: the cost of equity and the after-tax cost of debt, "
        "each weighted by its share of the capital structure. It is the discount rate for unlevered free cash "
        "flow, because those cash flows belong to both debt and equity holders."),
      H3("How would you value a small business?"),
      Q("Three approaches, then triangulate. A DCF for the intrinsic view. Comparable company multiples — "
        "EV/EBITDA is the usual starting point for a private business. Precedent transactions if there are "
        "any. For a small business I would also normalise owner compensation and strip out personal expenses "
        "before I trusted the EBITDA figure at all."),
      H3("What is the difference between EBITDA and cash flow?"),
      Q("EBITDA ignores three real cash costs: interest, tax, and the working capital and capital expenditure "
        "the business needs to keep running. It is a useful comparison metric across capital structures, not "
        "a cash figure. A capital-intensive business with strong EBITDA can be free-cash-flow negative for years."),
      PageBreak(),

      H2("More questions to be ready for"),
      bullets(['What is the difference between accrual and cash accounting?', 'Why can a company be profitable and still run out of cash?', 'What is deferred revenue, and where does it sit on the balance sheet?', 'How does a share buyback affect all three statements?', 'What is goodwill, and when is it impaired?', 'Explain operating leverage, and who it hurts in a downturn.', 'What is the difference between enterprise value and equity value?', 'Why do we discount unlevered free cash flow rather than net income?', 'What is a terminal value, and how would you sanity-check one?', 'What is the difference between FIFO and weighted-average inventory costing?', 'How would you build a revenue forecast for a business with no history?', 'What is a sensitivity analysis, and which two variables would you flex first?', 'What does a negative working capital balance tell you about a business?', 'How would you assess whether a company can afford its dividend?', 'How is amortisation of an intangible different from depreciation?']),
      H1("4 · Technical — AML, KYC and FINTRAC"),
      P("For any Canadian banking role, expect at least three compliance questions. Getting these right marks "
        "you as someone who can be put in front of clients without supervision."),
      H3("What is KYC and why does it exist?"),
      Q("Know Your Client — verifying who the client is, understanding the purpose of the account, and "
        "understanding the source of their funds. It exists so criminal proceeds cannot be placed into the "
        "financial system anonymously, and so the institution can spot when activity stops matching the "
        "client's stated profile."),
      H3("What is FINTRAC and what does it require of you at the front line?"),
      Q("Canada's financial intelligence unit. At the front line it means verifying identity to prescribed "
        "methods, keeping records, and submitting reports — large cash transaction reports at the $10,000 "
        "threshold including the 24-hour aggregation rule, electronic funds transfer reports, terrorist "
        "property reports, and suspicious transaction reports. The suspicious transaction report is the one "
        "with no dollar threshold at all: it is based on reasonable grounds to suspect."),
      H3("A long-standing client suddenly deposits $9,500 in cash three days in a row. What do you do?"),
      Q("Three things, in order. First, I do not tell the client what the reporting thresholds are — that "
        "would be tipping off. Second, I complete the transactions normally if they are legitimate on their "
        "face, and I apply the 24-hour aggregation rule, which may make these reportable regardless of the "
        "individual amounts. Third, I escalate to my AML officer with a factual, non-judgemental note of what "
        "I observed. Structuring is exactly this pattern, and the decision to file an STR is not mine to make "
        "alone — my job is to observe accurately and escalate promptly."),
      H3("What is a politically exposed person, and what changes if you have one?"),
      Q("Someone who holds or has held a prominent public office, plus their close associates and family. "
        "They are not prohibited clients — they simply carry higher risk of bribery and corruption proceeds. "
        "It triggers enhanced due diligence: senior management approval, establishing source of wealth as well "
        "as source of funds, and ongoing enhanced monitoring."),
      H3("Explain the three stages of money laundering."),
      Q("Placement — getting cash into the system. Layering — moving it through transactions and jurisdictions "
        "to break the audit trail. Integration — bringing it back as apparently legitimate wealth. Front-line "
        "banking is where placement is most visible, which is why cash controls sit where they do."),
      H3("What is the difference between source of funds and source of wealth?"),
      Q("Source of funds is where this specific money came from — the sale of a property, a bonus. Source of "
        "wealth is how the client accumulated their overall net worth. Standard due diligence asks the first; "
        "enhanced due diligence asks the second."),
      PageBreak(),

      H2("More questions to be ready for"),
      bullets(['What is the difference between customer due diligence and enhanced due diligence?', 'What is a beneficial owner, and what ownership threshold triggers identification?', 'Give me three red flags in a personal chequing account that you would escalate.', 'What is smurfing, and how would it show up in a branch?', 'What is a nominee account, and why is it higher risk?', 'How long must client identification and transaction records be kept?', 'What is a third-party determination, and when do you have to make one?', 'What is the difference between a suspicious transaction and a suspicious attempted transaction?', 'What happens when a client name matches a sanctions list?', 'What is trade-based money laundering, in one sentence?', 'Why are cash-intensive businesses treated as higher risk?', 'What would make you re-assess the risk rating of an existing client?', 'What is tipping off, and why is it an offence rather than a policy breach?', 'How do you verify identity for a client who never comes into a branch?']),
      H1("5 · Technical — credit and retail banking"),
      H3("Walk me through the five Cs of credit."),
      Q("Character — the client's repayment history and credit behaviour. Capacity — can the cash flow service "
        "the debt, measured by the service ratios. Capital — the client's own money in the deal. Collateral — "
        "what secures it and what it is worth in a forced sale. Conditions — the purpose of the loan and the "
        "economic environment. Capacity carries the most weight; collateral is a fallback, not a reason to lend."),
      H3("What are GDS and TDS and roughly where do the limits sit?"),
      Q("Gross debt service is housing costs — mortgage payment, property tax, heat and half of condo fees — "
        "over gross income. Total debt service adds all other debt obligations. Conventional guidance is "
        "around 32% and 40%, with insured mortgage limits commonly applied at 39% and 44%. The exact cut-offs "
        "vary by lender and product, so I would confirm the current policy rather than quote it from memory."),
      H3("A client is declined. How do you handle the conversation?"),
      Q("Tell them clearly and without hedging, explain what drove the decision in terms they can act on, and "
        "give them a concrete path — reduce the utilisation on this card, wait for these two payments to "
        "report, come back in six months. I never blame 'the system'. A decline handled well keeps the "
        "relationship and frequently produces a referral; a decline handled badly loses the household."),
      H3("What is the difference between a secured and unsecured line of credit?"),
      Q("A secured line is backed by an asset, usually home equity, so the rate is materially lower and the "
        "limit higher, but default risk transfers to the asset. An unsecured line prices the risk into the "
        "rate. For a client consolidating high-interest debt, the secured option saves the most money — "
        "provided they understand they have moved consumer debt onto their home."),
      H3("A client wants to put their whole emergency fund into a mutual fund for better returns. What do you say?"),
      Q("I would slow that conversation down and go back to purpose and time horizon. An emergency fund is "
        "there to be available at short notice without capital loss — that is a high-interest savings account "
        "or a cashable GIC, not a market investment. I would look at whether the fund is oversized relative to "
        "their expenses, and invest only the surplus, matched to their risk tolerance and KYC profile. "
        "Recommending otherwise would fail suitability."),
      PageBreak(),

      H2("More questions to be ready for"),
      bullets(['What is the difference between a hard and a soft credit enquiry?', 'A client has a credit score of 680. What does that tell you, and what does it not?', 'What is loan-to-value, and why does it drive pricing?', 'Explain the difference between the amortisation and the term on a Canadian mortgage.', 'What is the mortgage stress test rate, and what problem does it exist to solve?', 'What is the difference between a HELOC and a second mortgage?', 'How do you assess income for a self-employed applicant?', 'What is a covenant, and what happens when one is breached?', 'In a default, what actually changes between secured and unsecured lending?', 'A client wants to roll consumer debt into their mortgage. What do you walk them through?', 'What is Know Your Product, and how is it different from Know Your Client?', 'What makes an investment recommendation unsuitable, even when the client asks for it?', 'How does a GIC ladder work, and which client does it suit?']),
      H1("6 · Technical — payments, operations and controls"),
      H3("What is a reconciliation, and what do you do when it does not balance?"),
      Q("Comparing two independent records of the same activity and explaining every difference. When it does "
        "not balance I work by elimination: check the date cut-off first, then look for a difference divisible "
        "by nine, which indicates a transposition, then look for an amount equal to exactly half the variance, "
        "which indicates a sign error. Only then do I go transaction by transaction. Every unexplained item "
        "gets aged and escalated rather than written off."),
      H3("What controls stop a payment from going to the wrong place?"),
      Q("Maker-checker segregation, so the person who inputs is never the person who releases. Standing "
        "settlement instructions held independently of the payment request. Callback verification on any "
        "change of bank details. Four-eyes approval above a threshold. Sanctions screening before release. "
        "The change-of-details callback is the control that stops most business email compromise fraud."),
      H3("What is an SLA and how do you protect one on a heavy day?"),
      Q("A service level agreement — the agreed turnaround for a queue, usually cut-off driven in payments. "
        "On a heavy day I sequence by cut-off time rather than by arrival, escalate the items that cannot make "
        "their window early rather than at the deadline, and flag the breach risk to the client-facing team "
        "before it becomes a complaint. Missing an SLA is recoverable; missing it silently is not."),
      H3("Why does end-of-day matter so much in banking operations?"),
      Q("Because the day's position has to be final and reconciled before the next day's processing opens. An "
        "unresolved break at EOD compounds: it distorts the next day's balances, delays settlement, and by "
        "the time it surfaces the audit trail is three days deep. That is why EOD is a hard control point, "
        "not a housekeeping task."),
      PageBreak(),

      H2("More questions to be ready for"),
      bullets(['What is an MT103, and what does it carry?', 'What is an IBAN, and where is it required?', 'What is a value date, and why does it matter to the client?', 'What is the difference between a nostro and a vostro account?', 'What is straight-through processing, and what breaks it?', 'What causes a payment repair, and how would you reduce the repair rate?', 'What is the difference between a recall and a return?', 'What is a chargeback, and who carries the loss?', 'What is the difference between an EFT and a wire?', 'What happens to a payment that arrives after the cut-off time?', 'What is a suspense account, and why must it be cleared?', 'What is an aged item, and at what point do you escalate one?', 'What is dual control, and where would you insist on it?', 'What is a break in a nostro reconciliation?', 'A batch failed to release. What do you check first, second, third?', 'What is business continuity, and what would your role be in an outage?']),
      H1("7 · Questions to ask them"),
      P("Ask three or four. Never ask a question whose answer is on the first page of their website, and never "
        "lead with salary or holidays."),
      H2("Strong questions"),
      bullets(["What does someone need to have accomplished in their first six months for you to consider the "
               "hire a success?",
               "How is performance actually measured in this role — which numbers do you look at weekly?",
               "What is the hardest part of this job that does not show up in the job description?",
               "How does this team work with compliance and risk day to day?",
               "What has changed in the last year that made this role necessary?",
               "Where do people who do well in this seat tend to move next?",
               "How would you describe the difference between someone who is good at this job and someone who "
               "is exceptional at it?"]),
      H2("Questions that cost you the offer"),
      bullets(["Anything about salary, bonus or holidays before an offer conversation is opened by them.",
               "'What does your company do?' — this reads as no preparation.",
               "'Did I get the job?' — it puts the interviewer in an awkward position.",
               "Anything that suggests you plan to leave quickly."]),

      H1("8 · Your first 30-60-90 days"),
      P("Bring this. Print it on one page and hand it over at the end of a final-round interview — very few "
        "candidates do, and it changes the tone of the conversation immediately."),
      table([["Period", "Focus", "What you would deliver"],
             ["Days 1–30", "Learn the systems, the controls and the people.",
              "Complete all mandatory training and compliance certification. Shadow the top performer. Map the end-to-end process for my own queue. Know every product's key features and fees."],
             ["Days 31–60", "Carry the standard workload independently.",
              "Handle my full volume without escalation on routine items. Build my own checking routine. Identify one manual step worth automating and propose it."],
             ["Days 61–90", "Contribute beyond the role.",
              "Hit the standard targets for the seat. Deliver the process improvement identified in month two. Take on one piece of work my manager is currently doing themselves."]],
            [0.9 * inch, 1.8 * inch, 3.9 * inch]),
      PageBreak(),

      H1("9 · After the interview"),
      H2("The follow-up email — send within 24 hours"),
      box("Template", [
          "<i>Subject: Thank you — [Role] interview</i>",
          "Hello [Name],",
          "Thank you for your time today. I enjoyed the conversation, particularly [specific thing they said, "
          "not a generic compliment].",
          "One thing I want to add: when you asked about [topic], I described [X]. On reflection the clearest "
          "example is [better, quantified example in two sentences].",
          "The role fits what I do well — [one line tying your strongest evidence to their stated priority]. "
          "I would be glad to go further in the process, and I am happy to provide references at any point.",
          "Best regards,<br/>[Your name] · [phone]"]),
      P("The middle paragraph is what makes this work. Everyone sends thanks; almost nobody uses the follow-up "
        "to repair the one answer they fumbled. It is a second attempt at the question, and interviewers "
        "consistently respond to it."),
      H2("If they go quiet"),
      bullets(["Wait until one business day after the date they gave you. If they gave no date, wait five "
               "business days.",
               "Send one short note to the recruiter, not to the whole panel.",
               "Ask a single clear question: is there an updated timeline you can share?",
               "One follow-up, then leave it. Chasing weekly reads as desperation and it travels."]),
      H2("Talking about salary"),
      bullets(["Let them raise it. If pressed for a number early, give a researched range and say it depends "
               "on the whole package.",
               "Know the three numbers before you walk in: what you would be delighted with, what you would "
               "accept, and what you would decline.",
               "Negotiate the package, not just base — signing bonus, review timing, vacation, education "
               "funding and certification support are all real money.",
               "Once you accept, accept graciously and stop negotiating. Reputation in banking is small-town."]),
      Spacer(1, 0.15 * inch),
      SM("Written by Kartik Joshi, MBA — Financial Analyst and Banking Professional, Cornwall, Ontario. "
         "Experience across BMO retail banking, Deutsche Bank payments and audit, and AML/KYC/FINTRAC "
         "compliance in Canada and India. Questions? Message me through Etsy."),
      SM(LICENCE), SM(DISCLAIM)]

def _flat(seq):
    out = []
    for x in seq:
        (out.extend if isinstance(x, list) else out.append)(x)
    return out


doc.build(_flat(e))
print("wrote 08 interview pack")
