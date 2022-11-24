---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/04_cog_mosaic.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/04_cog_mosaic.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Creating a virtual mosaic of Cloud Optimized GeoTIFFs (COG)**


**Important Note:** This notebook no longer works. The `add_cog_mosaic()` has been removed from leafmap. See https://github.com/giswqs/leafmap/issues/180

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
# leafmap.update_package()
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
```

For this demo, we will use data from https://www.maxar.com/open-data/california-colorado-fires for mapping California and Colorado fires. A List of COGs can be found at:

- Pre-event: https://github.com/giswqs/leafmap/blob/master/examples/data/cog_pre_event.txt
- Post-event: https://github.com/giswqs/leafmap/blob/master/examples/data/cog_post_event.txt

```{code-cell} ipython3
pre_fire_url = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cog_pre_event.txt'
```

Create an XYZ tile layer based on a txt file containing a list of COG URLs.

```{code-cell} ipython3
# leafmap.cog_mosaic_from_file(pre_fire_url)
```

```{code-cell} ipython3
post_fire_url = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cog_post_event.txt'
```

```{code-cell} ipython3
# leafmap.cog_mosaic_from_file(post_fire_url)
```

Add a COG mosaic tile layer to the map.

```{code-cell} ipython3
# m.add_cog_mosaic_from_file(pre_fire_url, name="Pre-event", show_footprints=True)  #This line might take a while to run
```

```{code-cell} ipython3
# m.add_cog_mosaic_from_file(post_fire_url, name="Post-event", show_footprints=True)   #This line might take a while to run
```

```{code-cell} ipython3
pre_event_tile = (
    'https://titiler.xyzmosaicjson/anonymous.layer_pqmra/tiles/{z}/{x}/{y}@1x?'
)
m.add_tile_layer(pre_event_tile, name="Pre-event", attribution="Maxar")
```

```{code-cell} ipython3
post_event_tile = (
    'https://titiler.xyzmosaicjson/anonymous.layer_qdano/tiles/{z}/{x}/{y}@1x?'
)
m.add_tile_layer(post_event_tile, name="Post-event", attribution="Maxar")
```

```{code-cell} ipython3
m.set_center(-122.0828, 37.0317, 11)
```

```{code-cell} ipython3
m
```
