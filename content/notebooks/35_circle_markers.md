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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/35_circle_markers.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/35_circle_markers.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

For a list of options for circle markers, see https://ipyleaflet.readthedocs.io/en/latest/api_reference/circle_marker.html

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4)
m.add_basemap("Stamen.Toner")
data = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
m.add_circle_markers_from_xy(
    data, x="longitude", y="latitude", radius=10, color="blue", fill_color="black"
)
m
```
