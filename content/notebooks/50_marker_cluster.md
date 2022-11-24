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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/50_marker_cluster.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/50_marker_cluster.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating a marker cluster with custom icons**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4)
```

Use sample datasets.

```{code-cell} ipython3
cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
```

Add a GeoJSON to the map.

```{code-cell} ipython3
m.add_geojson(regions, layer_name='US Regions')
```

Add a marker cluster to the map. The input can either be a string (representing file path or HTTP URL to a csv file) or a Pandas DataFrame.

The list of available icon names can be found at <https://fontawesome.com/v4/icons>.

Please note that the `spin` parameter only supports the ipyleaflet backend. The folium backend does not support this.

```{code-cell} ipython3
m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    color_column='region',
    icon_names=['gear', 'map', 'leaf', 'globe'],
    spin=True,
    add_legend=True,
)
```

Display the map.

```{code-cell} ipython3
m
```

![](https://i.imgur.com/63LDhOx.gif)
