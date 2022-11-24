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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/15_openstreetmap.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/15_openstreetmap.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Downloading OpenStreetMap data with a single line of code**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install geopandas osmnx
```

```{code-cell} ipython3
import leafmap
```

Add OSM data of place(s) by name or ID to the map. Note that the leafmap custom layer control does not support GeoJSON, we need to use the ipyleaflet built-in layer control. 

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_geocode("New York City", layer_name='NYC')
m
```

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_geocode("Chicago, Illinois", layer_name='Chicago, IL')
m
```

Show OSM feature tags.

https://wiki.openstreetmap.org/wiki/Map_features

```{code-cell} ipython3
# leafmap.osm_tags_list()
```

Add OSM entities within some distance N, S, E, W of address to the map.

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_address(
    address="New York City", tags={"amenity": "bar"}, dist=1500, layer_name="NYC bars"
)
m
```

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_address(
    address="New York City",
    tags={"landuse": ["retail", "commercial"], "building": True},
    dist=1000,
    layer_name="NYC buildings",
)
m
```

Add OSM entities within a N, S, E, W bounding box to the map.

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
north, south, east, west = 40.7551, 40.7454, -73.9738, -73.9965
m.add_osm_from_bbox(
    north, south, east, west, tags={"amenity": "bar"}, layer_name="NYC bars"
)
m
```

Add OSM entities within some distance N, S, E, W of a point to the map.

```{code-cell} ipython3
m = leafmap.Map(
    center=[46.7808, -96.0156], zoom=12, toolbar_control=False, layers_control=True
)
m.add_osm_from_point(
    center_point=(46.7808, -96.0156),
    tags={"natural": "water"},
    dist=10000,
    layer_name="Lakes",
)
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[39.9170, 116.3908], zoom=15, toolbar_control=False, layers_control=True
)
m.add_osm_from_point(
    center_point=(39.9170, 116.3908),
    tags={"building": True, "natural": "water"},
    dist=1000,
    layer_name="Beijing",
)
m
```

Add OSM entities within the current map view to the map.

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.set_center(-73.9854, 40.7500, 16)
m
```

The `add_osm_from_view()` is only available for the ipyleaflet plotting backend. 

```{code-cell} ipython3
# m.add_osm_from_view(tags={"amenity": "bar", "building": True}, layer_name="New York")
```

Create a GeoPandas GeoDataFrame from place.

```{code-cell} ipython3
gdf = leafmap.osm_gdf_from_place("New York City", tags={"amenity": "bar"})
gdf
```
