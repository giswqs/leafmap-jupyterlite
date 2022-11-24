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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/28_publish_map.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/28_publish_map.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

To follow this tutorial, you will need to [sign up](https://datapane.com/accounts/signup/) for an account with <https://datapane.com>, then install and authenticate the `datapane` Python package. More information can be found [here](https://docs.datapane.com/tutorials/tut-getting-started). 

- `pip install datapane`
- `datapane login`
- `datapane ping`

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

Create an elevation map of North America.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap('USGS 3DEP Elevation')
colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
vmin = 0
vmax = 4000
m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
m
```

Publish the map to [datapane.com](https://datapane.com)

```{code-cell} ipython3
m.publish(name="Elevation Map of North America")
```

Create a land use and land cover map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("NLCD 2016 CONUS Land Cover")
m.add_legend(builtin_legend='NLCD')
m
```

Publish the map to [datapane.com](https://datapane.com).

```{code-cell} ipython3
m.publish(name="National Land Cover Database (NLCD) 2016")
```

Create a world population heat map.

```{code-cell} ipython3
m = leafmap.Map()
in_csv = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv"
m.add_heatmap(
    in_csv,
    latitude="latitude",
    longitude='longitude',
    value="pop_max",
    name="Heat map",
    radius=20,
)
```

```{code-cell} ipython3
colors = ['blue', 'lime', 'red']
vmin = 0
vmax = 10000
m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
m
```

Publish the map to [datapane.com](https://datapane.com).

```{code-cell} ipython3
m.publish(name="World Population Heat Map")
```
