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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/13_geopandas.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/13_geopandas.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding a GeoPandas GeoDataFrame to the map with a single line of code**

Uncomment the following line to install [leafmap](https://leafmap.org) if needed. You can also use conda to create a new environment to install geopandas and leafmap.

```
conda create geo -n python=3.8
conda activate geo
conda install geopandas
conda install mamba -c conda-forge
mamba install leafmap -c conda-forge
```

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import piplite
await piplite.install(['geopandas', 'shapely', 'pyproj'], deps=False)
```

```{code-cell} ipython3
import leafmap
import geopandas as gpd
```

```{code-cell} ipython3
# leafmap.update_package()
```

Use GeoPandas to read a GeoJSON from an HTTP URL and return it as a GeoDataFrame.

Sample data: https://github.com/giswqs/leafmap/raw/master/examples/data/cable_geo.geojson

```{code-cell} ipython3
gdf = gpd.read_file(
    "https://github.com/giswqs/leafmap/raw/master/examples/data/cable_geo.geojson"
)
```

Add a GeoDataFrame to the map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_gdf(gdf, layer_name="Cable lines")
m
```

The following example requires the ipyleaflet plotting backend.  

```{code-cell} ipython3
import leafmap.leafmap as leafmap  # for ipyleaflet only
```

Read the GeoPandas sample dataset as a GeoDataFrame.

```{code-cell} ipython3
path_to_data = gpd.datasets.get_path("nybb")
gdf = gpd.read_file(path_to_data)
gdf
```

Convert the GeoDataFrame to GeoJSON. Users can then use `add_geojson()` to add the GeoJSON to the map. Alternatively, users can directly use the `add_gdf()` function to add a GeoDataFrame to the map. Note you when hovering the mouse over the layer, an information box is shown at the lower right corner of the map. This feature is only available for the ipyleaflet plotting backend.

```{code-cell} ipython3
geojson = leafmap.gdf_to_geojson(gdf, epsg="4326")
# geojson
```

One can provide a list of colors (`fill_colors`) to randomly fill the polygons.

```{code-cell} ipython3
m = leafmap.Map()
m.add_gdf(gdf, layer_name="New York boroughs", fill_colors=["red", "green", "blue"])
m
```

![](https://i.imgur.com/lfAkjdt.gif)
