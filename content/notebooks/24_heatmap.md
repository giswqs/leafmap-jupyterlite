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

**Creating heat maps from csv**


```{code-cell} ipython3
%pip install -q leafmap
```

Specify the file path to the CSV. It can either be a file locally or on the Internet.

```{code-cell} ipython3
filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
```

Use the ipyleaflet plotting backend.

```{code-cell} ipython3
import leafmap.leafmap as leafmap
```

Specify the `latitude`, `longitude`, and `value` columns to create the heat map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Stamen.Toner")
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude='longitude',
    value="pop_max",
    name="Heat map",
    radius=20,
)
m
```

Use the folium plotting backend.

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

Specify the `latitude`, `longitude`, and `value` columns to create the heat map.

```{code-cell} ipython3
m = leafmap.Map(tiles='stamentoner')
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude='longitude',
    value="pop_max",
    name="Heat map",
    radius=20,
)
m
```
