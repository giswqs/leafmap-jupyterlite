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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=workshops/SIGSPATIAL_2021.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://gishub.org/acm-colab)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/acm-binder)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/acm-binder-nb)
![](https://i.imgur.com/uKiXeCl.png)

+++

**Interactive Mapping and Geospatial Analysis with Leafmap & Jupyter**


This notebook was developed for the [leafmap workshop](https://dataoceanlab.github.io/spatial-api-2021/files/paper_1.pdf) taking place on November 2, 2021 at the [The 3rd ACM SIGSPATIAL International Workshop on APIs and Libraries for Geospatial Data Science (SpatialAPI 2021)](https://dataoceanlab.github.io/spatial-api-2021).

Author: [Qiusheng Wu](https://github.com/giswqs)

Launch this notebook to execute code interactively using: 
- Google Colab: https://gishub.org/acm-colab
- Pangeo Binder JupyterLab: https://gishub.org/acm-binder
- Pangeo Binder Jupyter Notebook: https://gishub.org/acm-binder-nb
- Streamlit web app: https://streamlit.gishub.org


## Introduction

### Workshop description

[Leafmap](https://leafmap.org) is a Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment. It is built upon a number of open-source packages, such as [folium](https://github.com/python-visualization/folium) and [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) (for creating interactive maps), [WhiteboxTools](https://github.com/jblindsay/whitebox-tools) and [whiteboxgui](https://github.com/giswqs/whiteboxgui) (for analyzing geospatial data), and [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) (for designing interactive graphical user interface). The WhiteboxTools library currently contains 480+ tools for advanced geospatial analysis. Leafmap provides many convenient functions for loading and visualizing geospatial data with only one line of code. Users can also use the interactive user interface to load geospatial data without coding. Anyone with a web browser and Internet connection can use leafmap to perform geospatial analysis and data visualization in the cloud with minimal coding. The topics that will be covered in this workshop include: 

1. A brief introduction to leafmap and relevant web resources 
2. Creating interactive maps using multiple plotting backends
3. Changing basemaps
4. Loading and visualizing vector/raster data
5. Using Cloud Optimized GeoTIFF (COG) and SpatialTemporal Asset Catalog (STAC)
6. Downloading OpenStreetMap data
7. Creating custom legends and colorbars
8. Creating split-panel maps and linked maps
9. Performing geospatial analysis using whiteboxgui.
10. Discussion and Q&A


This workshop is intended for scientific programmers, data scientists, geospatial analysts, and concerned citizens of Earth. The attendees are expected to have a basic understanding of Python and the Jupyter ecosystem. Familiarity with Earth science and geospatial datasets is useful but not required. More information about leafmap can be found at https://leafmap.org.


### Jupyter keyboard shortcuts

- Shift+Enter: run cell, select below
- Ctrl+Enter: : run selected cells
- Alt+Enter: run cell and insert below
- Tab: code completion or indent
- Shift+Tab: tooltip
- Ctrl+/: comment out code

+++

## Set up environment

### Required Python packages:
* [leafmap](https://github.com/giswqs/leafmap) - A Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment
* [keplergl](https://docs.kepler.gl/docs/keplergl-jupyter) - A high-performance web-based application for visual exploration of large-scale geolocation data sets
* [pydeck](https://deckgl.readthedocs.io/en/latest) - High-scale spatial rendering in Python, powered by deck.gl.
* [geopandas](https://geopandas.org) - An open source project to make working with geospatial data in python easier. 
* [xarray-leaflet](https://github.com/davidbrochart/xarray_leaflet) - An xarray extension for tiled map plotting.

### Use Google Colab

Click the button below to open this notebook in Google Colab and execute code interactively.

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=workshops/SIGSPATIAL_2021.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://gishub.org/acm-colab)

```{code-cell} ipython3
import os
import subprocess
import sys
```

```{code-cell} ipython3
import warnings

warnings.filterwarnings("ignore")
```

A function for installing Python packages.

```{code-cell} ipython3
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
```

Install required Python packages in Google Colab.

```{code-cell} ipython3
pkgs = [
    'leafmap',
    'geopandas',
    'keplergl',
    'pydeck',
    'xarray_leaflet',
    'osmnx',
    'pygeos',
    'imageio',
    'tifffile',
]
if "google.colab" in sys.modules:
    for pkg in pkgs:
        install(pkg)
```

### Use Pangeo Binder

Click the buttons below to open this notebook in JupyterLab (first button) or Jupyter Notebook (second button) and execute code interactively.

[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/acm-binder)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/acm-binder-nb)

- JupyterLab: https://gishub.org/acm-binder
- Jupyter Notebook: https://gishub.org/acm-binder-nb

+++

### Use Miniconda/Anaconda

If you have
[Anaconda](https://www.anaconda.com/distribution/#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your computer, you can install leafmap using the following commands. Leafmap has an optional dependency - [geopandas](https://geopandas.org), which can be challenging to install on some computers, especially Windows. It is highly recommended that you create a fresh conda environment to install geopandas and leafmap. Follow the commands below to set up a conda env and install geopandas, leafmap, keplergl, and xarray_leaflet. 

```
conda create -n geo python=3.8
conda activate geo
conda install geopandas
conda install mamba -c conda-forge
mamba install leafmap keplergl pydeck xarray_leaflet -c conda-forge
mamba install osmnx pygeos imageio tifffile -c conda-forge
jupyter lab
```

```{code-cell} ipython3
try:
    import leafmap
except ImportError:
    install('leafmap')
```

## Create an interactive map

`Leafmap` has five plotting backends: [folium](https://github.com/python-visualization/folium), [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet), [here-map](https://github.com/heremaps/here-map-widget-for-jupyter), [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter), and [pydeck](https://deckgl.readthedocs.io). Note that the backends do not offer equal functionality. Some interactive functionality in `ipyleaflet` might not be available in other plotting backends. To use a specific plotting backend, use one of the following:

- `import leafmap.leafmap as leafmap`
- `import leafmap.foliumap as leafmap`
- `import leafmap.heremap as leafmap`
- `import leafmap.kepler as leafmap`
- `import leafmap.deck as leafmap`

### Use ipyleaflet

```{code-cell} ipython3
import leafmap

m = leafmap.Map()
m
```

### Use folium

```{code-cell} ipython3
import leafmap.foliumap as leafmap

m = leafmap.Map()
m
```

### Use kepler.gl

```{code-cell} ipython3
import leafmap.kepler as leafmap

m = leafmap.Map()
m
```

If you encounter an error saying `Error displaying widget: model not found` when trying to display the map, you can use `m.static_map()` as a workaround until this [kepler.gl bug](https://github.com/keplergl/kepler.gl/issues/1165) has been resolved.  

```{code-cell} ipython3
m.static_map(width=1280, height=600)
```

+++ {"tags": []}

### Use pydeck

```{code-cell} ipython3
import leafmap.deck as leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
m
```

## Customize the default map

### Specify map center and zoom level

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map(center=(40, -100), zoom=4)  # center=(lat, lon)
m
```

```{code-cell} ipython3
m = leafmap.Map(center=(51.5, -0.15), zoom=17)
m
```

### Change map size

```{code-cell} ipython3
m = leafmap.Map(height="400px", width="800px")
m
```

### Set control visibility

When creating a map, set the following controls to either `True` or `False` as appropriate.

* attribution_control
* draw_control
* fullscreen_control
* layers_control
* measure_control
* scale_control
* toolbar_control

```{code-cell} ipython3
m = leafmap.Map(
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=False,
)
m
```

Remove all controls from the map.

```{code-cell} ipython3
m = leafmap.Map()
m.clear_controls()
m
```

## Change basemaps

Specify a Google basemap to use, can be one of ["ROADMAP", "TERRAIN", "SATELLITE", "HYBRID"].

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map(google_map="TERRAIN")  # HYBIRD, ROADMAP, SATELLITE, TERRAIN
m
```

Add a basemap using the `add_basemap()` function.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Esri.NatGeoWorldMap")
m
```

Print out the list of available basemaps.

```{code-cell} ipython3
for basemap in leafmap.basemaps:
    print(basemap)
```

![](https://i.imgur.com/T1oBWSz.png)

```{code-cell} ipython3
m = leafmap.Map()
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m
```

### Add WMS tile layer

More WMS basemaps can be found at the following websites:

- USGS National Map: https://viewer.nationalmap.gov/services
- MRLC NLCD Land Cover data: https://www.mrlc.gov/data-services-page
- FWS NWI Wetlands data: https://www.fws.gov/wetlands/Data/Web-Map-Services.html

```{code-cell} ipython3
m = leafmap.Map()
naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
m.add_wms_layer(
    url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True
)
m
```

+++ {"tags": []}

### Add xyzservices provider

Add a layer from [xyzservices](https://github.com/geopandas/xyzservices) provider object.

```{code-cell} ipython3
import leafmap
import xyzservices.providers as xyz
```

```{code-cell} ipython3
basemap = xyz.OpenTopoMap
basemap
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap(basemap)
m
```

## Add COG/STAC layers

A Cloud Optimized GeoTIFF (COG) is a regular GeoTIFF file, aimed at being hosted on a HTTP file server, with an internal organization that enables more efficient workflows on the cloud. It does this by leveraging the ability of clients issuing HTTP GET range requests to ask for just the parts of a file they need. 

More information about COG can be found at <https://www.cogeo.org/in-depth.html>

Some publicly available Cloud Optimized GeoTIFFs:

* https://stacindex.org/
* https://cloud.google.com/storage/docs/public-datasets/landsat
* https://www.digitalglobe.com/ecosystem/open-data
* https://earthexplorer.usgs.gov/

For this demo, we will use data from https://www.maxar.com/open-data/california-colorado-fires for mapping California and Colorado fires. A list of COGs can be found [here](https://github.com/giswqs/leafmap/blob/master/examples/data/cog_files.txt).

### Add COG layer

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
url2 = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'

m.add_cog_layer(url, name="Fire (pre-event)")
m.add_cog_layer(url2, name="Fire (post-event)")
m
```

### Add STAC layer

The SpatioTemporal Asset Catalog (STAC) specification provides a common language to describe a range of geospatial information, so it can more easily be indexed and discovered. A 'spatiotemporal asset' is any file that represents information about the earth captured in a certain space and time. The initial focus is primarily remotely-sensed imagery (from satellites, but also planes, drones, balloons, etc), but the core is designed to be extensible to SAR, full motion video, point clouds, hyperspectral, LiDAR and derived data like NDVI, Digital Elevation Models, mosaics, etc. More information about STAC can be found at https://stacspec.org/

Some publicly available SpatioTemporal Asset Catalog (STAC):

* https://stacindex.org

For this demo, we will use STAC assets from https://stacindex.org/catalogs/spot-orthoimages-canada-2005#/?t=catalogs

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
m.add_stac_layer(url, bands=['B3', 'B2', 'B1'], name='False color')
m
```

## Add local raster datasets

The `add_raster` function relies on the `xarray_leaflet` package and is only available for the ipyleaflet plotting backend. Therefore, Google Colab is not supported. Note that `xarray_leaflet` does not work properly on Windows ([source](https://github.com/davidbrochart/xarray_leaflet/issues/30)).

```{code-cell} ipython3
import os
import leafmap
```

Download samples raster datasets

More datasets can be downloaded from https://viewer.nationalmap.gov/basic/

```{code-cell} ipython3
out_dir = os.getcwd()

landsat = os.path.join(out_dir, 'landsat.tif')
dem = os.path.join(out_dir, 'dem.tif')
```

Download a small Landsat imagery.

```{code-cell} ipython3
if not os.path.exists(landsat):
    landsat_url = 'https://drive.google.com/file/d/1EV38RjNxdwEozjc9m0FcO3LFgAoAX1Uw/view?usp=sharing'
    leafmap.download_from_gdrive(landsat_url, 'landsat.tif', out_dir, unzip=False)
```

Download a small DEM dataset.

```{code-cell} ipython3
if not os.path.exists(dem):
    dem_url = 'https://drive.google.com/file/d/1vRkAWQYsLWCi6vcTMk8vLxoXMFbdMFn8/view?usp=sharing'
    leafmap.download_from_gdrive(dem_url, 'dem.tif', out_dir, unzip=False)
```

```{code-cell} ipython3
m = leafmap.Map()
```

Add local raster datasets to the map

More colormap can be found at https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

```{code-cell} ipython3
m.add_raster(dem, colormap='terrain', layer_name='DEM')
```

```{code-cell} ipython3
m.add_raster(landsat, bands=[5, 4, 3], layer_name='Landsat')
```

```{code-cell} ipython3
m
```

## Add legend

### Add built-in legend

```{code-cell} ipython3
import leafmap
```

List all available built-in legends.

```{code-cell} ipython3
legends = leafmap.builtin_legends
for legend in legends:
    print(legend)
```

Add a WMS layer and built-in legend to the map.

```{code-cell} ipython3
m = leafmap.Map()
url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms?"
m.add_wms_layer(
    url,
    layers="NLCD_2019_Land_Cover_L48",
    name="NLCD 2019 CONUS Land Cover",
    format="image/png",
    transparent=True,
)
m.add_legend(builtin_legend='NLCD')
m
```

Add U.S. National Wetlands Inventory (NWI). More info at https://www.fws.gov/wetlands.

```{code-cell} ipython3
m = leafmap.Map(google_map="HYBRID")

url1 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?"
m.add_wms_layer(
    url1, layers="1", format='image/png', transparent=True, name="NWI Wetlands Vector"
)

url2 = "https://www.fws.gov/wetlands/arcgis/services/Wetlands_Raster/ImageServer/WMSServer?"
m.add_wms_layer(
    url2, layers="0", format='image/png', transparent=True, name="NWI Wetlands Raster"
)

m.add_legend(builtin_legend="NWI")
m
```

### Add custom legend

There are two ways you can add custom legends:

1. Define legend labels and colors
2. Define legend dictionary

Define legend keys and colors

```{code-cell} ipython3
m = leafmap.Map()

labels = ['One', 'Two', 'Three', 'Four', 'ect']
# color can be defined using either hex code or RGB (0-255, 0-255, 0-255)
colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3']
# colors = [(255, 0, 0), (127, 255, 0), (127, 18, 25), (36, 70, 180), (96, 68, 123)]

m.add_legend(title='Legend', labels=labels, colors=colors)
m
```

Define a legend dictionary.

```{code-cell} ipython3
m = leafmap.Map()

url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms?"
m.add_wms_layer(
    url,
    layers="NLCD_2019_Land_Cover_L48",
    name="NLCD 2019 CONUS Land Cover",
    format="image/png",
    transparent=True,
)

legend_dict = {
    '11 Open Water': '466b9f',
    '12 Perennial Ice/Snow': 'd1def8',
    '21 Developed, Open Space': 'dec5c5',
    '22 Developed, Low Intensity': 'd99282',
    '23 Developed, Medium Intensity': 'eb0000',
    '24 Developed High Intensity': 'ab0000',
    '31 Barren Land (Rock/Sand/Clay)': 'b3ac9f',
    '41 Deciduous Forest': '68ab5f',
    '42 Evergreen Forest': '1c5f2c',
    '43 Mixed Forest': 'b5c58f',
    '51 Dwarf Scrub': 'af963c',
    '52 Shrub/Scrub': 'ccb879',
    '71 Grassland/Herbaceous': 'dfdfc2',
    '72 Sedge/Herbaceous': 'd1d182',
    '73 Lichens': 'a3cc51',
    '74 Moss': '82ba9e',
    '81 Pasture/Hay': 'dcd939',
    '82 Cultivated Crops': 'ab6c28',
    '90 Woody Wetlands': 'b8d9eb',
    '95 Emergent Herbaceous Wetlands': '6c9fb8',
}

m.add_legend(title="NLCD Land Cover Classification", legend_dict=legend_dict)
m
```

## Add colormap

The colormap functionality requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
import leafmap
import leafmap.colormaps as cm
```

### Common colormaps

Color palette for DEM data.

```{code-cell} ipython3
cm.palettes.dem
```

Show the DEM palette.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.palettes.dem, axis_off=True)
```

Color palette for NDVI data.

```{code-cell} ipython3
cm.palettes.ndvi
```

Show the NDVI palette.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.palettes.ndvi)
```

### Custom colormaps

Specify the number of classes for a palette.

```{code-cell} ipython3
cm.get_palette('terrain', n_class=8)
```

Show the terrain palette with 8 classes.

```{code-cell} ipython3
cm.plot_colormap(colors=cm.get_palette('terrain', n_class=8))
```

Create a palette with custom colors, label, and font size.

```{code-cell} ipython3
cm.plot_colormap(colors=["red", "green", "blue"], label="Temperature", font_size=12)
```

Create a discrete color palette.

```{code-cell} ipython3
cm.plot_colormap(
    colors=["red", "green", "blue"], discrete=True, label="Temperature", font_size=12
)
```

Specify the width and height for the palette.

```{code-cell} ipython3
cm.plot_colormap(
    'terrain',
    label="Elevation",
    width=8.0,
    height=0.4,
    orientation='horizontal',
    vmin=0,
    vmax=1000,
)
```

Change the orentation of the colormap to be vertical.

```{code-cell} ipython3
cm.plot_colormap(
    'terrain',
    label="Elevation",
    width=0.4,
    height=4,
    orientation='vertical',
    vmin=0,
    vmax=1000,
)
```

### Horizontal colormap

Add a horizontal colorbar to an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_colormap(
    'terrain',
    label="Elevation",
    width=8.0,
    height=0.4,
    orientation='horizontal',
    vmin=0,
    vmax=4000,
)
m
```

### Vertical colormap

Add a vertical colorbar to an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_colormap(
    'terrain',
    label="Elevation",
    width=0.4,
    height=4,
    orientation='vertical',
    vmin=0,
    vmax=4000,
)
m
```

### List of available colormaps

```{code-cell} ipython3
cm.plot_colormaps(width=12, height=0.4)
```

## Add vector datasets

### Add CSV

Read a CSV as a Pandas DataFrame.

```{code-cell} ipython3
import os
import leafmap
```

```{code-cell} ipython3
in_csv = 'https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv'
df = leafmap.csv_to_df(in_csv)
df
```

Create a point layer from a CSV file containing lat/long information.

```{code-cell} ipython3
m = leafmap.Map()
m.add_xy_data(in_csv, x="longitude", y="latitude", layer_name="World Cities")
m
```

Set the output directory.

```{code-cell} ipython3
out_dir = os.getcwd()
out_shp = os.path.join(out_dir, 'world_cities.shp')
```

Convert a CSV file containing lat/long information to a shapefile.

```{code-cell} ipython3
leafmap.csv_to_shp(in_csv, out_shp)
```

Convert a CSV file containing lat/long information to a GeoJSON.

```{code-cell} ipython3
out_geojson = os.path.join(out_dir, 'world_cities.geojson')
leafmap.csv_to_geojson(in_csv, out_geojson)
```

Convert a CSV file containing lat/long information to a GeoPandas GeoDataFrame.

```{code-cell} ipython3
gdf = leafmap.csv_to_gdf(in_csv)
gdf
```

### Add GeoJSON

Add a GeoJSON to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(in_geojson, layer_name="Cable lines", info_mode='on_hover')
m
```

Add a GeoJSON with random filled color to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_geojson(
    url, layer_name="Countries", fill_colors=['red', 'yellow', 'green', 'orange']
)
m
```

### Add shapefile

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
in_shp = 'https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip'
m.add_shp(in_shp, layer_name="Countries")
m
```

### Add KML

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map()
in_kml = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.kml'
m.add_kml(in_kml, layer_name="US States KML")
m
```

### Add GeoDataFrame

```{code-cell} ipython3
import geopandas as gpd
```

```{code-cell} ipython3
m = leafmap.Map()
gdf = gpd.read_file(
    "https://github.com/giswqs/leafmap/raw/master/examples/data/cable_geo.geojson"
)
m.add_gdf(gdf, layer_name="Cable lines")
m
```

+++ {"tags": []}

### Add point layer

Add a point layer using the interactive GUI.

![](https://i.imgur.com/1QVEtlN.gif)

```{code-cell} ipython3
m = leafmap.Map()
m
```

Add a point layer programmatically.

```{code-cell} ipython3
m = leafmap.Map()
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.geojson"
m.add_point_layer(url, popup=["name", "pop_max"], layer_name="US Cities")
m
```

### Add vector

The `add_vector` function supports any vector data format supported by GeoPandas.

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_vector(
    url, layer_name="Countries", fill_colors=['red', 'yellow', 'green', 'orange']
)
m
```

## Download OSM data

### OSM from geocode

Add OSM data of place(s) by name or ID to the map. Note that the leafmap custom layer control does not support GeoJSON, we need to use the ipyleaflet built-in layer control. 

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_geocode("New York City", layer_name='NYC')
m
```

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_geocode("Chicago, Illinois", layer_name='Chicago, IL')
m
```

### OSM from place

Add OSM entities within boundaries of geocodable place(s) to the map.

+++

Show OSM feature tags.
https://wiki.openstreetmap.org/wiki/Map_features

```{code-cell} ipython3
# leafmap.osm_tags_list()
```

### OSM from address

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_address(
    address="New York City", tags={"amenity": "bar"}, dist=1500, layer_name="NYC bars"
)
m
```

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_address(
    address="New York City",
    tags={"landuse": ["retail", "commercial"], "building": True},
    dist=1000,
    layer_name="NYC buildings",
)
m
```

### OSM from bbox

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
north, south, east, west = 40.7551, 40.7454, -73.9738, -73.9965
m.add_osm_from_bbox(
    north, south, east, west, tags={"amenity": "bar"}, layer_name="NYC bars"
)
m
```

### OSM from point

Add OSM entities within some distance N, S, E, W of a point to the map.

```{code-cell} ipython3
m = leafmap.Map(
    center=[46.7808, -96.0156], zoom=12, toolbar_control=False, layers_control=True
)
m.add_osm_from_point(
    center_point=(46.7808, -96.0156),
    tags={"natural": "water"},
    dist=10000,
    layer_name="Lakes",
)
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[39.9170, 116.3908], zoom=15, toolbar_control=False, layers_control=True
)
m.add_osm_from_point(
    center_point=(39.9170, 116.3908),
    tags={"building": True, "natural": "water"},
    dist=1000,
    layer_name="Beijing",
)
m
```

### OSM from view

Add OSM entities within the current map view to the map.

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.set_center(-73.9854, 40.7500, 16)
m
```

```{code-cell} ipython3
m.add_osm_from_view(tags={"amenity": "bar", "building": True}, layer_name="New York")
```

Create a GeoPandas GeoDataFrame from place.

```{code-cell} ipython3
gdf = leafmap.osm_gdf_from_place("New York City", tags={"amenity": "bar"})
gdf
```

## Use WhiteboxTools

Use the built-in toolbox to perform geospatial analysis. For example, you can perform depression filling using the sample DEM dataset downloaded in the above step.

![](https://i.imgur.com/KGHly63.png)

```{code-cell} ipython3
import os
import leafmap
import urllib.request
```

Download a sample DEM dataset.

```{code-cell} ipython3
url = 'https://github.com/giswqs/whitebox-python/raw/master/whitebox/testdata/DEM.tif'
```

```{code-cell} ipython3
urllib.request.urlretrieve(url, "dem.tif")
```

```{code-cell} ipython3
m = leafmap.Map()
m
```

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
import whitebox
```

```{code-cell} ipython3
wbt = whitebox.WhiteboxTools()
wbt.verbose = False
```

```{code-cell} ipython3
data_dir = os.getcwd()
wbt.set_working_dir(data_dir)
```

```{code-cell} ipython3
wbt.feature_preserving_smoothing("dem.tif", "smoothed.tif", filter=9)
wbt.breach_depressions("smoothed.tif", "breached.tif")
wbt.d_inf_flow_accumulation("breached.tif", "flow_accum.tif")
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import imageio

%matplotlib inline
```

```{code-cell} ipython3
original = imageio.imread(os.path.join(data_dir, 'dem.tif'))
smoothed = imageio.imread(os.path.join(data_dir, 'smoothed.tif'))
breached = imageio.imread(os.path.join(data_dir, 'breached.tif'))
flow_accum = imageio.imread(os.path.join(data_dir, 'flow_accum.tif'))
```

```{code-cell} ipython3
fig = plt.figure(figsize=(16, 11))

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('Original DEM')
plt.imshow(original)

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Smoothed DEM')
plt.imshow(smoothed)

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('Breached DEM')
plt.imshow(breached)

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('Flow Accumulation')
plt.imshow(flow_accum)

plt.show()
```

## Create linked map

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
leafmap.basemaps.keys()
```

```{code-cell} ipython3
layers = ['ROADMAP', 'HYBRID']
leafmap.linked_maps(rows=1, cols=2, height='400px', layers=layers)
```

```{code-cell} ipython3
layers = ['Stamen.Terrain', 'OpenTopoMap']
leafmap.linked_maps(rows=1, cols=2, height='400px', layers=layers)
```

Create a 2 * 2 linked map to visualize land cover change. Specify the `center` and `zoom` parameters to change the default map center and zoom level.

```{code-cell} ipython3
layers = [str(f"NLCD {year} CONUS Land Cover") for year in [2001, 2006, 2011, 2016]]
labels = [str(f"NLCD {year}") for year in [2001, 2006, 2011, 2016]]
leafmap.linked_maps(
    rows=2,
    cols=2,
    height='300px',
    layers=layers,
    labels=labels,
    center=[36.1, -115.2],
    zoom=9,
)
```

## Create split-panel map

Create a split-panel map by specifying the `left_layer` and `right_layer`, which can be chosen from the basemap names, or any custom XYZ tile layer.

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
leafmap.split_map(left_layer="ROADMAP", right_layer="HYBRID")
```

Hide the zoom control from the map.

```{code-cell} ipython3
leafmap.split_map(
    left_layer="Esri.WorldTopoMap", right_layer="OpenTopoMap", zoom_control=False
)
```
