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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/14_postgis.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/14_postgis.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Adding data from a PostGIS database to the map**

Setting up the conda env:

```
conda create -n geo python=3.8
conda activate geo
conda install geopandas
conda install mamba -c conda-forge
mamba install leafmap sqlalchemy psycopg2 -c conda-forge
```

Sample dataset:
- [nyc_data.zip](https://github.com/giswqs/postgis/raw/master/data/nyc_data.zip) (Watch this [video](https://youtu.be/fROzLrjNDrs) to load data into PostGIS)

```{code-cell} ipython3
%pip install -q leafmap
```

**Connecting to the database**

```{code-cell} ipython3
import leafmap
```

You can directly pass in the user name and password to access the database. Alternative, you can define environment variables. The default environment variables for user and password are `SQL_USER` and `SQL_PASSWORD`, respectively.

+++

The `try...except...` statements are only used for building the documentation website (https://leafmap.org) because the PostGIS database is not available on GitHub. If you are running the notebook with Jupyter installed locally and PostGIS set up properly, you don't need these `try...except...` statements.

```{code-cell} ipython3
try:
    con = leafmap.connect_postgis(
        database="nyc", host="localhost", user=None, password=None, use_env_var=True
    )
except:
    pass
```

Create a GeoDataFrame from a sql query.

```{code-cell} ipython3
sql = 'SELECT * FROM nyc_neighborhoods'
```

```{code-cell} ipython3
try:
    gdf = leafmap.read_postgis(sql, con)
    display(gdf)
except:
    pass
```

Display the GeoDataFrame on the interactive map. 

```{code-cell} ipython3
try:
    m = leafmap.Map()
    m.add_gdf_from_postgis(
        sql, con, layer_name="NYC Neighborhoods", fill_colors=["red", "green", "blue"]
    )
    display(m)
except:
    pass
```

![](https://i.imgur.com/mAXaBCv.gif)
