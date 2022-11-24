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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/56_download_ned.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/56_download_ned.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Downloading 10-m National Elevation Dataset (NED) with only one line of code**

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install geopandas rasterio
```

```{code-cell} ipython3
import os
import leafmap
import shutil
import sys
```

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4)
m
```

```{code-cell} ipython3
region = m.user_roi_bounds()
if region is None:
    region = [-115.9689, 35.9758, -115.3619, 36.4721]
print(region)
```

```{code-cell} ipython3
leafmap.download_ned(region, return_url=True)
```

```{code-cell} ipython3
out_dir = "data"
os.makedirs(out_dir, exist_ok=True)
```

```{code-cell} ipython3
if "google.colab" in sys.modules:
    leafmap.download_ned(region, out_dir)
```

```{code-cell} ipython3
if "google.colab" in sys.modules:
    mosaic = "mosaic.tif"
    leafmap.mosaic(images=out_dir, output=mosaic)
```

```{code-cell} ipython3
if "google.colab" in sys.modules and (m.user_roi is not None):
    image = 'dem.tif'
    leafmap.clip_image(mosaic, mask=m.user_roi, output=image)
```

```{code-cell} ipython3
out_dir = '/content/drive/MyDrive/Data'
if os.path.exists(out_dir) and os.path.exists(image):
    shutil.copyfile(image, os.path.join(out_dir, image))
```
