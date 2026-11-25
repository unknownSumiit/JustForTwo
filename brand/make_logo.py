"""Just Two Plates logo kit. Text is converted to outlines so it looks the same everywhere.
Fonts: Lora (OFL), Inter (OFL)."""
import os, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
TEAL, CHERRY, CREAM, INK, BUTTER = "#4f6b4a", "#7a2e4d", "#fffdfb", "#2a2226", "#f5c6d8"

lora = instantiateVariableFont(TTFont("/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"), {"wght": 700})
inter = TTFont("/usr/share/fonts/opentype/inter/Inter-Bold.otf")


class Font:
    def __init__(self, tt):
        self.gs, self.cmap, self.hmtx, self.upm = tt.getGlyphSet(), tt.getBestCmap(), tt["hmtx"], tt["head"].unitsPerEm

    def text(self, s, x, y, size, tracking=0.0):
        sc, pen, cx = size / self.upm, SVGPathPen(self.gs), x
        for ch in s:
            name = self.cmap[ord(ch)]
            self.gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
            cx += self.hmtx[name][0] * sc + tracking * size
        return pen.getCommands(), cx - x - tracking * size


LORA, INTER = Font(lora), Font(inter)


def mark(card=CREAM, edge=TEAL, line=CHERRY, faint=TEAL, heart=CHERRY):
    """Two plates side by side, with a little heart where they meet."""
    return f'''
  <circle cx="34" cy="52" r="26" fill="{card}" stroke="{heart}" stroke-width="6"/>
  <circle cx="34" cy="52" r="14" fill="none" stroke="{heart}" stroke-width="3" opacity=".45"/>
  <circle cx="64" cy="52" r="26" fill="{card}" stroke="{edge}" stroke-width="6"/>
  <circle cx="64" cy="52" r="14" fill="none" stroke="{edge}" stroke-width="3" opacity=".45"/>
  <path d="M49 34 C44 29 44 23 48 21.5 C50 20.8 51.5 22 52 23.4 C52.5 22 54 20.8 56 21.5 C60 23 60 29 52 35 Z" transform="translate(-3 -4)" fill="{heart}" stroke="{card}" stroke-width="2"/>'''


def lockup(word=INK, small=CHERRY, card=CREAM, edge=TEAL):
    top_d, top_w = LORA.text("Just Two", 106, 58, 44)
    main_d, main_w = INTER.text("PLATES", 109, 86, 18, tracking=0.55)
    W = int(106 + max(top_w, main_w) + 8)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 100" width="{W * 3}" height="300">'
            f'<g transform="translate(4 2)">{mark(card=card, edge=edge)}</g>'
            f'<path d="{top_d}" fill="{word}"/><path d="{main_d}" fill="{small}"/></svg>'), W


def icon(bg=CREAM, rx=22):
    back = f'<rect width="100" height="100" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{back}<g transform="translate(1 3) scale(.98)">{mark()}</g></svg>'


logo, W = lockup()
open(os.path.join(OUT, "just-two-plates-logo.svg"), "w").write(logo)
open(os.path.join(OUT, "just-two-plates-logo-white.svg"), "w").write(lockup(word="#ffffff", small=BUTTER, card="#241e22", edge="#a9c7a2")[0])
open(os.path.join(OUT, "just-two-plates-icon.svg"), "w").write(icon())
open(os.path.join(OUT, "just-two-plates-icon-square.svg"), "w").write(icon(rx=0))
print("width", W)
