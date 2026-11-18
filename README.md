# MF Math

Math write-ups rendered with [Quarto](https://quarto.org) and published to magic-flea.com/math.

## Setup

Install Quarto (user-level, no sudo) and the Python environment used by executed cells:

```
pdm install
```

`plot_dg` (in `src/`) is installed editable, so changes to it are picked up immediately.

## Writing

Pages are Markdown (`.qmd`) with `$...$` / `$$...$$` math. Shared macros (`\R`, `\pd`, ...) live in
`_macros.html`. Executed `{python}` cells are frozen in `_freeze/` and only re-run when their page
changes; commit `_freeze/` with the page.

Live preview with reload on save:

```
pdm run quarto preview --host 0.0.0.0 --port 3000 --no-browser
```

`skill_docs/` holds working notes for the 17lands skill rating model.

Publish:

```
bash publish.sh
```

SageMath cells are shown with their saved output but are not executed.

Any code is free for copying or reuse in any context and other text content is copyright of the authors with rights reserved.

Any material copied from copyrighted text is intended as fair use educational commentary.
