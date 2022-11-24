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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/30_census_data.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/30_census_data.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Get the Census data WMS tiles as a dictionary. More info can be found at https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_wms.html

```{code-cell} ipython3
census_data_dict = leafmap.get_census_dict()
```

Print out the list of US Census WMS.

```{code-cell} ipython3
for key in census_data_dict:
    print(key)
```

Get the list of layers for a WMS.

```{code-cell} ipython3
census_data_dict['Census 2020']['layers']
```

Create an interactive map and add Census data layer to it. You might need to zoom in to see the data layer

```{code-cell} ipython3
m = leafmap.Map()
m.add_census_data(wms="Census 2020", layer="States")
m.add_census_data(wms="Census 2020", layer="States_Labels49388")
m
```

Alternatively, you can use the toolbar to load Census data interactively without coding.

![](https://i.imgur.com/nww2R1l.gif)
