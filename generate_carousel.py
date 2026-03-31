"""
LinkedIn Carousel Generator — Socket Programming in Python
Generates 3 slides: Intro, Server, Client
"""

from PIL import Image, ImageDraw, ImageFont
import os, textwrap

# ── Constants ──────────────────────────────────────────────────────────────────
W, H         = 1080, 1080
BG           = "#0A0E1A"          # deep navy
ACCENT       = "#00C2FF"          # bright cyan
ACCENT2      = "#7B61FF"          # purple highlight
WHITE        = "#FFFFFF"
LIGHT_GRAY   = "#B0BAD0"
CODE_BG      = "#111827"
CODE_BORDER  = "#1E2D40"
SLIDE_DIR    = os.path.dirname(os.path.abspath(__file__))

# ── Font helpers ────────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    """Try common system fonts; fall back to PIL default."""
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    bold_candidates = [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    pool = bold_candidates if bold else candidates
    for path in pool:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def load_mono(size):
    candidates = [
        "C:/Windows/Fonts/consola.ttf",    # Consolas
        "C:/Windows/Fonts/cour.ttf",       # Courier New
        "C:/Windows/Fonts/lucon.ttf",      # Lucida Console
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# ── Drawing helpers ─────────────────────────────────────────────────────────────
def new_slide():
    img = Image.new("RGB", (W, H), BG)
    d   = ImageDraw.Draw(img)
    return img, d

def draw_top_bar(d, label):
    """Thin accent bar + slide label at top."""
    d.rectangle([(0, 0), (W, 6)], fill=ACCENT)
    d.rectangle([(0, 6), (W, 7)], fill=ACCENT2)
    tag_font = load_font(22, bold=True)
    d.text((40, 24), label, font=tag_font, fill=ACCENT)

def draw_bottom_bar(d, note=""):
    d.rectangle([(0, H - 7), (W, H)], fill=ACCENT2)
    d.rectangle([(0, H - 8), (W, H - 7)], fill=ACCENT)
    if note:
        f = load_font(22)
        d.text((40, H - 50), note, font=f, fill=LIGHT_GRAY)

def draw_tag(d, text, x, y, bg=ACCENT, fg=BG):
    f = load_font(22, bold=True)
    bbox = d.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad = 10
    d.rounded_rectangle([x, y, x + tw + pad*2, y + th + pad*2], radius=6, fill=bg)
    d.text((x + pad, y + pad), text, font=f, fill=fg)
    return y + th + pad * 2 + 12

def draw_code_block(d, lines, x, y, width, line_height=34):
    """Draw a rounded code block with syntax-coloured lines."""
    padding     = 20
    total_h     = len(lines) * line_height + padding * 2
    d.rounded_rectangle(
        [x, y, x + width, y + total_h],
        radius=10,
        fill=CODE_BG,
        outline=CODE_BORDER,
        width=2,
    )
    mono = load_mono(22)
    cy = y + padding
    for raw in lines:
        colour, text = raw if isinstance(raw, tuple) else (LIGHT_GRAY, raw)
        d.text((x + padding, cy), text, font=mono, fill=colour)
        cy += line_height
    return y + total_h

def wrap_text(d, text, font, max_width, x, y, fill, line_spacing=10):
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        if d.textlength(test, font=font) <= max_width:
            line.append(w)
        else:
            lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    for l in lines:
        d.text((x, y), l, font=font, fill=fill)
        y += d.textbbox((0,0), l, font=font)[3] + line_spacing
    return y

# ── Slide 1 — Introduction ──────────────────────────────────────────────────────
def slide_intro():
    img, d = new_slide()
    draw_top_bar(d, "01 / 03  •  PYTHON SOCKET PROGRAMMING")

    # Hero title
    title_font = load_font(72, bold=True)
    d.text((40, 100), "Socket", font=title_font, fill=WHITE)
    d.text((40, 180), "Programming", font=title_font, fill=ACCENT)
    d.text((40, 260), "in Python", font=title_font, fill=WHITE)

    sub_font = load_font(30)
    y = 370
    y = wrap_text(d, "Sockets let two programs talk to each other over a network — even on the same machine.", sub_font, W - 80, 40, y, LIGHT_GRAY)
    y += 20

    # sockets.py snippet
    code_lines = [
        (ACCENT,      "import socket"),
        (LIGHT_GRAY,  ""),
        (LIGHT_GRAY,  "host = socket.gethostname()"),
        (LIGHT_GRAY,  "addr = socket.gethostbyname(host)"),
        (LIGHT_GRAY,  "info = socket.gethostbyaddr('127.0.0.1')"),
    ]
    y = draw_code_block(d, code_lines, 40, y, W - 80) + 30

    # Key concepts row
    concepts = [("AF_INET", "IPv4"), ("SOCK_STREAM", "TCP"), ("bind / connect", "Roles")]
    box_w = (W - 80 - 20) // 3
    bx = 40
    for label, sub in concepts:
        d.rounded_rectangle([bx, y, bx + box_w, y + 90], radius=8, fill=CODE_BG, outline=ACCENT2, width=2)
        lf = load_font(22, bold=True)
        sf = load_font(18)
        tw = d.textlength(label, font=lf)
        d.text((bx + (box_w - tw)//2, y + 10), label, font=lf, fill=ACCENT)
        sw = d.textlength(sub, font=sf)
        d.text((bx + (box_w - sw)//2, y + 44), sub, font=sf, fill=LIGHT_GRAY)
        bx += box_w + 10

    draw_bottom_bar(d, "swipe for server →")
    img.save(os.path.join(SLIDE_DIR, "slide_01_intro.png"))
    print("✓  slide_01_intro.png")

# ── Slide 2 — Server ───────────────────────────────────────────────────────────
def slide_server():
    img, d = new_slide()
    draw_top_bar(d, "02 / 03  •  THE SERVER")

    title_font = load_font(60, bold=True)
    d.text((40, 90), "server.py", font=title_font, fill=ACCENT)

    sub_font = load_font(28)
    y = 175
    y = wrap_text(d, "The server binds to a port and waits. When a client connects, it sends a welcome message.", sub_font, W - 80, 40, y, LIGHT_GRAY)
    y += 20

    code_lines = [
        (ACCENT,      "import socket"),
        (LIGHT_GRAY,  ""),
        (ACCENT2,     "with socket.socket("),
        (LIGHT_GRAY,  "        socket.AF_INET, socket.SOCK_STREAM) as s:"),
        (LIGHT_GRAY,  ""),
        ("#6EE7B7",   "    s.bind((socket.gethostname(), 4571))"),
        ("#6EE7B7",   "    s.listen(5)"),
        (LIGHT_GRAY,  "    print('Server is up. Listening...')"),
        (LIGHT_GRAY,  ""),
        ("#FCD34D",   "    client, address = s.accept()"),
        (LIGHT_GRAY,  "    client.send("),
        (LIGHT_GRAY,  "        bytes('Hello! Welcome.','utf-8'))"),
    ]
    y = draw_code_block(d, code_lines, 40, y, W - 80) + 24

    # Step annotations
    steps = [
        (ACCENT,   "bind()",    "Attach to hostname + port 4571"),
        ("#6EE7B7","listen(5)", "Queue up to 5 pending connections"),
        ("#FCD34D","accept()",  "Block until a client connects"),
    ]
    step_font_b = load_font(22, bold=True)
    step_font   = load_font(22)
    for colour, kw, desc in steps:
        d.text((40,  y), kw,   font=step_font_b, fill=colour)
        kw_w = d.textlength(kw, font=step_font_b)
        d.text((40 + kw_w + 8, y), f"— {desc}", font=step_font, fill=LIGHT_GRAY)
        y += 34

    draw_bottom_bar(d, "swipe for client →")
    img.save(os.path.join(SLIDE_DIR, "slide_02_server.png"))
    print("✓  slide_02_server.png")

# ── Slide 3 — Client ───────────────────────────────────────────────────────────
def slide_client():
    img, d = new_slide()
    draw_top_bar(d, "03 / 03  •  THE CLIENT")

    title_font = load_font(60, bold=True)
    d.text((40, 90), "client.py", font=title_font, fill=ACCENT2)

    sub_font = load_font(28)
    y = 175
    y = wrap_text(d, "The client reaches out to the server, connects, then listens for the reply — all in 6 lines.", sub_font, W - 80, 40, y, LIGHT_GRAY)
    y += 20

    code_lines = [
        (ACCENT,   "import socket"),
        (LIGHT_GRAY, ""),
        (ACCENT2,  "with socket.socket("),
        (LIGHT_GRAY,"        socket.AF_INET, socket.SOCK_STREAM) as s:"),
        (LIGHT_GRAY, ""),
        ("#FCD34D",  "    s.connect((socket.gethostname(), 4571))"),
        (LIGHT_GRAY, ""),
        ("#6EE7B7",  "    msg = s.recv(1024)"),
        (LIGHT_GRAY, "    print(f\"Message: {msg.decode('utf-8')}\")"),
    ]
    y = draw_code_block(d, code_lines, 40, y, W - 80) + 24

    # Step annotations
    steps = [
        ("#FCD34D","connect()", "Dial the server at hostname:4571"),
        ("#6EE7B7","recv(1024)","Receive up to 1024 bytes"),
        (ACCENT,  "decode()",  "Convert bytes → readable string"),
    ]
    step_font_b = load_font(22, bold=True)
    step_font   = load_font(22)
    for colour, kw, desc in steps:
        d.text((40,  y), kw,   font=step_font_b, fill=colour)
        kw_w = d.textlength(kw, font=step_font_b)
        d.text((40 + kw_w + 8, y), f"— {desc}", font=step_font, fill=LIGHT_GRAY)
        y += 34

    # "That's it!" closer
    y += 10
    closer_font = load_font(30, bold=True)
    d.text((40, y), "Run server.py first, then client.py — and watch them talk!", font=closer_font, fill=WHITE)

    draw_bottom_bar(d, "github.com/epas0  •  #Python #Networking")
    img.save(os.path.join(SLIDE_DIR, "slide_03_client.png"))
    print("✓  slide_03_client.png")

# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    slide_intro()
    slide_server()
    slide_client()
    print("\nAll 3 carousel slides saved to", SLIDE_DIR)
