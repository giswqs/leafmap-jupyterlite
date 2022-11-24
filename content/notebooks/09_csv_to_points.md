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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/09_csv_to_points.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/09_csv_to_points.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Converting CSV to points**


```{code-cell} ipython3
%pip install -q leafmap
```

This notebook example requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
import os
import leafmap.leafmap as leafmap
```

Read a CSV as a Pandas DataFrame.

```{code-cell} ipython3
in_csv = 'https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv'
```

```{code-cell} ipython3
df = leafmap.csv_to_df(in_csv)
df
```

Create a point layer from a CSV file containing lat/long information.

```{code-cell} ipython3
Map = leafmap.Map()
Map.add_xy_data(in_csv, x="longitude", y="latitude", layer_name="World Cities")
Map
```

Set the output directory.

```{code-cell} ipython3
out_dir = os.path.expanduser('~/Downloads')
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
out_shp = os.path.join(out_dir, 'world_cities.shp')
```

Convert a CSV file containing lat/long information to a shapefile.

```{code-cell} ipython3
leafmap.csv_to_shp(in_csv, out_shp)
```

```{code-cell} ipython3
out_geojson = os.path.join(out_dir, 'world_cities.geojson')
leafmap.csv_to_geojson(in_csv, out_geojson)
```

Convert a CSV file containing lat/long information to a GeoPandas GeoDataFrame.

```{code-cell} ipython3
# gdf = leafmap.csv_to_gdf(in_csv)
# gdf
```
