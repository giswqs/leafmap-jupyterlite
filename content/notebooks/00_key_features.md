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

# Key Features

You can try out leafmap by using [Goolge Colab](https://gishub.org/leafmap-colab) or [Binder](https://gishub.org/leafmap-binder) without having to install anything on your computer.

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/00_key_features.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://gishub.org/leafmap-colab)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

+++

## Install leafmap

```{code-cell} ipython3
%pip install -q leafmap
```

## Use folium plotting backend

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

## Use ipyleaflet plotting backend

```{code-cell} ipython3
import leafmap
```

## Create an interactive map

```{code-cell} ipython3
m = leafmap.Map(center=(40, -100), zoom=4)
m
```

## Customize map height

```{code-cell} ipython3
m = leafmap.Map(height="400px", width="800px")
m
```

## Set control visibility

```{code-cell} ipython3
m = leafmap.Map(
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True,
)
m
```

## Change basemaps

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Esri.NatGeoWorldMap")
m
```

## Add XYZ tile layer

```{code-cell} ipython3
m = leafmap.Map()
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m
```

## Add WMS tile layer

```{code-cell} ipython3
m = leafmap.Map()
naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
m.add_wms_layer(
    url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True
)
m
```

## Add COG layer

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
m.add_cog_layer(url, name="Fire (pre-event)")
m
```

## Add STAC layer

```{code-cell} ipython3
m = leafmap.Map()
url = 'https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json'
m.add_stac_layer(url, bands=['B3', 'B2', 'B1'], name='False color')
m
```

## Add legend

```{code-cell} ipython3
m = leafmap.Map()
url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?"
m.add_wms_layer(
    url,
    layers="NLCD_2016_Land_Cover_L48",
    name="NLCD 2016 CONUS Land Cover",
    format="image/png",
    transparent=True,
)
m.add_legend(builtin_legend='NLCD')
m
```

## Add colorbar

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap('USGS 3DEP Elevation')
colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
vmin = 0
vmax = 4000
m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
m
```

## Add GeoJSON

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(in_geojson, layer_name="Cable lines")
m
```

```{code-cell} ipython3
# Add a GeoJSON with random filled color to the map.
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
m.add_geojson(
    url, layer_name="Countries", fill_colors=['red', 'yellow', 'green', 'orange']
)
m
```

```{code-cell} ipython3
# Use custom style and hover_style functions.
m = leafmap.Map(center=[0, 0], zoom=2)
url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/countries.geojson"
style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,
}
hover_style = {"fillOpacity": 0.7}
m.add_geojson(url, layer_name="Countries", style=style, hover_style=hover_style)
m
```

## Add shapefile

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=2)
in_shp = 'https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip'
m.add_shp(in_shp, layer_name="Countries")
m
```

## Add KML

```{code-cell} ipython3
try:
    import geopandas
except ImportError:
    print('Installing geopandas ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'geopandas'])
```

```{code-cell} ipython3
m = leafmap.Map()
in_kml = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.kml'
m.add_kml(in_kml, layer_name="US States KML")
m
```

## Add GeoDataFrame

```{code-cell} ipython3
import geopandas as gpd

m = leafmap.Map()
gdf = gpd.read_file(
    "https://github.com/giswqs/leafmap/raw/master/examples/data/cable_geo.geojson"
)
m.add_gdf(gdf, layer_name="Cable lines")
m
```

## Create heat map

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
m.add_title("World Population Heat Map", font_size="20px", align="center")
m
```

## Save map to HTML

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Esri.NatGeoWorldMap")
m
```

```{code-cell} ipython3
m.to_html("mymap.html")
```

## Add Planet imagery

```{code-cell} ipython3
# os.environ["PLANET_API_KEY"] = "12345"
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_planet_by_month(year=2020, month=8)
m.add_planet_by_quarter(year=2019, quarter=2)
m
```

## Add OpenStreetMap data

Add OSM data of place(s) by name or ID to the map.

```{code-cell} ipython3
m = leafmap.Map(toolbar_control=False, layers_control=True)
m.add_osm_from_geocode("New York City", layer_name='NYC')
m
```

## Use heremap plotting backend

-   A HERE developer account, free and available under [HERE Developer Portal](https://developer.here.com)
-   An [API key](https://developer.here.com/documentation/identity-access-management/dev_guide/topics/dev-apikey.html) from the [HERE Developer Portal](https://developer.here.com)
-   Export API key into environment variable `HEREMAPS_API_KEY`

```bash
export HEREMAPS_API_KEY=YOUR-ACTUAL-API-KEY
```

```{code-cell} ipython3
import leafmap.heremap as leafmap
```

Set the API Key.

```{code-cell} ipython3
# os.environ["HEREMAPS_API_KEY"] = "12345"
```

```{code-cell} ipython3
api_key = os.environ.get("HEREMAPS_API_KEY")  # read api_key from environment variable.
```

Create an interactive map

```{code-cell} ipython3
m = leafmap.Map(api_key=api_key, center=(40, -100), zoom=4)
m
```
