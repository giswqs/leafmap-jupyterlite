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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/54_plot_raster.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/54_plot_raster.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import os
import leafmap
```

Download a sample dataset.

```{code-cell} ipython3
url = 'https://github.com/giswqs/data/raw/main/raster/srtm90.tif'
```

```{code-cell} ipython3
image = 'srtm90.tif'
if not os.path.exists(image):
    leafmap.download_file(url, image)
```

Plot the raster image in 2D.

```{code-cell} ipython3
leafmap.plot_raster(image, cmap='terrain', figsize=(15, 10))
```

![](https://i.imgur.com/oDoivba.png)

+++

Plot the raster image in 3D.

```{code-cell} ipython3
leafmap.plot_raster_3d('srtm90.tif', factor=2, cmap='terrain', background='gray')
```

![](https://i.imgur.com/UQDbV2G.gif)
