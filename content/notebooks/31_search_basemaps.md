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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/31_search_basemaps.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/31_search_basemaps.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Search xyz tiles from [xyzservices](https://github.com/geopandas/xyzservices). 

```{code-cell} ipython3
leafmap.search_xyz_services(keyword="esri")
```

Add an xyz tile to the map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_xyz_service("xyz.Esri.NatGeoWorldMap")
m
```

Search xyz tiles from [Quick Map Services](https://github.com/nextgis/quickmapservices).

```{code-cell} ipython3
leafmap.search_qms(keyword="google")
```

Add xyz tile to the map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_xyz_service("qms.Google Satellite Hybrid")
m
```

Search basemaps interactively without coding.

+++

![](https://i.imgur.com/WSxnAKY.gif)
