#!/usr/bin/env python3
"""
ContentSpy Demo Video v2 — Apple-style product demo
Структура: вставки → zoom-in на секции → описание фичи → демонстрация
Uses Pillow for text cards (ffmpeg has no drawtext here)
"""

import subprocess
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/Users/Shared/workspace/products/contentspy/landing/video"
IMG = "/Users/Shared/workspace/products/contentspy/landing/img"
TMP = f"{OUT_DIR}/tmp_v2"
OUTPUT = f"{OUT_DIR}/demo-v2.mp4"

W, H, FPS = 1280, 800, 30
FONT_PATH = "/System/Library/Fonts/SFNS.ttf"
ENC = ["-c:v", "libx264", "-preset", "fast", "-crf", "20", "-an", "-pix_fmt", "yuv420p"]

os.makedirs(TMP, exist_ok=True)


def run(cmd, label=""):
    print(f"[{label}]" if label else "", "...", sep="")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("STDERR:", result.stderr[-3000:])
        raise RuntimeError(f"ffmpeg failed: {label}")
    print("  OK")


def hex_to_rgb(h):
    h = h.lstrip("0x").lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def make_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()


def create_text_card_png(path, lines, bg_color=(12, 12, 15)):
    """
    lines = list of (text, fontsize, color_hex, y_offset_from_center)
    """
    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)

    for text, fontsize, color_hex, y_off in lines:
        font = make_font(fontsize)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (W - tw) // 2
        y = (H // 2) - (th // 2) + y_off
        color = hex_to_rgb(color_hex)
        draw.text((x, y), text, fill=color, font=font)

    img.save(path)


def png_to_video(png_path, out_path, duration, fade_in=0.4):
    """Convert a PNG to a video clip with fade-in"""
    fade_frames = int(fade_in * FPS)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", str(FPS), "-i", png_path,
        "-vf", f"fade=in:0:{fade_frames}",
        *ENC, "-t", str(duration), out_path
    ]
    run(cmd, f"png→video: {os.path.basename(out_path)}")


def screenshot_zoom(out, img_path, duration, zoom_to=1.5, cx=None, cy=None):
    """
    Apply zoompan to a screenshot.
    cx, cy: center of zoom target in SOURCE image coords (default: center)
    """
    frames = int(duration * FPS)
    zoom_speed = (zoom_to - 1.0) / frames

    # Get source dimensions
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0", img_path],
        capture_output=True, text=True
    )
    dims = probe.stdout.strip().split("x")
    src_w, src_h = int(dims[0]), int(dims[1])

    # Crop to 1280x800 if taller
    crop_filter = ""
    eff_h = src_h
    if src_h > H:
        cy_crop = (src_h - H) // 2
        crop_filter = f"crop={W}:{H}:0:{cy_crop},"
        eff_h = H

    # Set defaults
    if cx is None:
        cx = W // 2
    if cy is None:
        cy = eff_h // 2

    # zoompan: zoom from 1 → zoom_to, pan toward (cx, cy)
    zoom_expr = f"min(zoom+{zoom_speed:.6f},{zoom_to})"
    pan_x = f"min(max(0,{cx}-iw/(zoom*2)),iw-iw/zoom)"
    pan_y = f"min(max(0,{cy}-ih/(zoom*2)),ih-ih/zoom)"
    zoom_filter = f"zoompan=z='{zoom_expr}':x='{pan_x}':y='{pan_y}':d={frames}:s={W}x{H}:fps={FPS}"

    fade_frames = int(0.4 * FPS)
    vf = f"{crop_filter}{zoom_filter},fade=in:0:{fade_frames}"

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", img_path,
        "-vf", vf,
        *ENC, "-t", str(duration), out
    ]
    run(cmd, f"screenshot_zoom: {os.path.basename(img_path)}")


def screenshot_zoom_with_label(out, img_path, duration, zoom_to=1.5, cx=None, cy=None,
                                label_lines=None):
    """Screenshot zoom + overlay text label (using Pillow for label)"""
    # First create zoom video
    tmp_zoom = out.replace(".mp4", "_zoom_tmp.mp4")
    screenshot_zoom(tmp_zoom, img_path, duration, zoom_to=zoom_to, cx=cx, cy=cy)

    if not label_lines:
        os.rename(tmp_zoom, out)
        return

    # Create label PNG (semi-transparent overlay style)
    label_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(label_img)

    # Draw semi-transparent background bar
    bar_y = H - 120
    draw.rectangle([(0, bar_y), (W, H)], fill=(0, 0, 0, 160))

    for text, fontsize, color_hex, y_pos in label_lines:
        font = make_font(fontsize)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) // 2
        color = hex_to_rgb(color_hex) + (255,)
        draw.text((x, y_pos), text, fill=color, font=font)

    label_rgb = Image.new("RGB", (W, H), (0, 0, 0))
    label_rgb.paste(label_img, mask=label_img.split()[3])
    label_png = out.replace(".mp4", "_label.png")
    label_rgb.save(label_png)

    # Create label video (same duration, fade in after 1s)
    label_vid = out.replace(".mp4", "_label_tmp.mp4")
    fade_start = int(1.0 * FPS)
    fade_frames = int(0.5 * FPS)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", str(FPS), "-i", label_png,
        "-vf", f"fade=in:{fade_start}:{fade_frames}",
        *ENC, "-t", str(duration), label_vid
    ]
    run(cmd, "label video")

    # Overlay label on zoom
    cmd = [
        "ffmpeg", "-y",
        "-i", tmp_zoom, "-i", label_vid,
        "-filter_complex", "[0:v][1:v]blend=all_mode=addition:all_opacity=1[vout]",
        "-map", "[vout]",
        *ENC, "-t", str(duration), out
    ]
    run(cmd, "overlay label")

    # Cleanup
    for f in [tmp_zoom, label_vid, label_png]:
        if os.path.exists(f):
            os.remove(f)


# ============================================================
# CREATE SEGMENTS
# ============================================================
print("\n🎬 Creating ContentSpy Demo v2 (Apple-style)\n")
print("Structure: Title → Brand → Overview → Zoom Features → AI → CTA\n")

segments = []  # list of (path, duration)


# --- S01: ВСТАВКА — Problem hook (3.0s) ---
s01_png = f"{TMP}/s01.png"
s01 = f"{TMP}/s01.mp4"
create_text_card_png(s01_png, [
    ("Your competitors are posting.",  56, "ffffff", -48),
    ("You're guessing.",               40, "888888",  32),
], bg_color=(12, 12, 15))
png_to_video(s01_png, s01, 3.0)
segments.append((s01, 3.0))
print()

# --- S02: ВСТАВКА — Brand intro (2.5s) ---
s02_png = f"{TMP}/s02.png"
s02 = f"{TMP}/s02.mp4"
create_text_card_png(s02_png, [
    ("ContentSpy",                        68, "ffffff", -50),
    ("Understand why competitors win.",    32, "5599ff",  30),
], bg_color=(8, 8, 16))
png_to_video(s02_png, s02, 2.5)
segments.append((s02, 2.5))
print()

# --- S03: Dashboard overview (3.0s) — gentle zoom showing full app ---
s03 = f"{TMP}/s03.mp4"
screenshot_zoom(s03, f"{IMG}/dashboard.png", 3.0, zoom_to=1.18, cx=640, cy=400)
segments.append((s03, 3.0))
print()

# --- S04: ВСТАВКА — Caption (2.0s) ---
s04_png = f"{TMP}/s04.png"
s04 = f"{TMP}/s04.mp4"
create_text_card_png(s04_png, [
    ("All your competitor content.",  46, "ffffff", -35),
    ("Analyzed automatically.",        32, "5599ff",  30),
], bg_color=(8, 8, 16))
png_to_video(s04_png, s04, 2.0)
segments.append((s04, 2.0))
print()

# --- S05: Content Hub zoom (3.0s) — zoom into video grid ---
s05 = f"{TMP}/s05.mp4"
screenshot_zoom(s05, f"{IMG}/content-hub.png", 3.0, zoom_to=1.6, cx=640, cy=380)
segments.append((s05, 3.0))
print()

# --- S06: HOOKS HERO — zoom into viral scores (4.0s) ---
s06 = f"{TMP}/s06.mp4"
screenshot_zoom_with_label(
    s06, f"{IMG}/hooks.png", 4.0,
    zoom_to=2.0,
    cx=850, cy=220,  # right-top area where viral scores are
    label_lines=[
        ("27.2x Viral Multiplier", 38, "ffd700", H - 90),
        ("Discover what makes content go viral", 24, "cccccc", H - 48),
    ]
)
segments.append((s06, 4.0))
print()

# --- S07: ВСТАВКА — Feature description (2.0s) ---
s07_png = f"{TMP}/s07.png"
s07 = f"{TMP}/s07.mp4"
create_text_card_png(s07_png, [
    ("Hook patterns. Viral multipliers.",         40, "ffffff", -50),
    ("Reverse-engineered from top performers.",   28, "888888",  20),
    ("Only ContentSpy shows you why.",            26, "5599ff",  65),
], bg_color=(8, 8, 16))
png_to_video(s07_png, s07, 2.0)
segments.append((s07, 2.0))
print()

# --- S08: AI Analysis zoom (3.0s) ---
s08 = f"{TMP}/s08.mp4"
screenshot_zoom(s08, f"{IMG}/ai-analysis.png", 3.0, zoom_to=1.5, cx=900, cy=380)
segments.append((s08, 3.0))
print()

# --- S09: ВСТАВКА — AI caption (2.0s) ---
s09_png = f"{TMP}/s09.png"
s09 = f"{TMP}/s09.mp4"
create_text_card_png(s09_png, [
    ("AI explains why it went viral.", 44, "ffffff", -35),
    ("In plain language. No guessing.", 30, "5599ff",  30),
], bg_color=(8, 8, 16))
png_to_video(s09_png, s09, 2.0)
segments.append((s09, 2.0))
print()

# --- S10: AI Chat zoom (3.0s) ---
s10 = f"{TMP}/s10.mp4"
screenshot_zoom(s10, f"{IMG}/ai-chat.png", 3.0, zoom_to=1.4, cx=640, cy=500)
segments.append((s10, 3.0))
print()

# --- S11: CTA card (3.5s) ---
s11_png = f"{TMP}/s11.png"
s11 = f"{TMP}/s11.mp4"
create_text_card_png(s11_png, [
    ("ContentSpy",                          64, "ffffff", -80),
    ("One-time payment. No subscription.",  30, "888888",  10),
    ("contentspy.co",                       38, "5599ff",  70),
    ("From $79",                            26, "555555", 125),
], bg_color=(8, 8, 16))
png_to_video(s11_png, s11, 3.5)
segments.append((s11, 3.5))
print()


# ============================================================
# CONCATENATE WITH XFADE
# ============================================================
print("🔗 Concatenating with xfade transitions...\n")

TRANS = 0.5  # transition duration

inputs = []
for seg_path, _ in segments:
    inputs += ["-i", seg_path]

n = len(segments)
filter_parts = []
offset = 0.0
prev_label = "[0:v]"

for i in range(1, n):
    _, dur = segments[i-1]
    offset += dur - TRANS
    out_label = f"[xf{i}]" if i < n - 1 else "[vout]"
    filter_parts.append(
        f"{prev_label}[{i}:v]xfade=transition=fade:duration={TRANS}:offset={offset:.2f}{out_label}"
    )
    prev_label = out_label

filter_complex = ";".join(filter_parts)
total_duration = sum(d for _, d in segments) - TRANS * (n - 1)

print(f"  Segments: {n} | Total: {total_duration:.1f}s")

cmd = [
    "ffmpeg", "-y",
    *inputs,
    "-filter_complex", filter_complex,
    "-map", "[vout]",
    "-c:v", "libx264", "-preset", "fast", "-crf", "23",
    "-pix_fmt", "yuv420p", "-an",
    "-t", str(total_duration),
    OUTPUT
]
run(cmd, "Final concat + xfade")

size_mb = os.path.getsize(OUTPUT) / 1024 / 1024
print(f"\n✅ Done!")
print(f"   File: {OUTPUT}")
print(f"   Size: {size_mb:.1f} MB")
print(f"   Duration: {total_duration:.1f}s")
print(f"   Segments: {n}")

# Cleanup
shutil.rmtree(TMP)
print("   Temp cleaned up.")
