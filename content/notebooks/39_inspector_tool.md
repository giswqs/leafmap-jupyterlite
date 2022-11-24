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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/39_inspector_tool.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/39_inspector_tool.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
```

Add Cloud Optimized GeoTIFF (COG) from [Planetary Computer](https://planetarycomputer.microsoft.com/catalog).

```{code-cell} ipython3
collection = "landsat-8-c2-l2"
item = "LC08_L2SP_047027_20201204_02_T1"
```

```{code-cell} ipython3
m.add_stac_layer(
    collection=collection,
    item=item,
    assets="SR_B7,SR_B5,SR_B4",
    name="Landsat Band-754",
)
```

```{code-cell} ipython3
m.add_stac_layer(
    collection=collection,
    item=item,
    assets="SR_B5,SR_B4,SR_B3",
    name="Landsat Band-543",
)
```

```{code-cell} ipython3
m
```

![](https://i.imgur.com/Idfx767.gif)
