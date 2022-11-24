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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/58_bokeh.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/58_bokeh.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install bokeh jupyter_bokeh
```

```{code-cell} ipython3
import leafmap.bokehmap as leafmap
```

Create an interactive map

```{code-cell} ipython3
m = leafmap.Map()
m
```

Specify center and zoom level

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4, height=400)
m
```

Add basemaps

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap('OpenTopoMap')
m
```

```{code-cell} ipython3
# print(leafmap.basemaps.keys())
```

Add COG

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'
m.add_cog_layer(url)
m
```

Add STAC

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
m.add_stac_layer(url, bands=['B3', 'B2', 'B1'], name='False color')
m
```

Add local raster datasets

```{code-cell} ipython3
url = 'https://github.com/giswqs/data/raw/main/raster/srtm90.tif'
leafmap.download_file(url, 'dem.tif')
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_raster('dem.tif', palette='terrain')
m
```

Add points

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://github.com/giswqs/leafmap/blob/master/examples/data/us_cities.geojson'
m.add_geojson(url, size=10, color='blue', alpha=0.7)
m
```

Add lines

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap('CartoDB.DarkMatter')
url = 'https://github.com/giswqs/leafmap/raw/master/examples/data/cable_geo.geojson'
m.add_vector(url, line_color='color', line_width=2)
m
```

Add polygons

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://github.com/giswqs/leafmap/blob/master/examples/data/countries.geojson'
m.add_vector(url, fill_alpha=0.5, fill_color='lightblue')
m
```
