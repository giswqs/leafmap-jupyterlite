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

[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Using local raster datasets or remote Cloud Optimized GeoTIFFs (COG) with leafmap**

Uncomment the following line to install [leafmap](https://leafmap.org) and [localtileserver](https://github.com/banesullivan/localtileserver) if needed.

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install localtileserver
```

```{code-cell} ipython3
import os
import leafmap
```

Specify input raster datasets

```{code-cell} ipython3
out_dir = os.path.expanduser('~/Downloads')
dem = os.path.join(out_dir, 'dem.tif')
landsat = os.path.join(out_dir, 'landsat.tif')
```

Download samples raster datasets.

```{code-cell} ipython3
if not os.path.exists(dem):
    dem_url = 'https://drive.google.com/file/d/1vRkAWQYsLWCi6vcTMk8vLxoXMFbdMFn8/view?usp=sharing'
    leafmap.download_from_gdrive(dem_url, dem, out_dir, unzip=False)
```

```{code-cell} ipython3
if not os.path.exists(landsat):
    landsat_url = 'https://github.com/giswqs/leafmap/raw/master/examples/data/cog.tif'
    leafmap.download_from_url(landsat_url, landsat, out_dir, unzip=False)
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
```

Add local raster datasets to the map. The available palettes can be found at https://jiffyclub.github.io/palettable/

```{code-cell} ipython3
m.add_raster(landsat, band=[4, 3, 2], layer_name="Landsat")
```

```{code-cell} ipython3
m.add_raster(dem, palette='viridis', layer_name="DEM")
```

```{code-cell} ipython3
m
```

Add a remote Cloud Optimized GeoTIFF(COG) to the map.

```{code-cell} ipython3
m = leafmap.Map()
```

```{code-cell} ipython3
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
```

```{code-cell} ipython3
m.add_cog_layer(url, name="CA Fire")
```

```{code-cell} ipython3
m
```

![](https://i.imgur.com/dy6LSq5.gif)
