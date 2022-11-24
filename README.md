# JupyterLite Demo

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org)

JupyterLite deployed as a static site to GitHub Pages, for demo purposes.

## ✨ Try it in your browser ✨

➡️ **https://demo.leafmap.org**

## Usage

Install leafmap for JupyterLite using:

```bash
%pip install -q leafmap
```

Alternatively, you can install leafmap using piplite:

```python
import piplite
await piplite.install('leafmap')
```

To install GeoPandas, you can use:

```python
import piplite
await piplite.install(['geopandas', 'shapely', 'pyproj'], deps=False)
```
