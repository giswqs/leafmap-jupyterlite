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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/25_map_title.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/25_map_title.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating a population heat map with a colorbar and map title**


```{code-cell} ipython3
%pip install -q leafmap
```

The notebook requires the folium plotting backend. ipyleaflet is not supported.

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

Creates an interactive folium map.

```{code-cell} ipython3
m = leafmap.Map()
```

Specify the `latitude`, `longitude`, and `value` columns to create the heat map.

```{code-cell} ipython3
in_csv = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv"
```

Specify the file path to the CSV. It can either be a file locally or on the Internet.

```{code-cell} ipython3
m.add_heatmap(
    in_csv,
    latitude="latitude",
    longitude='longitude',
    value="pop_max",
    name="Heat map",
    radius=20,
)
```

Adds a colorbar to the map.

```{code-cell} ipython3
colors = ['blue', 'lime', 'red']
vmin = 0
vmax = 10000

m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
```

Adds a title to the map.

```{code-cell} ipython3
m.add_title("World Population Heat Map", font_size="20px", align="center")
```

```{code-cell} ipython3
m
```

Save the map as an HTML.

```{code-cell} ipython3
m.to_html("heatmap.html")
```
