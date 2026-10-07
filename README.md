# manim-slides-starter

## Setup

Follow the instructions in the [Manim installation guide](https://docs.manim.community/en/stable/installation/uv.html) to install Manim and its dependencies.

Then, install the python packages with:
```bash
uv sync
```

## Changing the presentation

Add regular Manim slides to the [main.py](src/manim_slides_starter/main.py) and add or adjust their order in [build.py](src/manim_slides_starter/build.py).

## Usage

```bash
uv run slides-l # 480p
uv run slides-m # 720p
uv run slides-h # 1080p
uv run slides-p # 1440p
uv run slides-k # 4k
```

This will output a single HTML presentation file in the [build](build) directory.