---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3.9.12 ('geo')
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/55_lidar.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/55_lidar.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**LiDAR data analysis and visualization with whitebox and leafmap**

Create a new conda env to install required packages:

```bash
conda create -n geo python
conda activate geo
conda install -c conda-forge mamba
mamba install -c conda-forge pygis
pip install laspy[lazrs]
```

Uncomment the following line to install packages in Google Colab.

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install laspy[lazrs]
```

## Import libraries

```{code-cell} ipython3
import os
import leafmap
import whitebox
```

## Set up whitebox

```{code-cell} ipython3
wbt = whitebox.WhiteboxTools()
wbt.set_working_dir(os.getcwd())
wbt.set_verbose_mode(False)
```

## Download sample data

```{code-cell} ipython3
url = 'https://github.com/giswqs/data/raw/main/lidar/madison.laz'
if not os.path.exists('madison.laz'):
    leafmap.download_file(url)
```

## Read LAS/LAZ data

```{code-cell} ipython3
laz = leafmap.read_lidar('madison.laz')
```

```{code-cell} ipython3
laz
```

```{code-cell} ipython3
str(laz.header.version)
```

## Upgrade file version

```{code-cell} ipython3
las = leafmap.convert_lidar(laz, file_version='1.4')
```

```{code-cell} ipython3
str(las.header.version)
```

## Write LAS data

```{code-cell} ipython3
leafmap.write_lidar(las, 'madison.las')
```

+++ {"tags": []}

## Histogram analysis

```{code-cell} ipython3
wbt.lidar_histogram('madison.las', 'histogram.html')
```

## Visualize LiDAR data

```{code-cell} ipython3
leafmap.view_lidar('madison.las')
```

## Remove outliers

```{code-cell} ipython3
wbt.lidar_elevation_slice("madison.las", "madison_rm.las", minz=0, maxz=450)
```

## Visualize LiDAR data after removing outliers

```{code-cell} ipython3
leafmap.view_lidar('madison_rm.las', cmap='terrain')
```

## Create DSM

```{code-cell} ipython3
wbt.lidar_digital_surface_model(
    'madison_rm.las', 'dsm.tif', resolution=1.0, minz=0, maxz=450
)
```

```{code-cell} ipython3
:jp-MarkdownHeadingCollapsed: true
:tags: []

leafmap.add_crs("dsm.tif", epsg=2255)
```

## Visualize DSM

```{code-cell} ipython3
m = leafmap.Map()
m.add_raster('dsm.tif', palette='terrain', layer_name='DSM')
m
```

## Create DEM

```{code-cell} ipython3
wbt.remove_off_terrain_objects('dsm.tif', 'dem.tif', filter=25, slope=15.0)
```

## Visualize DEM

```{code-cell} ipython3
m.add_raster('dem.tif', palette='terrain', layer_name='DEM')
m
```

## Create CHM

```{code-cell} ipython3
chm = wbt.subtract('dsm.tif', 'dem.tif', 'chm.tif')
```

```{code-cell} ipython3
m.add_raster('chm.tif', palette='gist_earth', layer_name='CHM')
m
```
