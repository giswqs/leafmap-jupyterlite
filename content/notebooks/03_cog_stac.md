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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/03_cog_stac.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/03_cog_stac.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Using Cloud Optimized GeoTIFF (COG) and SpatioTemporal Asset Catalog (STAC)**


```{code-cell} ipython3
%pip install -q leafmap
```

**Working with Cloud Optimized GeoTIFF (COG)**

A Cloud Optimized GeoTIFF (COG) is a regular GeoTIFF file, aimed at being hosted on a HTTP file server, with an internal organization that enables more efficient workflows on the cloud. It does this by leveraging the ability of clients issuing HTTP GET range requests to ask for just the parts of a file they need. 

More information about COG can be found at <https://www.cogeo.org/in-depth.html>

Some publicly available Cloud Optimized GeoTIFFs:

* https://stacindex.org/
* https://cloud.google.com/storage/docs/public-datasets/landsat
* https://www.digitalglobe.com/ecosystem/open-data
* https://earthexplorer.usgs.gov/

For this demo, we will use data from https://www.maxar.com/open-data/california-colorado-fires for mapping California and Colorado fires. A List of COGs can be found [here](https://github.com/giswqs/leafmap/blob/master/examples/data/cog_files.txt). 

+++

![](https://i.imgur.com/pE4mxwf.gif)

```{code-cell} ipython3
import leafmap
```

Create an interactive map.

```{code-cell} ipython3
Map = leafmap.Map()
```

```{code-cell} ipython3
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
```

Retrieve the bounding box coordinates of the COG file.

```{code-cell} ipython3
leafmap.cog_bounds(url)
```

Retrieve the centroid coordinates of the COG file.

```{code-cell} ipython3
leafmap.cog_center(url)
```

Retrieve the band names of the COG file.

```{code-cell} ipython3
leafmap.cog_bands(url)
```

Retrieves the tile layer URL of the COG file.

```{code-cell} ipython3
leafmap.cog_tile(url)
```

Add a COG layer to the map.

```{code-cell} ipython3
Map.add_cog_layer(url, name="Fire (pre-event)")
```

```{code-cell} ipython3
url2 = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'
```

```{code-cell} ipython3
Map.add_cog_layer(url2, name="Fire (post-event)")
```

```{code-cell} ipython3
Map
```

**Working with  SpatioTemporal Asset Catalog (STAC)**

The SpatioTemporal Asset Catalog (STAC) specification provides a common language to describe a range of geospatial information, so it can more easily be indexed and discovered. A 'spatiotemporal asset' is any file that represents information about the earth captured in a certain space and time. The initial focus is primarily remotely-sensed imagery (from satellites, but also planes, drones, balloons, etc), but the core is designed to be extensible to SAR, full motion video, point clouds, hyperspectral, LiDAR and derived data like NDVI, Digital Elevation Models, mosaics, etc. More information about STAC can be found at https://stacspec.org/

Some publicly available SpatioTemporal Asset Catalog (STAC):

* https://stacindex.org

For this demo, we will use STAC assets from https://stacindex.org/catalogs/spot-orthoimages-canada-2005#/?t=catalogs

+++

Create an interactive map.

```{code-cell} ipython3
Map = leafmap.Map()
```

```{code-cell} ipython3
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
```

Retrieve the bounding box coordinates of the STAC file.

```{code-cell} ipython3
leafmap.stac_bounds(url)
```

Retrieve the centroid coordinates of the STAC file.

```{code-cell} ipython3
leafmap.stac_center(url)
```

Retrieve the band names of the STAC file.

```{code-cell} ipython3
leafmap.stac_bands(url)
```

Retrieve the tile layer URL of the STAC file.

```{code-cell} ipython3
leafmap.stac_tile(url, bands=['B3', 'B2', 'B1'])
```

Add a STAC layer to the map.

```{code-cell} ipython3
Map.add_stac_layer(url, bands=['pan'], name='Panchromatic')
```

```{code-cell} ipython3
Map.add_stac_layer(url, bands=['B3', 'B2', 'B1'], name='False color')
```

```{code-cell} ipython3
Map
```
