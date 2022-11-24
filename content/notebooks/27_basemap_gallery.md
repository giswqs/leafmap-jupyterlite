---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3.9.13 ('geo')
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/27_basemap_gallery.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/27_basemap_gallery.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.leafmap as leafmap
```

Select 100 basemaps

```{code-cell} ipython3
layers = list(leafmap.basemaps.keys())[17:117]
# layers
```

Print out the labels

```{code-cell} ipython3
print(layers[:10])
```

Create linked maps of 100 basemaps

```{code-cell} ipython3
leafmap.linked_maps(rows=20, cols=5, height="200px", layers=layers, labels=layers)
```
