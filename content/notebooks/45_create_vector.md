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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/45_create_vector.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/45_create_vector.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Create an interactive map and use the drawing tool to draw shapes on the map.

```{code-cell} ipython3
m = leafmap.Map()
m
```

Save the draw features as GeoJSON, Shapefile, or GeoPackage.

```{code-cell} ipython3
m.save_draw_features("data.geojson")
```

![](https://i.imgur.com/b9RbEqb.gif)
