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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/06_legend.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/06_legend.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding custom legends to the map**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

List available built-in legends.

```{code-cell} ipython3
legends = leafmap.builtin_legends
for legend in legends:
    print(legend)
```

National Land Cover Database (NLCD)

https://developers.google.com/earth-engine/datasets/catalog/USGS_NLCD

+++

Create an interactive map.

```{code-cell} ipython3
Map = leafmap.Map()
```

Add a WMS layer and built-in legend to the map.

```{code-cell} ipython3
url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?"
Map.add_wms_layer(
    url,
    layers="NLCD_2016_Land_Cover_L48",
    name="NLCD 2016 CONUS Land Cover",
    format="image/png",
    transparent=True,
)
Map.add_legend(builtin_legend='NLCD')

Map
```

Add National Wetlands Inventory to the map.

```{code-cell} ipython3
Map = leafmap.Map(google_map="HYBRID")

url1 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?"
Map.add_wms_layer(
    url1, layers="1", format='image/png', transparent=True, name="NWI Wetlands Vector"
)

url2 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands_Raster/ImageServer/WMSServer?"
Map.add_wms_layer(
    url2, layers="0", format='image/png', transparent=True, name="NWI Wetlands Raster"
)

Map.add_legend(builtin_legend="NWI")
Map
```

**Add custom legends**

There are two ways you can add custom legends:

1. Define legend labels and colors
2. Define legend dictionary

Define legend keys and colors

```{code-cell} ipython3
Map = leafmap.Map()

labels = ['One', 'Two', 'Three', 'Four', 'ect']
# color can be defined using either hex code or RGB (0-255, 0-255, 0-255)
colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3']
# colors = [(255, 0, 0), (127, 255, 0), (127, 18, 25), (36, 70, 180), (96, 68, 123)]

Map.add_legend(title='Legend', labels=labels, colors=colors)
Map
```

Define a legend dictionary.

```{code-cell} ipython3
Map = leafmap.Map()

url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?"
Map.add_wms_layer(
    url,
    layers="NLCD_2016_Land_Cover_L48",
    name="NLCD 2016 CONUS Land Cover",
    format="image/png",
    transparent=True,
)

legend_dict = {
    '11 Open Water': '466b9f',
    '12 Perennial Ice/Snow': 'd1def8',
    '21 Developed, Open Space': 'dec5c5',
    '22 Developed, Low Intensity': 'd99282',
    '23 Developed, Medium Intensity': 'eb0000',
    '24 Developed High Intensity': 'ab0000',
    '31 Barren Land (Rock/Sand/Clay)': 'b3ac9f',
    '41 Deciduous Forest': '68ab5f',
    '42 Evergreen Forest': '1c5f2c',
    '43 Mixed Forest': 'b5c58f',
    '51 Dwarf Scrub': 'af963c',
    '52 Shrub/Scrub': 'ccb879',
    '71 Grassland/Herbaceous': 'dfdfc2',
    '72 Sedge/Herbaceous': 'd1d182',
    '73 Lichens': 'a3cc51',
    '74 Moss': '82ba9e',
    '81 Pasture/Hay': 'dcd939',
    '82 Cultivated Crops': 'ab6c28',
    '90 Woody Wetlands': 'b8d9eb',
    '95 Emergent Herbaceous Wetlands': '6c9fb8',
}

Map.add_legend(title="NLCD Land Cover Classification", legend_dict=legend_dict)
Map
```
