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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/10_add_vector.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/10_add_vector.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding local vector data (e.g., shp, geojson, kml) to the map**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
m
```

This demo is based on the ipyleaflet plotting backend. The folium plotting backend does not have the interactive GUI for loading local vector data.

+++

![](https://i.imgur.com/hnaTPZa.gif)

+++

Add a GeoJSON to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)

in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(in_geojson, layer_name="Cable lines")

m
```

Add a GeoJSON with random filled color to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_geojson(
    url, layer_name="Countries", fill_colors=['red', 'yellow', 'green', 'orange']
)
m
```

Use the `style_callback`function for assigning a random color to each polygon.

```{code-cell} ipython3
import random

m = leafmap.Map(center=[0, 0], zoom=2)

url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"


def random_color(feature):
    return {
        'color': 'black',
        'fillColor': random.choice(['red', 'yellow', 'green', 'orange']),
    }


m.add_geojson(url, layer_name="Countries", style_callback=random_color)
m
```

Use custom `style` and `hover_style` functions.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)

url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"

style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,
}

hover_style = {"fillOpacity": 0.7}

m.add_geojson(url, layer_name="Countries", style=style, hover_style=hover_style)
m
```

Add a shapefile to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)

in_shp = '../data/countries.shp'
m.add_shp(in_shp, layer_name="Countries")

m
```

Add a KML to the map.

```{code-cell} ipython3
m = leafmap.Map()

in_kml = '../data/us_states.kml'
m.add_kml(in_kml, layer_name="US States KML")

m
```

The `add_vector` function supports any vector data format supported by GeoPandas.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_vector(
    url, layer_name="Countries", fill_colors=['red', 'yellow', 'green', 'orange']
)
m
```

```{code-cell} ipython3
m = leafmap.Map()
```

```{code-cell} ipython3
in_shp = '../data/countries.shp'
in_geojson = '../data/us_states.json'
in_kml = '../data/us_states.kml'
```

```{code-cell} ipython3
m.add_shp(in_shp, layer_name="Shapefile")
```

```{code-cell} ipython3
m.add_geojson(in_geojson, layer_name="GeoJSON")
```

```{code-cell} ipython3
m.add_kml(in_kml, layer_name="KML")
```

```{code-cell} ipython3
m
```
