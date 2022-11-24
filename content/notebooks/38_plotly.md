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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/38_plotly.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/38_plotly.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.plotlymap as leafmap
```

If you run into an error saying "FigureWidget - 'mapbox._derived' Value Error" ([source](https://github.com/plotly/plotly.py/issues/2570#issuecomment-738735816)), uncomment the following line and run it. 

```{code-cell} ipython3
# leafmap.fix_widget_error()
```

Create an interactive map using default settings.

```{code-cell} ipython3
m = leafmap.Map()
m
```

Change default setting when creating a map. 

 Can be one of string from "open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner" or "stamen-watercolor" . 

```{code-cell} ipython3
m = leafmap.Map(center=(40, -100), zoom=3, basemap="stamen-terrain", height=500)
m
```

Set map center and zoom level.

```{code-cell} ipython3
m = leafmap.Map(basemap="stamen-watercolor")
m.set_center(lat=20, lon=0, zoom=2)
m
```

Print out available basemaps.

```{code-cell} ipython3
leafmap.basemaps.keys()
```

Add a basemap.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m
```

Add XYZ tile layer.

```{code-cell} ipython3
m = leafmap.Map()
tile_url = "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"
m.add_tile_layer(tile_url, name="Google Satellite", attribution="Google", opacity=1.0)
m
```

Add a mapbox tile layer. You will need a mapbox token. The map style can be Can be "basic", "streets", "outdoors", "light", "dark", "satellite", or "satellite-streets". 

```{code-cell} ipython3
import os
```

```{code-cell} ipython3
# os.environ["MAPBOX_TOKEN"] = "your-mapbox-token"
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_mapbox_layer(style="streets")
m
```

Remove the modebar in the upper-right corner.

```{code-cell} ipython3
m = leafmap.Map(basemap="stamen-toner")
m
```

```{code-cell} ipython3
m.clear_controls()
```

Add more buttons to the modebar.

```{code-cell} ipython3
m = leafmap.Map(basemap="carto-positron")
controls = [
    'drawline',
    'drawopenpath',
    'drawclosedpath',
    'drawcircle',
    'drawrect',
    'eraseshape',
]
m.add_controls(controls)
m
```

Add Cloud Optimized GeoTIFF.

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
m.add_cog_layer(url, name="Fire (pre-event)")
m
```

Add a STAC item via HTTP URL.

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
m.add_stac_layer(url, bands=['B3', 'B2', 'B1'], name='False color')
m
```

Add a STAC item from Microsoft Planetary Computer.

```{code-cell} ipython3
collection = "landsat-8-c2-l2"
item = "LC08_L2SP_047027_20201204_02_T1"
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(
    collection=collection,
    item=item,
    bands=["SR_B7", "SR_B5", "SR_B4"],
    titiler_endpoint="pc",
)
m
```

Add a heat map.

```{code-cell} ipython3
url = 'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv'
```

```{code-cell} ipython3
m = leafmap.Map(basemap="stamen-terrain")
m.add_heatmap(
    url, latitude="Latitude", longitude="Longitude", z="Magnitude", name="Earthquake"
)
m
```

Add a choropleth map.

```{code-cell} ipython3
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
```

```{code-cell} ipython3
m = leafmap.Map(basemap="stamen-terrain")
m.add_choropleth_map(url, name="Pop", z="POP_EST", colorscale="Viridis")
m
```
