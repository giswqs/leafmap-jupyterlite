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

[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.kepler as leafmap
```

Create an interactive map. You can specify various parameters to initialize the map, such as `center`, `zoom`, `height`, and `widescreen`.

```{code-cell} ipython3
m = leafmap.Map(center=[40, -100], zoom=2, height=600, widescreen=False)
m
```

Save the map to an interactive html. To hide the side panel and disable map customization. Set `read_only=False`

```{code-cell} ipython3
m.to_html(outfile="../html/kepler.html", read_only=False)
```

Display the interactive map in a notebook cell.

```{code-cell} ipython3
# m.static_map(width=950, height=600, read_only=True)
```

Add a CSV to the map. If you have a map config file, you can directly apply config to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
in_csv = (
    'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_data.csv'
)
config = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_config.json'
m.add_csv(in_csv, layer_name="hex_data", config=config)
m
```

Save the map configuration as a JSON file.

```{code-cell} ipython3
m.save_config("cache/config.json")
```

Save the map to an interactive html.

```{code-cell} ipython3
m.to_html(outfile="../html/kepler_hex.html")
```

Add a GeoJSON to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[20, 0], zoom=1)
lines = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
m.add_geojson(lines, layer_name="Cable lines")
m
```

```{code-cell} ipython3
m.to_html("../html/kepler_lines.html")
```

Add a GeoJSON with US state boundaries to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[50, -110], zoom=2)
polygons = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.json'
m.add_geojson(polygons, layer_name="Countries")
m
```

```{code-cell} ipython3
m.to_html("../html/kepler_states.html")
```

Add a shapefile to the map.

```{code-cell} ipython3
m = leafmap.Map(center=[20, 0], zoom=1)
in_shp = "https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip"
m.add_shp(in_shp, "Countries")
m
```

```{code-cell} ipython3
m.to_html("../html/kepler_countries.html")
```

Add a GeoPandas GeoDataFrame to the map.

```{code-cell} ipython3
import geopandas as gpd
```

```{code-cell} ipython3
gdf = gpd.read_file(
    "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson"
)
```

```{code-cell} ipython3
gdf
```

```{code-cell} ipython3
m = leafmap.Map(center=[20, 0], zoom=1)
m.add_gdf(gdf, "World cities")
m
```

```{code-cell} ipython3
m.to_html("../html/kepler_cities.html")
```
