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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/18_point_layer.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/18_point_layer.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding a point layer with popup attributes to the map**

The notebook requires the ipyleaflet plotting backend. Folium is not supported. The point dataset can be any geopandas-supported file stored locally or online. 



```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
from leafmap import leafmap
```

Use the toolbar GUI to open a point-type vector dataset.

```{code-cell} ipython3
m = leafmap.Map()
m
```

Display a single popup attribute.

```{code-cell} ipython3
m = leafmap.Map()
m.add_point_layer("../data/us_cities.geojson", popup="name", layer_name="US Cities")
m
```

Display multiple popup attributes.

```{code-cell} ipython3
m = leafmap.Map()
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.geojson"
m.add_point_layer(url, popup=["name", "pop_max"], layer_name="US Cities")
m
```

![](https://i.imgur.com/1QVEtlN.gif)
