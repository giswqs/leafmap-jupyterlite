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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/29_pydeck.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/29_pydeck.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.deck as leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map(center=(40, -100), zoom=3)
m
```

Add basemap.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("HYBRID")
m
```

Add vector data to the map. It supports any GeoPandas supported format, such as GeoJSON, shapefile, KML.

```{code-cell} ipython3
m = leafmap.Map()
filename = (
    "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson"
)
m.add_vector(filename, random_color_column="STATEFP")
m
```

Add a GeoPandas GeoDataFrame to the map.

```{code-cell} ipython3
import geopandas as gpd
```

```{code-cell} ipython3
url = (
    "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_counties.geojson"
)
gdf = gpd.read_file(url)
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_gdf(gdf, random_color_column="STATEFP")
m
```

Create a 3D view of the map. **Press Ctrl and hold down the left mouse button to rotate the 3D view.**

```{code-cell} ipython3
initial_view_state = {
    "latitude": 40,
    "longitude": -100,
    "zoom": 3,
    "pitch": 45,
    "bearing": 10,
}
m = leafmap.Map(initial_view_state=initial_view_state)
filename = (
    "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson"
)
m.add_vector(
    filename,
    random_color_column="STATEFP",
    extruded=True,
    get_elevation="ALAND",
    elevation_scale=0.000001,
)
m
```

![](https://i.imgur.com/LbCKhcM.gif)
