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

**Using timeseries inspector with a single click**


```{code-cell} ipython3
%pip install -q leafmap
```

This notebook requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
import os
from leafmap import leafmap
```

```{code-cell} ipython3
# leafmap.update_package()
```

First, you need to sign up a Planet account and get an API key. See https://developers.planet.com/quickstart/apis.
Uncomment the following line to pass in your API key.

```{code-cell} ipython3
# os.environ["PLANET_API_KEY"] = "12345"
```

Create a list of Planet monthly mosaic tile layers.

```{code-cell} ipython3
monthly_tiles = leafmap.planet_monthly_tiles()
```

Use the timeseries inspector to visualize images side by side with a split-panel map.

```{code-cell} ipython3
leafmap.ts_inspector(monthly_tiles)
```

Create a list of Planet quarterly mosaic tile layers.

```{code-cell} ipython3
quarterly_tiles = leafmap.planet_quarterly_tiles()
```

Use the timeseries inspector to visualize images side by side with a split-panel map.

```{code-cell} ipython3
leafmap.ts_inspector(quarterly_tiles)
```

Create a list of Planet quarterly and monthly mosaic tile layers.

```{code-cell} ipython3
tiles = leafmap.planet_tiles()
```

Use the timeseries inspector to visualize images side by side with a split-panel map.

```{code-cell} ipython3
leafmap.ts_inspector(tiles)
```

Use the toolbar GUI to activate the timeseries inspector.

```{code-cell} ipython3
m = leafmap.Map()
m
```

![](https://i.imgur.com/cEilgvb.gif)
