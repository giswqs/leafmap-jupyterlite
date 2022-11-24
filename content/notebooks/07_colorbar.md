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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/07_colorbar.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/07_colorbar.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding custom colorbars to the map**


```{code-cell} ipython3
%pip install -q leafmap
```

**Continuous colorbar**

```{code-cell} ipython3
import leafmap
```

Add a WMS layer to the map

```{code-cell} ipython3
Map = leafmap.Map()

url = "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer?"
Map.add_wms_layer(
    url,
    layers="3DEPElevation:Hillshade Elevation Tinted",
    name="USGS 3DEP Elevation",
    format="image/png",
    transparent=True,
)
```

Add a continuous colorbar with a custom palette to the map.

```{code-cell} ipython3
colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
vmin = 0
vmax = 4000

Map.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)

Map
```

**Categorical colorbar**

Add a WMS layer to the map

```{code-cell} ipython3
Map = leafmap.Map()

url = "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer?"
Map.add_wms_layer(
    url,
    layers="3DEPElevation:Hillshade Elevation Tinted",
    name="USGS 3DEP Elevation",
    format="image/png",
    transparent=True,
)
```

Add a categorical colorbar with a custom palette to the map.

```{code-cell} ipython3
colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
vmin = 0
vmax = 4000

Map.add_colorbar(colors=colors, vmin=vmin, vmax=vmax, categorical=True, step=4)
Map
```
