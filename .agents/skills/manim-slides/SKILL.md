---
name: manim-slides
description: 'Create mathematical animations and turn them into interactive, slide-based presentations with Manim Slides; use when asked to animate math or craft a presentation.'
---

# Manim Slides

Use Manim Community Edition to build the visual content and Manim Slides to divide it into presenter-controlled segments and export it as a presentation. Apply this skill whenever the user asks for mathematical animations or to craft a presentation.

## Workflow

1. Clarify the presentation goal, audience, mathematical level, target format, and any constraints that materially affect the result. If the user has already specified these, proceed without asking again.
2. Inspect the project before editing. Reuse its installed Manim and Manim Slides versions, scene organization, build scripts, and export conventions. Check the installed CLI help when command options or output formats are uncertain.
3. Plan a sequence of clear visual beats: introduce the question, build intuition with diagrams or motion, explain the key idea, then summarize. Keep each beat focused and make the visual state at every pause understandable.
4. Implement each presentation scene as a subclass of `manim_slides.Slide` and put the scene construction in `construct()`. Use standard Manim mobjects and animations to create the visuals; insert `self.next_slide()` where the presenter should advance. Keep objects on screen when they provide useful continuity, and animate or remove them when the story moves on.
5. Render at a fast, low quality while iterating. Fix layout, timing, text legibility, mathematical correctness, and transitions before producing the requested final quality and format.
6. Convert rendered slides with the project's existing workflow. Confirm the expected output path and format from the repository's scripts or `manim-slides convert --help`; do not assume a format or overwrite existing deliverables without checking.

## Minimal example

```python
from manim import *
from manim_slides import Slide


class PythagoreanTheorem(Slide):
    def construct(self):
        equation = MathTex("a^2 + b^2 = c^2")
        self.play(Write(equation))
        self.next_slide()

        square = Square().next_to(equation, DOWN)
        self.play(Create(square))
        self.next_slide()
```

## Rendering and conversion

In this repository, use the existing uv scripts to render and convert the presentation into an offline, single-file HTML presentation in `build/`:

| Command | Quality | Output |
| --- | --- | --- |
| `uv run slides-l` | 480p | `build/main-480p.html` |
| `uv run slides-m` | 720p | `build/main-720p.html` |
| `uv run slides-h` | 1080p | `build/main-1080p.html` |
| `uv run slides-k` | 4K | `build/main-4k.html` |

Use `uv run slides-l` while iterating and the requested quality for the final presentation. Edit scenes in `src/manim_slides_starter/main.py` and update `SCENES` in `src/manim_slides_starter/build.py` when adding, renaming, or reordering scenes; set `TITLE` there for the presentation title. These scripts handle both rendering and HTML conversion, so a separate conversion command is unnecessary.

For projects without these scripts, a common direct render invocation is:

```bash
manim-slides render --quality l path/to/presentation.py SceneName
```

Then convert the rendered scene using the desired format and options supported by the installed version. For example, the starter project in this repository builds an offline, single-file HTML presentation with:

```bash
manim-slides convert --to html --one-file --offline SceneName build/presentation.html
```

Check `manim-slides render --help` and `manim-slides convert --help` if options differ by version. Do not use plain `manim render` as a substitute for the Manim Slides render workflow when presenter-controlled slide boundaries are required.

## Presentation and animation practices

- Use `self.next_slide()` to mark deliberate presenter-controlled pauses, not after every small animation.
- Make the progression meaningful: introduce one idea at a time, then transform or connect existing objects to show relationships.
- Keep equations, labels, and diagrams large enough to read at the target presentation resolution; avoid crowding and excessive on-screen text.
- Use `MathTex` or `Tex` for mathematical notation and ordinary text mobjects for prose. Split long equations into meaningful parts when that helps pacing or emphasis.
- Keep important content within the frame and check that labels remain attached to the intended geometry after transformations.
- Prefer a low-quality preview render during iteration; render at the requested quality once the scene and pacing are ready.
- Preserve the project's scene names, quality presets, output directory, and existing build entry points unless the user asks to change them.
- If a render or conversion fails, report the concrete error and resolve its cause; do not claim an export succeeded when it did not.

## References

- Manim Slides documentation: https://manim-slides.eertmans.be/
- Manim Community documentation: https://docs.manim.community/
- Manim Slides repository: https://github.com/jeertmans/manim-slides
