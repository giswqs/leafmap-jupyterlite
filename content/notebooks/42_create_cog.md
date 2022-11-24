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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/42_create_cog.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/42_create_cog.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Provide a dataset path or URL.

```{code-cell} ipython3
url = "https://github.com/giswqs/data/raw/main/raster/srtm90.tif"
```

Validate COG.

```{code-cell} ipython3
leafmap.cog_validate(url)
```

```{code-cell} ipython3
leafmap.cog_validate(url, verbose=True)
```

Convert the image to tiled COG.

```{code-cell} ipython3
out_cog = "cog.tif"
leafmap.image_to_cog(url, out_cog)
```

Validate COG.

```{code-cell} ipython3
leafmap.cog_validate(out_cog)
```

```{code-cell} ipython3
leafmap.cog_validate(out_cog, verbose=True)
```

Add COG to map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_raster(out_cog, palette="terrain", layer_name="Local COG")
m.add_cog_layer(url, palette="gist_earth", name="Remote COG")
m
```
