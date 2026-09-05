# -*- coding: utf-8 -*-
"""Generate shop.html for the portfolio site, straight from the product catalog."""
import os, html, catalog

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
E = html.escape

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
:root{--navy:#0A1628;--mid:#0D1F3C;--gold:#C9A84C;--amber:#F5A623;--teal:#00B4A6;
 --coral:#E8635A;--lav:#9B89D4;--green:#2ECC71;--text:#E8E4DA;--muted:#8A97AB;
 --card:rgba(255,255,255,0.04);--cb:rgba(255,255,255,0.08)}
body{font-family:'DM Sans',sans-serif;background:var(--navy);color:var(--text);line-height:1.6;overflow-x:hidden}
a{color:inherit}
nav{position:fixed;top:0;left:0;right:0;z-index:500;padding:0 48px;height:64px;display:flex;
 align-items:center;justify-content:space-between;background:rgba(10,22,40,.92);
 backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.07)}
.nbrand{font-family:'Playfair Display',serif;font-size:1.1rem;color:var(--gold);text-decoration:none}
.nlinks{display:flex;gap:22px;list-style:none}
.nlinks a{color:var(--muted);font-size:.74rem;font-weight:500;letter-spacing:.12em;
 text-transform:uppercase;text-decoration:none;transition:color .2s}
.nlinks a:hover{color:var(--gold)}
section{padding:84px 80px}
.wrap{max-width:1180px;margin:0 auto}
.slabel{font-family:'DM Mono',monospace;font-size:.68rem;color:var(--teal);letter-spacing:.25em;
 text-transform:uppercase;margin-bottom:10px}
.stitle{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:700;margin-bottom:14px}
.divl{width:56px;height:3px;background:linear-gradient(90deg,var(--gold),var(--teal));margin-bottom:30px;border-radius:2px}
.lede{color:var(--muted);max-width:720px;font-weight:300;margin-bottom:8px}
/* HERO */
.shero{min-height:78vh;display:flex;align-items:center;padding:130px 80px 70px;position:relative;overflow:hidden}
.shero .hbg{position:absolute;inset:0;background:
 radial-gradient(ellipse 70% 60% at 75% 25%,rgba(0,180,166,.12) 0%,transparent 60%),
 radial-gradient(ellipse 50% 70% at 5% 85%,rgba(201,168,76,.09) 0%,transparent 55%)}
.shero .hgrid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.02) 1px,transparent 1px),
 linear-gradient(90deg,rgba(255,255,255,.02) 1px,transparent 1px);background-size:64px 64px;
 -webkit-mask-image:radial-gradient(ellipse at center,black 20%,transparent 75%);
 mask-image:radial-gradient(ellipse at center,black 20%,transparent 75%)}
.sh-in{position:relative;z-index:2;max-width:820px}
.sh-mono{font-family:'DM Mono',monospace;font-size:.7rem;color:var(--teal);letter-spacing:.22em;
 text-transform:uppercase;margin-bottom:18px}
.sh-title{font-family:'Playfair Display',serif;font-size:clamp(2.6rem,6vw,4.6rem);font-weight:900;
 line-height:1.05;margin-bottom:24px}
.sh-title .acc{color:var(--gold)}
.sh-sub{font-size:1.02rem;color:var(--muted);font-weight:300;max-width:640px;margin-bottom:30px;line-height:1.75}
.badges{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:34px}
.badge{padding:5px 14px;border-radius:100px;font-size:.72rem;font-weight:500;border:1px solid;
 color:var(--teal);border-color:rgba(0,180,166,.35);background:rgba(0,180,166,.07)}
.btns{display:flex;gap:14px;flex-wrap:wrap}
.bgold{padding:13px 30px;background:linear-gradient(135deg,var(--gold),var(--amber));color:var(--navy);
 border:none;border-radius:8px;font-weight:700;font-size:.85rem;cursor:pointer;letter-spacing:.04em;
 transition:all .2s;text-decoration:none;display:inline-block}
.bgold:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(201,168,76,.3)}
.bghost{padding:13px 30px;background:transparent;color:var(--text);border:1px solid rgba(255,255,255,.14);
 border-radius:8px;font-weight:500;font-size:.85rem;transition:all .2s;text-decoration:none;display:inline-block}
.bghost:hover{border-color:var(--gold);color:var(--gold)}
/* BUNDLE */
.bundle{background:linear-gradient(135deg,rgba(201,168,76,.1),rgba(0,180,166,.06));
 border:1px solid rgba(201,168,76,.3);border-radius:18px;padding:38px;display:grid;
 grid-template-columns:1.15fr .85fr;gap:38px;align-items:center}
.bundle img{width:100%;border-radius:12px;border:1px solid var(--cb);display:block}
.bflag{display:inline-block;font-family:'DM Mono',monospace;font-size:.66rem;color:var(--gold);
 letter-spacing:.14em;border:1px solid rgba(201,168,76,.4);background:rgba(201,168,76,.1);
 border-radius:4px;padding:3px 10px;margin-bottom:14px}
.bname{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:700;margin-bottom:12px}
.bprice{display:flex;align-items:baseline;gap:12px;margin:18px 0 20px}
.bprice .now{font-family:'Playfair Display',serif;font-size:2.4rem;color:var(--gold);font-weight:700}
.bprice .was{color:var(--muted);text-decoration:line-through;font-size:1rem}
.bprice .off{color:var(--green);font-size:.8rem;border:1px solid rgba(46,204,113,.3);
 background:rgba(46,204,113,.08);border-radius:4px;padding:2px 8px}
/* GRID */
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:26px}
.pcard{background:var(--card);border:1px solid var(--cb);border-radius:14px;overflow:hidden;
 display:flex;flex-direction:column;transition:transform .2s,border-color .2s}
.pcard:hover{transform:translateY(-4px);border-color:rgba(201,168,76,.35)}
.pcard img{width:100%;aspect-ratio:1/1;object-fit:cover;object-position:top;display:block;
 border-bottom:1px solid var(--cb)}
.pbody{padding:22px 24px 24px;display:flex;flex-direction:column;flex:1}
.pkind{font-family:'DM Mono',monospace;font-size:.63rem;color:var(--teal);letter-spacing:.16em;
 text-transform:uppercase;margin-bottom:8px}
.pname{font-family:'Playfair Display',serif;font-size:1.22rem;font-weight:700;margin-bottom:10px;line-height:1.3}
.pdesc{font-size:.85rem;color:var(--muted);font-weight:300;margin-bottom:14px;line-height:1.65}
.plist{list-style:none;margin-bottom:18px}
.plist li{font-size:.79rem;color:#B9C3D2;padding-left:18px;position:relative;margin-bottom:6px;line-height:1.5}
.plist li::before{content:'✓';position:absolute;left:0;color:var(--teal);font-size:.75rem}
.prow{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:14px;
 padding-top:16px;border-top:1px solid var(--cb)}
.price{font-family:'Playfair Display',serif;font-size:1.5rem;color:var(--gold);font-weight:700}
.price small{font-size:.65rem;color:var(--muted);font-family:'DM Sans',sans-serif;margin-left:5px}
.buy{padding:10px 20px;background:linear-gradient(135deg,var(--gold),var(--amber));color:var(--navy);
 border-radius:7px;font-weight:700;font-size:.78rem;text-decoration:none;white-space:nowrap;transition:all .2s}
.buy:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(201,168,76,.28)}
/* STEPS + FAQ */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px}
.step{background:var(--card);border:1px solid var(--cb);border-radius:12px;padding:26px}
.snum{font-family:'Playfair Display',serif;font-size:2rem;color:var(--gold);line-height:1;margin-bottom:12px}
.stt{font-weight:600;margin-bottom:8px}
.sdd{font-size:.85rem;color:var(--muted);font-weight:300;line-height:1.65}
.faq{border-bottom:1px solid var(--cb);padding:20px 0}
.faq h4{font-size:.95rem;margin-bottom:8px;color:var(--gold);font-weight:600}
.faq p{font-size:.87rem;color:var(--muted);font-weight:300;line-height:1.7}
footer{padding:44px 80px;border-top:1px solid var(--cb);text-align:center;color:var(--muted);font-size:.78rem}
.note{margin-top:26px;font-size:.78rem;color:var(--muted);font-weight:300;max-width:760px;line-height:1.7;
 border-left:2px solid rgba(201,168,76,.4);padding-left:16px}
@media(max-width:900px){
 section,.shero{padding-left:26px;padding-right:26px}
 nav{padding:0 22px}.nlinks{display:none}
 .bundle{grid-template-columns:1fr;padding:26px}
 footer{padding:34px 26px}
}
"""


def card(p):
    hi = "".join("<li>%s</li>" % E(h) for h in p["highlights"][:4])
    kind = {"xlsx": "Excel template · instant download",
            "pdf": "PDF guide · instant download"}.get(p["kind"], "Digital download")
    return f"""      <article class="pcard">
        <img src="shop/dist/images/{p['slug']}/1-main.png" alt="{E(p['name'])} — listing preview" loading="lazy">
        <div class="pbody">
          <div class="pkind">{kind}</div>
          <h3 class="pname">{E(p['name'])}</h3>
          <p class="pdesc">{E(p['desc_open'])}</p>
          <ul class="plist">{hi}</ul>
          <div class="prow">
            <div class="price">${p['price']:.2f}<small>CAD</small></div>
            <a class="buy" data-listing="{p['slug']}" href="#" target="_blank" rel="noopener">View on Etsy →</a>
          </div>
        </div>
      </article>"""


def build():
    b = catalog.ALL[-1]
    full = sum(p["price"] for p in catalog.PRODUCTS)
    cards = "\n".join(card(p) for p in catalog.PRODUCTS)
    faqs = [
        ("Will these work in Google Sheets?",
         "Yes. Upload the .xlsx to Google Drive and open it with Google Sheets — every formula carries "
         "over. Drop-down lists may need re-applying and chart styling can shift slightly, but the "
         "calculations are unaffected."),
        ("Do I need to be good at Excel?",
         "No. Every file opens on a Start Here tab that tells you exactly what to do, and the cells are "
         "colour-coded: yellow means type here, grey means a formula lives there. If you can type a "
         "number into a box, you can use these."),
        ("Is this a subscription?",
         "No. You buy the file once and it is yours — nothing to log in to, nothing to renew, and it "
         "works offline."),
        ("Can I use these for my business?",
         "Yes. The licence covers your own personal or business use, including editing. What it does not "
         "cover is reselling, sharing, or including the file in a product of your own."),
        ("Are the Canadian figures current?",
         "TFSA limits run from 2009 through 2026 and RRSP dollar limits through 2026, with a note on each "
         "tab telling you to confirm the current year with the CRA. Limits are indexed annually, so the "
         "file points you at the authoritative source rather than pretending it never goes stale."),
        ("Is any of this financial advice?",
         "No. These are educational planning tools built by a finance professional. They are not "
         "financial, tax, investment or legal advice, and buying one does not create an advisor "
         "relationship. Check anything you plan to act on with the CRA or a licensed advisor."),
    ]
    faq_html = "\n".join(
        f'      <div class="faq"><h4>{E(q)}</h4><p>{E(a)}</p></div>' for q, a in faqs)
    steps = "\n".join(
        f"""        <div class="step"><div class="snum">{i}</div><div class="stt">{E(t)}</div>
        <div class="sdd">{E(s)}</div></div>"""
        for i, (t, s) in enumerate(
            [("Buy on Etsy", "Payment, delivery and buyer protection are all handled by Etsy. Nothing is shipped."),
             ("Download instantly", "Etsy emails a download link the moment payment clears, and the files sit in your Etsy account too."),
             ("Open and use it", "The formulas are already written. Type in the yellow cells and the rest calculates itself."),
             ("Keep it forever", "No subscription, no login, no expiry. Message me any time if you get stuck — I answer my own messages.")], 1))

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Joshi Finance Templates — Finance spreadsheets &amp; guides by Kartik Joshi</title>
<meta name="description" content="Canadian finance templates built by a banking professional: budget tracker, TFSA vs RRSP planner, debt payoff planner, portfolio tracker, business cash flow forecast and a linked 3-statement financial model.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<nav>
  <a class="nbrand" href="index.html">Kartik Joshi</a>
  <ul class="nlinks">
    <li><a href="index.html">Portfolio</a></li>
    <li><a href="#products">Products</a></li>
    <li><a href="#bundle">Bundle</a></li>
    <li><a href="#how">How it works</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="stats-app.html">StatLens</a></li>
  </ul>
</nav>

<header class="shero">
  <div class="hbg"></div><div class="hgrid"></div>
  <div class="sh-in">
    <div class="sh-mono">Joshi Finance Templates · Cornwall, Ontario</div>
    <h1 class="sh-title">Spreadsheets that<br><span class="acc">do the thinking</span></h1>
    <p class="sh-sub">Finance templates and guides built by a Canadian banking professional — retail
      banking at BMO, payments and audit at Deutsche Bank, and AML, KYC and FINTRAC compliance across
      two countries. Every file arrives with the formulas already written.</p>
    <div class="badges">
      <span class="badge">Instant download</span>
      <span class="badge">Excel &amp; PDF</span>
      <span class="badge">No subscription</span>
      <span class="badge">Canadian rules built in</span>
    </div>
    <div class="btns">
      <a class="bgold" id="shopCta" href="#products">Browse the shop</a>
      <a class="bghost" href="index.html">Back to portfolio</a>
    </div>
  </div>
</header>

<section id="bundle">
  <div class="wrap">
    <div class="slabel">Best value</div>
    <h2 class="stitle">Start with the bundle</h2>
    <div class="divl"></div>
    <div class="bundle">
      <div>
        <span class="bflag">SAVE {int(round((1 - b['price'] / full) * 100))}%</span>
        <div class="bname">{E(b['name'])}</div>
        <p class="pdesc">{E(b['desc_open'])}</p>
        <ul class="plist">{''.join('<li>%s</li>' % E(h) for h in b['highlights'])}</ul>
        <div class="bprice">
          <span class="now">${b['price']:.2f}</span>
          <span class="was">${full:.2f}</span>
          <span class="off">You save ${full - b['price']:.2f}</span>
        </div>
        <a class="bgold" data-listing="{b['slug']}" href="#" target="_blank" rel="noopener">Get the bundle on Etsy →</a>
      </div>
      <img src="shop/dist/images/{b['slug']}/1-main.png" alt="The Complete Finance Bundle">
    </div>
  </div>
</section>

<section id="products">
  <div class="wrap">
    <div class="slabel">The shop</div>
    <h2 class="stitle">Eight products</h2>
    <div class="divl"></div>
    <p class="lede">Six Excel templates and two written guides. Each one exists because I needed it
      first — for a client, for a forecast, or for my own first year in Canada.</p>
    <div style="height:30px"></div>
    <div class="pgrid">
{cards}
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="slabel">No shipping, no waiting</div>
    <h2 class="stitle">How it works</h2>
    <div class="divl"></div>
    <div class="steps">
{steps}
    </div>
    <p class="note"><strong>A word on what these are.</strong> Every template and guide here is an
      educational planning tool built by a finance professional. None of it is financial, tax,
      investment or legal advice, and buying one does not create an advisor relationship. Contribution
      limits and tax rules change — confirm current figures with the CRA or a licensed advisor before
      acting on anything a spreadsheet tells you.</p>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="slabel">Before you buy</div>
    <h2 class="stitle">Questions people ask</h2>
    <div class="divl"></div>
{faq_html}
  </div>
</section>

<footer>
  <div>© 2026 Kartik Joshi · Joshi Finance Templates · Cornwall, Ontario</div>
  <div style="margin-top:8px">
    <a href="index.html" style="color:var(--gold);text-decoration:none">Portfolio</a> ·
    <a href="mailto:kartikjoshi0999@gmail.com" style="color:var(--gold);text-decoration:none">kartikjoshi0999@gmail.com</a> ·
    <a href="https://www.linkedin.com/in/kartikjoshi09" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:none">LinkedIn</a>
  </div>
</footer>

<script>
/* ────────────────────────────────────────────────────────────────────────────
   ETSY LINKS — the only thing to edit on this page.

   1. Put your shop URL in SHOP_URL once the shop is open.
   2. As each listing goes live, paste its URL next to the matching key.
      Anything left empty falls back to the shop URL, so the page always works.
   ──────────────────────────────────────────────────────────────────────────── */
var SHOP_URL = "https://www.etsy.com/ca/shop/JoshiFinanceCo";
var LISTINGS = {{
{chr(10).join('  "%s": "",' % p['slug'] for p in catalog.ALL)}
}};

(function () {{
  var cta = document.getElementById("shopCta");
  if (SHOP_URL) {{ cta.href = SHOP_URL; cta.target = "_blank"; cta.rel = "noopener"; }}
  var links = document.querySelectorAll("[data-listing]");
  for (var i = 0; i < links.length; i++) {{
    var key = links[i].getAttribute("data-listing");
    links[i].href = (LISTINGS[key] && LISTINGS[key].length) ? LISTINGS[key] : SHOP_URL;
  }}
}})();
</script>
</body>
</html>
"""
    out = os.path.join(ROOT, "shop.html")
    open(out, "w").write(doc)
    print("wrote", out, len(doc), "bytes")


if __name__ == "__main__":
    build()


def index_section():
    """The Shop section injected into index.html between the SHOP markers."""
    b = catalog.ALL[-1]
    full = sum(p["price"] for p in catalog.PRODUCTS)
    feat = [catalog.PRODUCTS[i] for i in (0, 1, 5, 4)]
    cards = "\n".join(f"""      <div class="scard">
        <img src="shop/dist/images/{p['slug']}/1-main.png" alt="{E(p['name'])}" loading="lazy">
        <div class="sbody">
          <div class="skind">{'Excel template' if p['kind'] == 'xlsx' else 'PDF guide'} · instant download</div>
          <div class="sname">{E(p['name'])}</div>
          <p class="sdesc">{E(p['desc_open'][:150].rsplit(' ', 1)[0])}…</p>
          <div class="sfoot">
            <div class="sprice">${p['price']:.2f}<small>CAD</small></div>
            <a class="sbuy" href="shop.html#products">Details →</a>
          </div>
        </div>
      </div>""" for p in feat)
    return f"""<!-- SHOP:START -->
<section id="shop">
  <div class="slabel rev">Digital Products</div>
  <h2 class="stitle rev">The Shop</h2>
  <div class="divl rev"></div>
  <p class="ssub rev" style="max-width:820px">Finance templates and guides I built for my own work, then rebuilt properly so
    somebody else could use them. Six Excel templates and two written guides — budgeting, debt, TFSA and
    RRSP planning, portfolio tracking, business cash flow and a fully linked 3-statement financial model.
    Every file arrives with the formulas already written, and none of it needs a subscription.</p>
  <div class="shopgrid rev">
{cards}
  </div>
  <div class="shopbar rev">
    <div class="sbtxt"><b>All eight products together are ${b['price']:.2f}</b> — {int(round((1 - b['price'] / full) * 100))}% less than the
      ${full:.2f} they cost separately. Sold as instant digital downloads on Etsy.</div>
    <a class="bgold" href="shop.html" style="text-decoration:none">Open the shop →</a>
  </div>
</section>
<!-- SHOP:END -->"""


def inject_index():
    path = os.path.join(ROOT, "index.html")
    s = open(path).read()
    a, z = "<!-- SHOP:START -->", "<!-- SHOP:END -->"
    i, j = s.index(a), s.index(z) + len(z)
    s = s[:i] + index_section() + s[j:]
    open(path, "w").write(s)
    print("injected shop section into index.html")
