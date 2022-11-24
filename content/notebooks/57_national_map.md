---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3.9.13 ('geo')
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/57_national_map.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/57_national_map.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

### Downloading various shapes from the National Map

The national map (TNM) is a catalog of *topological* datasources maintained by the USGS. 

- It contains a wide range of dataformats (such as GeoTiff, LAZ, ...) and datasets.
- It provides an endpoint that can be used to search for published datasets and files.
- This API supports a wide range of searchable parameters (bounding box, polygon, dates, keyword, ...)
- It returns detailed information regarding the properties of datasets, file,
- as well as various download links (file, thumbnail, xml descriptions, ...).

We've created a thin wrapper to expose this treasure trove. 

- For more details about TNM, see https://apps.nationalmap.gov/tnmaccess/#/
- The same data is also downloable using https://apps.nationalmap.gov/downloader/

```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

### Usage

A class groups the functionalities together.

```{code-cell} ipython3
TNM = leafmap.The_national_map_USGS()
```

### Datasets

```{code-cell} ipython3
TNM.datasets
```

### Formats

Note that any format (f.e. 'All') is specific to one or more datasets.

```{code-cell} ipython3
TNM.prodFormats
```

### Looking for files

```{code-cell} ipython3
TNM.find_details().keys(), TNM.find_details()['total']
```

### A detail

```{code-cell} ipython3
TNM.find_details()['items'][0]
```

### Using parameters

```{code-cell} ipython3
params = {
    'q': 'National Elevation Dataset (NED) 1/3 arc-second',
    'polyCode': '01010002',
    'polyType': 'huc8',
}

TNM.find_details(**params)['total']
```

```{code-cell} ipython3
params = {
    'prodFormats': 'LAS,LAZ',
    'datasets': 'Lidar Point Cloud (LPC)',
    'polygon': [
        (-104.94262695312236, 41.52867510196275),
        (-102.83325195312291, 40.45065268246805),
        (-104.94262695312236, 40.45065268246805),
        (-104.94262695312236, 41.52867510196275),
    ],
}

TNM.find_details(**params)['total']
```

Available parameters

```{code-cell} ipython3
help(TNM.find_details)
```

### Max items

Defaults to about 50. You only retrieve about 1000 items in one call.

```{code-cell} ipython3
len(TNM.find_details()['items'])
```

```{code-cell} ipython3
len(TNM.find_details(max=1000000)['items'])
```

Use offset to retrieve more batches.

```{code-cell} ipython3
params = {
    'q': 'National Elevation Dataset (NED) 1/3 arc-second',
    'polyCode': '01010002',
    'polyType': 'huc8',
    'max': 2,
}

TNM.find_details(**params, offset=0)['items'][0] == TNM.find_details(
    **params, offset=1
)['items'][0]
```

### Select a region from leafmap

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=4)
m
```

```{code-cell} ipython3
region = m.user_roi_bounds()
if region is None:
    region = [-115.9689, 35.9758, -115.3619, 36.4721]
```

```{code-cell} ipython3
TNM.find_details(q='LAZ', bbox=region)['total']
```

### Error handling

```{code-cell} ipython3
bool(TNM.find_details(start="01-01-2010", q="NED", bbox=region))
```

```{code-cell} ipython3
bool(TNM.find_details(start='2021-12-01', end='2020-01-01', q='NED', bbox=region))
```

```{code-cell} ipython3
bool(TNM.find_details(start='2021-12-01', end='2022-01-01', q='NED', bbox=region))
```

```{code-cell} ipython3
bool(
    TNM.find_details(
        start='2020-12-01',
        end='2022-01-01',
        q='NED',
        dateType='dateCreated',
        bbox=region,
    )
)
```

### Downloading files 

```{code-cell} ipython3
help(TNM.download_tiles)
```

```{code-cell} ipython3
params = {
    'q': 'National Elevation Dataset (NED) 1/3 arc-second',
    'polyCode': '01010002',
    'polyType': 'huc8',
    'max': 0,
}

TNM.download_tiles(API=params)
```

It can also be accessed without invoking the class.

```{code-cell} ipython3
params = {
    'q': 'National Elevation Dataset (NED) 1/3 arc-second',
    'polyCode': '01010002',
    'polyType': 'huc8',
    'max': 0,
}

leafmap.download_tnm(API=params)
```

```{code-cell} ipython3
region = [-115.9689, 35.9758, -115.3619, 36.4721]

leafmap.download_ned(region=region, return_url=True) == leafmap.download_tnm(
    region=region, return_url=True, API={'q': 'NED'}
)
```

### List of files

```{code-cell} ipython3
TNM.find_tiles(API=params)
```

### Dataset metadata

```{code-cell} ipython3
TNM.datasets_full[0]
```

### Read the docs

```{code-cell} ipython3
help(TNM)
```
