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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/43_search_control.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/43_search_control.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Add a search control to the map. See the [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim).

```{code-cell} ipython3
m = leafmap.Map(draw_control=False)
url = "https://nominatim.openstreetmap.org/search?format=json&q={s}"
m.add_search_control(url)
m
```

Search for features in GeoJSON files or any GeoPandas supported vector data.

```{code-cell} ipython3
m = leafmap.Map(draw_control=False, layers_control=True)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_geojson(
    url,
    layer_name="Countries",
    fill_colors=['red', 'yellow', 'green', 'orange'],
    info_mode=None,
)
m
```

![](https://i.imgur.com/LP0BElT.gif)
