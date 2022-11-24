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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/17_vector_tile_layer.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/17_vector_tile_layer.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding a vector tile layer to the map**



```{code-cell} ipython3
%pip install -q leafmap
```

This notebook example requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
from leafmap import leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
```

The URL to the vector tile.

```{code-cell} ipython3
url = 'https://tile.nextzen.org/tilezen/vector/v1/512/all/{z}/{x}/{y}.mvt?api_key=gCZXZglvRQa6sB2z7JzL1w'
```

Attribution of the vector tile.

```{code-cell} ipython3
attribution = "Nextzen"
```

One can customize the vector tile layer style if needed. More info can be found at https://ipyleaflet.readthedocs.io/en/latest/api_reference/vector_tile.html

```{code-cell} ipython3
vector_tile_layer_styles = {}
```

Add the vector tile layer to the map.

```{code-cell} ipython3
m.add_vector_tile_layer(url, attribution, vector_tile_layer_styles)
m
```
