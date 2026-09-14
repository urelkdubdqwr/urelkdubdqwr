#!/usr/bin/env python3
"""ONAR-77 banner generator — 2000s preppy / editorial brutalism / Gen X.
usage: gen_banner.py OUTDIR TITLE SUBTITLE TAG [TAGS...]
emits header.svg (animated) + rule.svg
"""
import sys, html
from pathlib import Path

NAVY, CREAM, GOLD, INK, RED = "#1B2A4A", "#F4EFE4", "#C9A227", "#111318", "#B23A48"

TPL = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-label="{TITLE} — ONAR-77. {SUBTITLE}">
  <defs>
    <style><![CDATA[
      .paper {{ fill: {CREAM}; }}
      .hair  {{ stroke: {INK}; fill: none; }}
      .kicker {{ font-family: Georgia, "Times New Roman", serif; font-style: italic;
                font-size: 20px; letter-spacing: 1px; fill: {NAVY}; }}
      .title {{ font-family: "Arial Black", "Helvetica Neue", Impact, sans-serif;
                font-weight: 900; font-size: 92px; letter-spacing: -4px; fill: {INK}; }}
      .sub   {{ font-family: Georgia, serif; font-size: 21px; fill: #3a3d44; }}
      .mono  {{ font-family: ui-monospace, Menlo, monospace; font-size: 13px;
                letter-spacing: 2px; fill: {NAVY}; }}
      .stamp {{ font-family: "Arial Black", Impact, sans-serif; font-size: 17px;
                letter-spacing: 3px; fill: none; stroke: {RED}; stroke-width: 1.4; }}
      .ticker{{ font-family: ui-monospace, Menlo, monospace; font-size: 15px;
                letter-spacing: 2px; fill: {GOLD}; }}
      /* — animations (CSS keyframes run inside GitHub's img render) — */
      @keyframes blink {{ 0%,49% {{opacity:1}} 50%,100% {{opacity:0}} }}
      @keyframes rise  {{ 0%,100% {{transform:translateY(0)}} 50% {{transform:translateY(-14px)}} }}
      @keyframes flapL {{ 0%,100% {{transform:rotate(0deg)}} 50% {{transform:rotate(-16deg)}} }}
      @keyframes flapR {{ 0%,100% {{transform:rotate(0deg)}} 50% {{transform:rotate(16deg)}} }}
      @keyframes scroll {{ 0% {{transform:translateX(0)}} 100% {{transform:translateX(-{{STEP}}px)}} }}
      @keyframes wig   {{ 0%,100% {{transform:rotate(-2deg)}} 50% {{transform:rotate(2deg)}} }}
      @keyframes draw  {{ to {{stroke-dashoffset: 0;}} }}
      .cursor {{ animation: blink 1.1s steps(1) infinite; }}
      .phoenix {{ transform-origin: 1050px 118px; animation: rise 3.2s ease-in-out infinite; }}
      .wL {{ transform-origin: 1044px 118px; animation: flapL 1.6s ease-in-out infinite; }}
      .wR {{ transform-origin: 1056px 118px; animation: flapR 1.6s ease-in-out infinite; }}
      .tape  {{ animation: scroll 12s linear infinite; }}
      .scorp {{ stroke-dasharray: 220; stroke-dashoffset: 220;
               animation: draw 4s ease-out 0.4s forwards; }}
      .coin  {{ transform-box: fill-box; transform-origin: center; animation: wig 2.4s ease-in-out infinite; }}
      .coin2 {{ animation-delay: .6s; }} .coin3 {{ animation-delay: 1.2s; }}
    ]]></style>
    <pattern id="argyle" width="48" height="48" patternUnits="userSpaceOnUse">
      <rect width="48" height="48" fill="{NAVY}"/>
      <path d="M24 0 L48 24 L24 48 L0 24 Z" fill="none" stroke="{GOLD}" stroke-width="1" opacity=".55"/>
      <path d="M0 0 L48 48 M48 0 L0 48" stroke="{CREAM}" stroke-width=".6" opacity=".18"/>
    </pattern>
    <clipPath id="tapeclip"><rect x="0" y="352" width="1200" height="48"/></clipPath>
  </defs>

  <!-- editorial page -->
  <rect width="1200" height="400" class="paper"/>
  <rect x="10" y="10" width="1180" height="380" class="hair" stroke-width="6"/>
  <rect x="20" y="20" width="1160" height="360" class="hair" stroke-width="1.5"/>

  <!-- preppy argyle sidebar -->
  <rect x="20" y="20" width="64" height="332" fill="url(#argyle)"/>
  <text x="52" y="196" transform="rotate(-90 52 196)" text-anchor="middle"
        class="mono" style="fill:{CREAM}">NO. 77 — EST. MMXXVI</text>

  <!-- masthead -->
  <text x="116" y="72" class="kicker">The {TITLE} Journal · edisi harian, terbit sambil tidur</text>
  <line x1="116" y1="86" x2="1160" y2="86" class="hair" stroke-width="2"/>
  <line x1="116" y1="92" x2="1160" y2="92" class="hair" stroke-width="1"/>

  <text x="110" y="188" class="title">{TITLE_SVG}</text>

  <!-- headline rules + subtitle (editorial) -->
  <line x1="116" y1="216" x2="880" y2="216" class="hair" stroke-width="6"/>
  <text x="116" y="252" class="sub">{SUBTITLE}</text>
  <text x="116" y="280" class="mono">ONAR-77 · SCORPIO ✕ EAGLE ✕ PHOENIX · WEB3 · MONEY MONEY MONEY<tspan class="cursor">▮</tspan></text>

  <!-- Gen X rotated stamp -->
  <g transform="rotate(-8 1010 250)">
    <rect x="936" y="226" width="224" height="42" fill="none" stroke="{RED}" stroke-width="2.5"/>
    <text x="1048" y="254" text-anchor="middle" class="stamp">RECEIPTS INCLUDED</text>
  </g>

  <!-- phoenix rising, flapping (line art, brutalist) -->
  <g class="phoenix">
    <g class="wL"><path d="M1044 118 C1010 96 986 104 972 118 C992 116 1010 122 1024 130 Z" fill="{INK}"/></g>
    <g class="wR"><path d="M1056 118 C1090 96 1114 104 1128 118 C1108 116 1090 122 1076 130 Z" fill="{INK}"/></g>
    <path d="M1050 104 L1056 118 L1050 140 L1044 118 Z" fill="{GOLD}" stroke="{INK}"/>
    <circle cx="1050" cy="102" r="4" fill="{RED}"/>
  </g>

  <!-- scorpio, self-drawing constellation -->
  <g class="scorp" stroke="{NAVY}" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M900 322 h26 l8 -10 l8 14 l8 -8 h30 q10 0 14 -8 l6 -12"/>
  </g>
  <g fill="{RED}"><circle cx="1000" cy="298" r="3.4"/></g>
  <g fill="{NAVY}">
    <circle cx="900" cy="322" r="2.2"/><circle cx="926" cy="322" r="2.2"/>
    <circle cx="934" cy="312" r="2.2"/><circle cx="942" cy="326" r="2.2"/>
  </g>

  <!-- coins -->
  <g stroke="{INK}" stroke-width="2">
    <g class="coin"><ellipse cx="860" cy="332" rx="16" ry="6" fill="{GOLD}"/><ellipse cx="860" cy="327" rx="16" ry="6" fill="#EBD06B"/></g>
    <g class="coin coin2"><ellipse cx="916" cy="340" rx="13" ry="5" fill="{GOLD}"/><ellipse cx="916" cy="336" rx="13" ry="5" fill="#EBD06B"/></g>
    <g class="coin coin3"><ellipse cx="824" cy="342" rx="11" ry="4" fill="{GOLD}"/><ellipse cx="824" cy="338" rx="11" ry="4" fill="#EBD06B"/></g>
  </g>

  <!-- ticker tape -->
  <g clip-path="url(#tapeclip)">
    <rect x="0" y="352" width="1200" height="48" fill="{NAVY}"/>
    <g class="tape">
      <text x="20" y="382" class="ticker">{TAGRUN}</text>
      <text x="{X2}" y="382" class="ticker">{TAGRUN}</text>
      <text x="{X3}" y="382" class="ticker">{TAGRUN}</text>
    </g>
  </g>
  <line x1="20" y1="352" x2="1180" y2="352" stroke="{INK}" stroke-width="3"/>
</svg>
'''

RULE = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="34" viewBox="0 0 1200 34" role="presentation">
  <defs>
    <pattern id="z" width="60" height="34" patternUnits="userSpaceOnUse">
      <path d="M0 20 H22 L28 12 L34 24 L40 14 H60" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-linecap="square"/>
      <circle cx="50" cy="8" r="1.8" fill="{GOLD}"/>
    </pattern>
    <linearGradient id="f" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".16" stop-color="#fff"/>
      <stop offset=".84" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="m"><rect width="1200" height="34" fill="url(#f)"/></mask>
  </defs>
  <rect width="1200" height="34" fill="url(#z)" mask="url(#m)"/>
</svg>
'''

def main():
    out, title, subtitle, *tags = sys.argv[1:]
    tags = tags or ["MONEY MONEY MONEY", "SHIPPED WHILE YOU SLEEP", "ZERO TRUST FULL AUTOMATION"]
    sep = " ✦  "
    tagrun_raw = sep.join(tags) + sep
    tagrun = html.escape(tagrun_raw)
    step = int(len(tagrun_raw) * 11.5) + 40   # ~11.5px/char mono 15px + 2px tracking
    svg = TPL.format(TITLE=html.escape(title), TITLE_SVG=html.escape(title),
                     SUBTITLE=html.escape(subtitle), TAGRUN=tagrun, STEP=step,
                     NAVY=NAVY, CREAM=CREAM, GOLD=GOLD, INK=INK, RED=RED,
                     X2=20+step, X3=20+2*step).replace("{STEP}", str(step))
    Path(out).mkdir(parents=True, exist_ok=True)
    Path(out, "header.svg").write_text(svg)
    Path(out, "rule.svg").write_text(RULE)
    print(f"✓ {out}/header.svg + rule.svg")

if __name__ == "__main__":
    main()
