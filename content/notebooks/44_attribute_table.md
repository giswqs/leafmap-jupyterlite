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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/44_attribute_table.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/44_attribute_table.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Add vector data to the map and use the GUI to open attribute table.

```{code-cell} ipython3
m = leafmap.Map()

url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_geojson(
    url,
    layer_name="Countries",
    fill_colors=['red', 'yellow', 'green', 'orange'],
    info_mode=False,
)

in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(in_geojson, layer_name="Cable lines", info_mode=False)

m
```

![](https://i.imgur.com/IIoLVSG.gif)
