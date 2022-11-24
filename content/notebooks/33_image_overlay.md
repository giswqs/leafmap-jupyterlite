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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/33_image_overlay.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/01_leafmap_intro.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import os
from leafmap import leafmap
```

**Using local files**

Download the sample png from https://i.imgur.com/06Q1fSz.png to your `Downloads` folder.

```{code-cell} ipython3
filepath = '06Q1fSz.png'
if not os.path.exists(filepath):
    leafmap.download_from_url("https://i.imgur.com/06Q1fSz.png", filepath)
```

```{code-cell} ipython3
m = leafmap.Map(center=(25, -115), zoom=4)

image = leafmap.ImageOverlay(url=filepath, bounds=((13, -130), (32, -100)))

m.add_layer(image)
m
```

**Using remote files**

```{code-cell} ipython3
m = leafmap.Map(center=(25, -115), zoom=4)

image = leafmap.ImageOverlay(
    url="https://i.imgur.com/06Q1fSz.png", bounds=((13, -130), (32, -100))
)

m.add_layer(image)
m
```

Update image url

```{code-cell} ipython3
image.url = "https://i.imgur.com/J9qCf4E.png"
```
