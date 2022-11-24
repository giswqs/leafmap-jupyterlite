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

+++ {"id": "1CFzMrw5zmzc"}

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/01_leafmap_intro.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/01_leafmap_intro.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Introducing the leafmap Python package for interactive mapping**


```{code-cell} ipython3

%pip install -q leafmap
```

`leafmap` has four plotting backends: [folium](https://github.com/python-visualization/folium), [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet), [here-map](https://github.com/heremaps/here-map-widget-for-jupyter), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter). Note that the backends do not offer equal functionality. Some interactive functionality in `ipyleaflet` might not be available in other plotting backends. To use a specific plotting backend, use one of the following:

- `import leafmap.leafmap as leafmap`
- `import leafmap.foliumap as leafmap`
- `import leafmap.heremap as leafmap`
- `import leafmap.kepler as leafmap`

```{code-cell} ipython3

import leafmap
```

Create an interactive map. 

```{code-cell} ipython3

m = leafmap.Map()
m
```

Specify the default map center and zoom level.

```{code-cell} ipython3

m = leafmap.Map(center=[50, 19], zoom=4)  # center=[lat, lon]
m
```

Set the visibility of map controls.

```{code-cell} ipython3

m = leafmap.Map(
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True,
)
m
```

Change the map width and height.

```{code-cell} ipython3

m = leafmap.Map(height="450px", width="800px")
m
```

Use the `ipyleaflet` plotting backend.

```{code-cell} ipython3
import leafmap.leafmap as leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
m
```

Use the `folium` plotting backend.

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
m
```
