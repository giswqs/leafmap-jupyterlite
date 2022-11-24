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

**Creating a split-panel map with only one line of code**


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

Create a split-panel map by specifying the `left_layer` and `right_layer`, which can be chosen from the basemap names, or any custom XYZ tile layer.

```{code-cell} ipython3
leafmap.split_map(left_layer="ROADMAP", right_layer="HYBRID")
```

Hide the zoom control from the map.

```{code-cell} ipython3
leafmap.split_map(
    left_layer="Esri.WorldTopoMap", right_layer="OpenTopoMap", zoom_control=False
)
```

Add labels to the map and change the default map center and zoom level.

```{code-cell} ipython3
leafmap.split_map(
    left_layer="NLCD 2001 CONUS Land Cover",
    right_layer="NLCD 2016 CONUS Land Cover",
    left_label="2001",
    right_label="2016",
    label_position="bottom",
    center=[36.1, -114.9],
    zoom=10,
)
```

![](https://i.imgur.com/ICuhdzW.gif)
