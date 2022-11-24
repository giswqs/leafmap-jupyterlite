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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/48_lidar.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/48_lidar.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Visualizing LiDAR data in 3D with only one line of code**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install leafmap[lidar] open3d
```

```{code-cell} ipython3
import os
import leafmap
```

Download a [sample LiDAR dataset](https://drive.google.com/file/d/1H_X1190vL63BoFYa_cVBDxtIa8rG-Usb/view?usp=sharing) from Google Drive. The zip file is 52.1 MB and the uncompressed LAS file is 109 MB.

```{code-cell} ipython3
url = (
    'https://github.com/giswqs/data/raw/main/lidar/madison.zip'
)
filename = 'madison.las'
```

```{code-cell} ipython3
if not os.path.exists(filename):
    leafmap.download_file(url, 'madison.zip', unzip=True)
```

Read the LiDAR data

```{code-cell} ipython3
las = leafmap.read_lidar(filename)
```

The LAS header.

```{code-cell} ipython3
las.header
```

The number of points.

```{code-cell} ipython3
las.header.point_count
```

The list of features.

```{code-cell} ipython3
list(las.point_format.dimension_names)
```

Inspect data.

```{code-cell} ipython3
las.X
```

```{code-cell} ipython3
las.Y
```

```{code-cell} ipython3
las.Z
```

```{code-cell} ipython3
las.intensity
```

Visualize LiDAR data using the [pyvista](https://github.com/pyvista/pyvista) backend. 

```{code-cell} ipython3
# leafmap.view_lidar(filename, cmap='terrain', backend='pyvista')
```

![](https://i.imgur.com/xezcgMP.gif)

+++

Visualize LiDAR data using the [ipygany](https://github.com/QuantStack/ipygany) backend.

```{code-cell} ipython3
# leafmap.view_lidar(filename, backend='ipygany', background='white')
```

![](https://i.imgur.com/MyMWW4I.gif)

+++

Visualize LiDAR data using the [panel](https://github.com/holoviz/panel) backend.

```{code-cell} ipython3
# leafmap.view_lidar(filename, cmap='terrain', backend='panel', background='white')
```

![](https://i.imgur.com/XQGWbJk.gif)

+++

Visualize LiDAR data using the [open3d](http://www.open3d.org) backend. 

```{code-cell} ipython3
# leafmap.view_lidar(filename, backend='open3d')
```

![](https://i.imgur.com/rL85fbl.gif)
