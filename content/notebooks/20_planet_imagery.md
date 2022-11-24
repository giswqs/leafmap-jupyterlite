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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/20_planet_imagery.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/20_planet_imagery.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding Planet global monthly and quarterly mosaic**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import os
import leafmap
```

First, you need to sign up a Planet account and get an API key. See https://developers.planet.com/quickstart/apis.
Uncomment the following line to pass in your API key.

```{code-cell} ipython3
# os.environ["PLANET_API_KEY"] = "12345"
```

Determine the tile format based on the plotting backend being use. It can be either ipyleaflet or folium.

```{code-cell} ipython3
tile_format = "ipyleaflet"

if os.environ.get("USE_MKDOCS") is not None:
    tile_format = "folium"
```

Generate Planet quarterly imagery URLs.

```{code-cell} ipython3
# leafmap.planet_quarterly()
```

Generate Planet monthly imagery URLs.

```{code-cell} ipython3
# leafmap.planet_monthly()
```

Generates Planet bi-annual and monthly imagery URLs.

```{code-cell} ipython3
# leafmap.planet_catalog()
```

Generate Planet quarterly imagery TileLayer.

```{code-cell} ipython3
quarterly_tiles = leafmap.planet_quarterly_tiles(tile_format=tile_format)
```

Generate Planet monthly imagery TileLayer.

```{code-cell} ipython3
monthly_tiles = leafmap.planet_monthly_tiles(tile_format=tile_format)
```

Print out the quarterly tile URLs.

```{code-cell} ipython3
for tile in quarterly_tiles:
    print(tile)
```

Print out the monthly tile URLs.

```{code-cell} ipython3
for tile in monthly_tiles:
    print(tile)
```

Add a Planet monthly mosaic by specifying year and month.

```{code-cell} ipython3
m = leafmap.Map()
m.add_planet_by_month(year=2020, month=8)
m
```

Add a Planet quarterly mosaic by specifying year and quarter.

```{code-cell} ipython3
m = leafmap.Map()
m.add_planet_by_quarter(year=2019, quarter=2)
m
```
