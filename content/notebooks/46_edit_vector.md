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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/46_edit_vector.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/46_edit_vector.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
from leafmap import leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map(center=(37.712615, -122.386665), zoom=12)
m.add_basemap("HYBRID")
m
```

Add existing vector data to the map.

```{code-cell} ipython3
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/training_samples.geojson"
m.edit_vector(url)
```

Edit the existing vector data using the drawing tools and save the resulting vector data as GeoJSON, Shapefile, or GeoPackage.

```{code-cell} ipython3
m.save_draw_features("data.geojson")
```
