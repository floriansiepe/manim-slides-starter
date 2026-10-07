import base64
import os
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TITLE = "demo" # Replace with your actual presentation title
SCENES = ("BasicExample", "AnotherExample")  # Replace with your actual scene names

def _build(quality: str, suffix: str) -> None:
    output = ROOT / "build" / f"main-{suffix}.html"
    output.parent.mkdir(exist_ok=True)

    subprocess.run(
        ("manim-slides", "render", "--quality", quality, "src/manim_slides_starter/main.py", *SCENES), cwd=ROOT, check=True
    )
    with tempfile.TemporaryDirectory() as tmp:
        convert = (
            "manim-slides",
            "convert",
            "--to",
            "html",
            "--one-file",
            "--offline",
            "-ccontrols=true", # Optional control buttons
            # "-cslide_number=c/t", # Add a slide number in the format current/total, uncomment if needed
            "-cbackground_color=#000000", # Default black background, change if needed
            "-ctitle=" + TITLE,
            *SCENES,
            str(output.relative_to(ROOT)),
        )
        subprocess.run(convert, cwd=ROOT, check=True)


def slides_l() -> None:
    """Build a 480p offline presentation."""
    _build("l", "480p")


def slides_m() -> None:
    """Build a 720p offline presentation."""
    _build("m", "720p")


def slides_h() -> None:
    """Build a 1080p offline presentation."""
    _build("h", "1080p")


def slides_p() -> None:
    """Build a 1440p offline presentation."""
    _build("p", "1440p")


def slides_k() -> None:
    """Build a 4K offline presentation."""
    _build("k", "4k")
