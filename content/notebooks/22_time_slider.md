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

**Using time slider for visualizing timeseries images**


```{code-cell} ipython3
%pip install -q leafmap
```

This notebook requires the ipyleaflet plotting backend. Folium is not supported.

```{code-cell} ipython3
from leafmap import leafmap
```

First, you need to sign up a Planet account and get an API key. See https://developers.planet.com/quickstart/apis.
Uncomment the following line to pass in your API key.

```{code-cell} ipython3
# os.environ["PLANET_API_KEY"] = "12345"
```

![](https://i.imgur.com/ipVJ4cb.gif)

+++

Specify the map center and zoom level. 

```{code-cell} ipython3
m = leafmap.Map(center=[38.2659, -103.2447], zoom=13)
m
```

Use the time slider to visualize Planet quarterly mosaic.

```{code-cell} ipython3
m = leafmap.Map()
layers_dict = leafmap.planet_quarterly_tiles()
m.add_time_slider(layers_dict, time_interval=1)
m
```

Use the time slider to visualize basemaps.

```{code-cell} ipython3
m = leafmap.Map()
m.clear_layers()
layers_dict = leafmap.basemap_xyz_tiles()
m.add_time_slider(layers_dict, time_interval=1)
m
```

Use the time slider to visualize COG assets found within STAC items.

```{code-cell} ipython3
import ipyleaflet
import json
import requests

stac_api = "https://earth-search.aws.element84.com/v0"
search_endpoint = f"{stac_api}/search"

collection = "sentinel-s2-l2a-cogs"
payload = {
    "bbox": [
        -102.83340454101562,
        49.77860375256143,
        -102.41043090820312,
        50.05273014900257,
    ],
    "datetime": "2021-07-01T00:00:00Z/2021-10-01T12:31:12Z",
    "collections": [collection],
    "limit": 10,
    "query": {"eo:cloud_cover": {"gte": 0, "lte": 10}},
}

headers = {'Content-Type': 'application/json'}

response = requests.request(
    "POST", search_endpoint, headers=headers, data=json.dumps(payload)
)

features = response.json()["features"]
features.sort(key=lambda x: x["properties"]["datetime"], reverse=False)

layers_dict = {}
for feature in features:
    feature_id = feature["id"]
    print(feature_id)

    url = leafmap.stac_tile(
        f"{stac_api}/collections/{collection}/items/{feature_id}", bands=["visual"]
    )
    tile_layer = ipyleaflet.TileLayer(
        url=url,
        name=feature_id,
    )
    layers_dict[feature_id] = tile_layer

m = leafmap.Map(center=[50.093079, -103.152825], zoom=11)
m.add_time_slider(layers_dict, time_interval=2)
m
```
