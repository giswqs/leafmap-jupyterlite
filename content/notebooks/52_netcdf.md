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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/52_netcdf.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/52_netcdf.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Visualizing NetCDF data**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
# !pip install xarray rioxarray netcdf4 localtileserver
```

```{code-cell} ipython3
import leafmap
```

Download a sample NetCDF dataset.

```{code-cell} ipython3
url = 'https://github.com/giswqs/leafmap/raw/master/examples/data/wind_global.nc'
filename = 'wind_global.nc'
```

```{code-cell} ipython3
leafmap.download_file(url, output=filename)
```

Read the NetCDF dataset.

```{code-cell} ipython3
data = leafmap.read_netcdf(filename)
data
```

Convert the NetCDF dataset to GeoTIFF. Note that the longitude range of the NetCDF dataset is `[0, 360]`. We need to convert it to `[-180, 180]` by setting `shift_lon=True` so that it can be displayed on the map.

```{code-cell} ipython3
tif = 'wind_global.tif'
leafmap.netcdf_to_tif(filename, tif, variables=['u_wind', 'v_wind'], shift_lon=True)
```

Add the GeoTIFF to the map. We can also overlay the country boundary on the map.

```{code-cell} ipython3
geojson = 'https://github.com/giswqs/leafmap/raw/master/examples/data/countries.geojson'
```

```{code-cell} ipython3
m = leafmap.Map(layers_control=True)
m.add_raster(tif, band=[1], palette='coolwarm', layer_name='u_wind')
m.add_geojson(geojson, layer_name='Countries')
m
```

You can also use the `add_netcdf()` function to add the NetCDF dataset to the map without having to convert it to GeoTIFF explicitly.

```{code-cell} ipython3
m = leafmap.Map(layers_control=True)
m.add_netcdf(
    filename,
    variables=['v_wind'],
    palette='coolwarm',
    shift_lon=True,
    layer_name='v_wind',
)
m.add_geojson(geojson, layer_name='Countries')
m
```

Visualizing wind velocity.

```{code-cell} ipython3
m = leafmap.Map(layers_control=True)
m.add_basemap('CartoDB.DarkMatter')
m.add_velocity(filename, zonal_speed='u_wind', meridional_speed='v_wind')
m
```

![](https://i.imgur.com/oL5Mgeu.gif)
