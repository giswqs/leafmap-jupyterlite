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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/08_whitebox.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/08_whitebox.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Using WhiteboxTools with leafmap**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import os
import leafmap
```

Download a sample DEM dataset.

```{code-cell} ipython3
out_dir = os.path.expanduser('~/Downloads')
dem = os.path.join(out_dir, 'dem.tif')

if not os.path.exists(dem):
    dem_url = 'https://drive.google.com/file/d/1vRkAWQYsLWCi6vcTMk8vLxoXMFbdMFn8/view?usp=sharing'
    leafmap.download_from_gdrive(dem_url, 'dem.tif', out_dir, unzip=False)
```

Create an interactive map.

```{code-cell} ipython3
Map = leafmap.Map()
Map
```

Use the built-in toolbox to perform geospatial analysis. For example, you can perform depression filling using the sample DEM dataset downloaded in the above step.

+++

![](https://i.imgur.com/KGHly63.png)

+++

Display the toolbox using the default mode.

```{code-cell} ipython3
leafmap.whiteboxgui()
```

Display the toolbox using the collapsible tree mode. Note that the tree mode does not support Google Colab. 

```{code-cell} ipython3
leafmap.whiteboxgui(tree=True)
```

Perform geospatial analysis using the [whitebox](https://github.com/giswqs/whitebox-python) package. 

```{code-cell} ipython3
import os
import pkg_resources
```

```{code-cell} ipython3
wbt = leafmap.WhiteboxTools()
wbt.verbose = False
```

```{code-cell} ipython3
# identify the sample data directory of the package
data_dir = os.path.dirname(pkg_resources.resource_filename("whitebox", 'testdata/'))
wbt.set_working_dir(data_dir)

wbt.feature_preserving_smoothing("DEM.tif", "smoothed.tif", filter=9)
wbt.breach_depressions("smoothed.tif", "breached.tif")
```
