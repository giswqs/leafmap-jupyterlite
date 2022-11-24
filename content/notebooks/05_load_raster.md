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

**Loading local raster datasets with leafmap**


```{code-cell} ipython3
%pip install -q leafmap
```

To follow this tutorial, you need to install the [leafmap](https://leafmap.org) and [xarray_leaflet](https://github.com/davidbrochart/xarray_leaflet) Python packages. Use the following conda commands to create a conda env and install packages. Note that `xarray_leaflet` does not work properly on Windows ([source](https://github.com/davidbrochart/xarray_leaflet/issues/30)). Also, the `add_raster` function is only available for the ipyleaflet plotting backend. Therefore, Google Colab is not supported. Use the binder link above instead.  

- `conda create -n gee python`
- `conda activate gee`
- `conda install mamba -c conda-forge`
- `mamba install leafmap xarray_leaflet -c conda-forge`

+++

Use the ipyleaflet plotting backend. The folium plotting backend does not support the `add_raster` function.

```{code-cell} ipython3
import os
import leafmap.leafmap as leafmap
```

Specify input raster datasets

```{code-cell} ipython3
out_dir = os.path.expanduser('~/Downloads')

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

landsat = os.path.join(out_dir, 'landsat.tif')
dem = os.path.join(out_dir, 'dem.tif')
```

Download samples raster datasets

More datasets can be downloaded from https://viewer.nationalmap.gov/basic/

```{code-cell} ipython3
if not os.path.exists(landsat):
    landsat_url = 'https://drive.google.com/file/d/1EV38RjNxdwEozjc9m0FcO3LFgAoAX1Uw/view?usp=sharing'
    leafmap.download_from_gdrive(landsat_url, 'landsat.tif', out_dir, unzip=False)
```

```{code-cell} ipython3
if not os.path.exists(dem):
    dem_url = 'https://drive.google.com/file/d/1vRkAWQYsLWCi6vcTMk8vLxoXMFbdMFn8/view?usp=sharing'
    leafmap.download_from_gdrive(dem_url, 'dem.tif', out_dir, unzip=False)
```

Create an interactive map

```{code-cell} ipython3
Map = leafmap.Map()
```

Add local raster datasets to the map

More colormap can be found at https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

```{code-cell} ipython3
Map.add_raster(dem, colormap='terrain', layer_name='DEM')
```

```{code-cell} ipython3
Map.add_raster(landsat, bands=[5, 4, 3], layer_name='Landsat')
```

Display the map

```{code-cell} ipython3
Map
```
