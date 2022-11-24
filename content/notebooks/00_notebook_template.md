---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/00_notebook_template.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/01_leafmap_intro.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

If you are using a recently implemented leafmap feature that has not yet been released to PyPI or conda-forge, you can uncomment the following line to install the development version from GitHub.

```{code-cell} ipython3
# leafmap.update_package()
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m
```
