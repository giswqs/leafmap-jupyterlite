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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/34_add_points_from_xy.ipynb)
<a href="https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/34_add_points_from_xy.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
import pandas as pd
```

```{code-cell} ipython3
# leafmap.update_package()
```

Using a CSV file containing xy coordinates

```{code-cell} ipython3
m = leafmap.Map()
data = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
m.add_points_from_xy(data, x="longitude", y="latitude")
m
```

Using a Pandas DataFrame containing xy coordinates.

```{code-cell} ipython3
m = leafmap.Map()
data = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
df = pd.read_csv(data)
m.add_points_from_xy(df, x="longitude", y="latitude")
m
```

```{code-cell} ipython3

```
