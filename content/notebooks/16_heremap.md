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

**Using [HERE Map Widget for Jupyter](https://github.com/heremaps/here-map-widget-for-jupyter) as a plotting backend**


```{code-cell} ipython3
%pip install -q leafmap
```

## Prerequisites
Before you run the below cells make sure you have:
- A HERE developer account, free and available under [HERE Developer Portal](https://developer.here.com)
- An [API key](https://developer.here.com/documentation/identity-access-management/dev_guide/topics/dev-apikey.html) from the [HERE Developer Portal](https://developer.here.com)
- Export API key into environment variable `HEREMAPS_API_KEY`

    ```bash
        export HEREMAPS_API_KEY=YOUR-ACTUAL-API-KEY
    ```

```{code-cell} ipython3
import os
import leafmap.heremap as leafmap
```

```{code-cell} ipython3
# Read api_key from environment

api_key = os.environ["HEREMAPS_API_KEY"]
```

## HERE default basemap

+++

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key)
m
```

Specify the default map center and zoom level.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[50, 19], zoom=4)  # center=[lat, lon]
m
```

Set the visibility of map controls.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, fullscreen_control=False)
m
```

Change the map width and height.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, height="450px")
m
```

## Basemaps

+++

Use built-in basemaps.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, basemap="HERE_RASTER_TERRAIN_MAP")
m
```

### zoom to bounds

+++

Zoom to map to a bounding box [South, West, North, East].

```{code-cell} ipython3
m.zoom_to_bounds((-9.0882278, -55.3228175, 168.2249543, 72.2460938))  #
```

```{code-cell} ipython3
m.add_basemap(basemap="Esri.WorldTopoMap")
```

Add a custom XYZ tile layer.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, layers_control=True)
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m
```

## Add vector data
**How to add GeoJSON to the map**

+++

Add a GeoJSON from an HTTP URL to the map.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2, layers_control=True)

in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(in_geojson, layer_name="Cable lines")

m
```

Add a local GeoJSON file to the map.

```{code-cell} ipython3
import json

m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2)
with open("../data/countries.geojson") as fh:
    geo = json.load(fh)
m.add_geojson(geo, layer_name="Countries")
m
```

Customize style for the GeoJSON layer.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2)

url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"

style = {
    "fillColor": "rgba(0, 0, 255, 0.2)",
    "strokeColor": "blue",
}

hover_style = {"fillColor": "rgba(0, 0, 255, 0.7)"}

m.add_geojson(url, layer_name="Countries", style=style, hover_style=hover_style)
m
```

```{code-cell} ipython3
in_shp = '../data/countries.shp'
in_geojson = '../data/us_states.json'
in_kml = '../data/us_states.kml'
```

Add a shapefile to the map.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2)
m.add_shp(in_shp, layer_name="Shapefile")
m
```

Add a KML file to the map.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[40.273502, -86.126976], zoom=4)
m.add_kml(in_kml, layer_name="KML")
m
```

The add_vector function supports any vector data format supported by GeoPandas.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_vector(url, layer_name="Countries")
m
```

### Point style for GeoJSON

+++

Customize the style of point layers.

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=2)

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
point_style = {
    "strokeColor": 'white',
    "lineWidth": 1,
    "fillColor": "red",
    "fillOpacity": 0.7,
    "radius": 5,
}
m.add_geojson(url, layer_name="Countries", point_style=point_style, default_popup=True)
m
```

```{code-cell} ipython3
import geopandas
import json
import os

countries = geopandas.read_file(geopandas.datasets.get_path("naturalearth_cities"))
point_style = {
    "strokeColor": 'white',
    "lineWidth": 1,
    "fillColor": "blue",
    "fillOpacity": 0.7,
    "radius": 5,
}

m = leafmap.Map(api_key=api_key, center=[0, 0], zoom=3)
m.add_gdf(countries, zoom_to_layer=False, point_style=point_style, default_popup=True)
m
```
