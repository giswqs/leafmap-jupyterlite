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

[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating colormaps with a single line of code**


```{code-cell} ipython3
%pip install -q leafmap
```

This notebook requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
from leafmap import leafmap
import leafmap.colormaps as cm
```

Color palette for DEM data.

```{code-cell} ipython3
cm.palettes.dem
```

Show the DEM palette.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.palettes.dem, axis_off=True)
```



+++

Color palette for NDVI data.

```{code-cell} ipython3
cm.palettes.ndvi
```

Show the NDVI palette.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.palettes.ndvi)
```

Specify the number of classes for a palette.

```{code-cell} ipython3
cm.get_palette('terrain', n_class=8)
```

Show the terrain palette with 8 classes.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.get_palette('terrain', n_class=8))
```

Create a palette with custom colors, label, and font size.

```{code-cell} ipython3
cm.plot_colormap(colors=["red", "green", "blue"], label="Temperature", font_size=12)
```

Create a discrete color palette.

```{code-cell} ipython3
cm.plot_colormap(
    colors=["red", "green", "blue"], discrete=True, label="Temperature", font_size=12
)
```

Specify the width and height for the palette.

```{code-cell} ipython3
cm.plot_colormap(
    'terrain',
    label="Elevation",
    width=8.0,
    height=0.4,
    orientation='horizontal',
    vmin=0,
    vmax=1000,
)
```

Change the orentation of the colormap to be vertical.

```{code-cell} ipython3
cm.plot_colormap(
    'terrain',
    label="Elevation",
    width=0.4,
    height=4,
    orientation='vertical',
    vmin=0,
    vmax=1000,
)
```

Add a horizontal colorbar to an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_colormap(
    'terrain',
    label="Elevation",
    width=8.0,
    height=0.4,
    orientation='horizontal',
    vmin=0,
    vmax=4000,
)
m
```

![](https://i.imgur.com/tuB728Y.png)

+++

Add a vertical colorbar to an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_colormap(
    'terrain',
    label="Elevation",
    width=0.4,
    height=4,
    orientation='vertical',
    vmin=0,
    vmax=4000,
)
m
```

Show all available colormaps.

```{code-cell} ipython3
cm.plot_colormaps(width=12, height=0.4)
```
