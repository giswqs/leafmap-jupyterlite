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

[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating linked maps for visualizing multiple maps simultaneously**


```{code-cell} ipython3
%pip install -q leafmap
```

This notebook example requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
import leafmap.leafmap as leafmap
```

Print out the list of available basemaps.

```{code-cell} ipython3
print(leafmap.basemaps.keys())
```

Specify the number of rows and columns to create a linked map. The `layers` parameter accepts a list of two XYZ tile layers, which can be chosen from the basemap names, or any custom XYZ tile layer.

```{code-cell} ipython3
layers = ['ROADMAP', 'HYBRID']
leafmap.linked_maps(rows=1, cols=2, height='400px', layers=layers)
```

![](https://i.imgur.com/9qwmgPR.jpg)

```{code-cell} ipython3
layers = ['Stamen.Terrain', 'OpenTopoMap']
leafmap.linked_maps(rows=1, cols=2, height='400px', layers=layers)
```

![](https://i.imgur.com/tx89sKu.png)

+++

Create a 2 * 2 linked map to visualize land cover change. Specify the `center` and `zoom` parameters to change the default map center and zoom level.

```{code-cell} ipython3
layers = [str(f"NLCD {year} CONUS Land Cover") for year in [2001, 2006, 2011, 2016]]
labels = [str(f"NLCD {year}") for year in [2001, 2006, 2011, 2016]]
leafmap.linked_maps(
    rows=2,
    cols=2,
    height='300px',
    layers=layers,
    labels=labels,
    center=[36.1, -115.2],
    zoom=9,
)
```

![](https://i.imgur.com/VUp7H3m.png)
