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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/37_planetary_computer.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/37_planetary_computer.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Add a STAC item via an HTTP URL

```{code-cell} ipython3
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
```

```{code-cell} ipython3
leafmap.stac_assets(url)
```

```{code-cell} ipython3
leafmap.stac_bounds(url)
```

```{code-cell} ipython3
leafmap.stac_center(url)
```

```{code-cell} ipython3
# leafmap.stac_info(url)
```

```{code-cell} ipython3
# leafmap.stac_stats(url)
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(url, bands=["B3", "B2", "B1"])
m
```

Add a Microsoft Planetry Computer STAC item. The titiler endpoint can set in one of the ways below:

```
os.environ["TITILER_ENDPOINT"] = "planetary-computer"
titiler_endpoint="pc"
titiler_endpoint="planetary-computer"
```

```{code-cell} ipython3
# import os
# os.environ["TITILER_ENDPOINT"] = "planetary-computer"
```

```{code-cell} ipython3
collection = "landsat-8-c2-l2"
```

```{code-cell} ipython3
item = "LC08_L2SP_047027_20201204_02_T1"
```

```{code-cell} ipython3
leafmap.stac_assets(collection=collection, item=item, titiler_endpoint="pc")
```

```{code-cell} ipython3
leafmap.stac_bounds(collection=collection, item=item)
```

```{code-cell} ipython3
leafmap.stac_info(collection=collection, item=item, assets="SR_B7")
```

```{code-cell} ipython3
leafmap.stac_stats(collection=collection, item=item, assets="SR_B7")
```

Color infrared composite.

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(
    collection=collection,
    item=item,
    assets=["SR_B5", "SR_B4", "SR_B3"],
    name="Color infrared",
)
m
```

False color composite.

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(
    collection=collection, item=item, assets="SR_B7,SR_B5,SR_B4", name="False color"
)
m
```

Calculate NDVI.

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(
    collection=collection,
    item=item,
    expression="(SR_B5-SR_B4)/(SR_B5+SR_B4)",
    rescale="-1,1",
    name="NDVI",
)
m
```

Calculate NDVI and add a colormap. See available colormaps at https://planetarycomputer.microsoft.com/docs/reference/data/

```{code-cell} ipython3
m = leafmap.Map()
m.add_stac_layer(
    collection=collection, item=item, assets="SR_B5,SR_B4,SR_B3", name="Color infrared"
)
m.add_stac_layer(
    collection=collection,
    item=item,
    expression="(SR_B5-SR_B4)/(SR_B5+SR_B4)",
    rescale="-1,1",
    colormap_name="greens",
    name="NDVI Green",
)
m
```
