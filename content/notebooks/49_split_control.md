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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/49_split_control.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/49_split_control.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating a split-panel map**

This notebook demonstrates how to add a split-panel map with leafmap anf folium. It also supports streamlit. Note that the ipyleaflet SplitControl does not support streamlit. 


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import folium
import leafmap.foliumap as leafmap
```

The split-panel map requires two layers: `left_layer` and `right_layer`. The layer instance can be a string representing a basemap, or an HTTP URL to a Cloud Optimized GeoTIFF (COG), or a folium TileLayer instance. 

**Using basemaps**

```{code-cell} ipython3
m = leafmap.Map(height=500)
m.split_map(left_layer='TERRAIN', right_layer='OpenTopoMap')
m
```

Show available basemaps.

```{code-cell} ipython3
# leafmap.basemaps.keys()
```

**Using COG**

```{code-cell} ipython3
m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
url2 = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'
m.split_map(url, url2)
m
```

**Using folium TileLayer**

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4)

url1 = 'https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2001_Land_Cover_L48/wms?'
url2 = 'https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms?'

left_layer = folium.WmsTileLayer(
    url=url1,
    layers='NLCD_2001_Land_Cover_L48',
    name='NLCD 2001',
    attr='MRLC',
    fmt="image/png",
    transparent=True,
)
right_layer = folium.WmsTileLayer(
    url=url2,
    layers='NLCD_2019_Land_Cover_L48',
    name='NLCD 2019',
    attr='MRLC',
    fmt="image/png",
    transparent=True,
)

m.split_map(left_layer, right_layer)
m
```
