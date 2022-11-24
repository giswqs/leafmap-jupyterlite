---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3.9.13 ('geo')
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/02_using_basemaps.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/02_using_basemaps.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Using basemaps in leafmap**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m
```

Specify a Google basemap to use, can be one of ["ROADMAP", "TERRAIN", "SATELLITE", "HYBRID"].

```{code-cell} ipython3
m = leafmap.Map(google_map="HYBRID")
m
```

```{code-cell} ipython3
m = leafmap.Map(google_map="TERRAIN")
m
```

Add a basemap using the `add_basemap()` function.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("HYBRID")
m.add_basemap("Esri.NatGeoWorldMap")
m
```

Add an XYZ tile layer.

```{code-cell} ipython3
m = leafmap.Map()
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m
```

Add a WMS tile layer.

```{code-cell} ipython3
m = leafmap.Map()
naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
m.add_wms_layer(
    url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True
)
m
```

Add a legend to the map.

```{code-cell} ipython3
m = leafmap.Map(google_map="HYBRID")

url1 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?"
m.add_wms_layer(
    url1, layers="1", format='image/png', transparent=True, name="NWI Wetlands Vector"
)

url2 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands_Raster/ImageServer/WMSServer?"
m.add_wms_layer(
    url2, layers="0", format='image/png', transparent=True, name="NWI Wetlands Raster"
)

m.add_legend(builtin_legend="NWI")
m
```

Add a layer from [xyzservices](https://github.com/geopandas/xyzservices) provider object

```{code-cell} ipython3
import os
import xyzservices.providers as xyz
```

```{code-cell} ipython3
basemap = xyz.HEREv3.basicMap
basemap
```

Pass the api key to the xyzservices provider object or set it as an environment variable.

```{code-cell} ipython3
basemap['apiKey'] = os.environ["HEREMAPS_API_KEY"]
```

Add the xyzservices provider object as a layer to the map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap(basemap)
m
```
