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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/51_clip_image.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/51_clip_image.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install rasterio fiona
```

```{code-cell} ipython3
import leafmap
```

Download a sample raster dataset.

```{code-cell} ipython3
url = 'https://github.com/giswqs/data/raw/main/raster/srtm90.tif'
dem = 'dem.tif'
```

```{code-cell} ipython3
leafmap.download_file(url, dem, overwrite=True)
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_raster(dem, palette='terrain', layer_name="DEM")
m
```

Define a mask to extract the image. The mask can be a string representing a file path to a vector dataset (e.g., geojson, shp), or a list of coordinates (e.g., `[[lon,lat], [lon,lat]]`), or a dictionary representing a feature (e.g., m.user_roi).

For example, the mask can be a filepath to a vector dataset.

```{code-cell} ipython3
# mask = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/mask.geojson'
```

Or you can draw a polygon on the map, then use `m.user_roi` as the mask.

```{code-cell} ipython3
# mask = m.user_roi
```

Or specify a list of coordinates `[lon, lat]` as the mask.

```{code-cell} ipython3
mask = [
    [-119.679565, 37.256566],
    [-119.679565, 38.061067],
    [-118.24585, 38.061067],
    [-118.24585, 37.256566],
    [-119.679565, 37.256566],
]
```

Specify the output filename.

```{code-cell} ipython3
output = 'clip.tif'
```

Clip image by mask.

```{code-cell} ipython3
leafmap.clip_image(dem, mask, output)
```

Add the clipped image to the map.

```{code-cell} ipython3
m.add_raster(output, palette='gist_earth', layer_name="Clip Image")
```
