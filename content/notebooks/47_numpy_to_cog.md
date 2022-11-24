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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/47_numpy_to_cog.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/47_numpy_to_cog.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

Create a fresh conda env to run this example if needed.

```
conda create -n cog python=3.9
conda install mamba -c conda-forge
mamba install leafmap rio-cogeo -c conda-forge
```

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install rio-cogeo
```

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
url = 'https://github.com/giswqs/leafmap/raw/master/examples/data/cog.tif'
in_cog = 'cog.tif'
out_cog = "ndvi.tif"
```

Download a sample dataset.

```{code-cell} ipython3
leafmap.download_from_url(url, in_cog)
```

Convert image to numpy array.

```{code-cell} ipython3
arr = leafmap.image_to_numpy(in_cog)
```

```{code-cell} ipython3
arr.shape
```

Computer NDVI.

```{code-cell} ipython3
ndvi = (arr[3] - arr[0]) / (arr[3] + arr[0])
```

```{code-cell} ipython3
ndvi.shape
```

Convert numpy array to COG.

```{code-cell} ipython3
leafmap.numpy_to_cog(ndvi, out_cog, profile=in_cog)
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_raster(in_cog, band=[4, 1, 2], layer_name="Color infrared")
m.add_raster(out_cog, palette="Greens", layer_name="NDVI")
m
```

![](https://i.imgur.com/OVaTyP3.gif)
