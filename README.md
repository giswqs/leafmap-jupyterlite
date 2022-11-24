# JupyterLite Demo

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org)

JupyterLite deployed as a static site to GitHub Pages, for demo purposes.

## ✨ Try it in your browser ✨

➡️ **https://demo.leafmap.org**

## Usage

Install leafmap for JupyterLite:

```python
import piplite
await piplite.install('leafmap-lite')
await piplite.install(['leafmap', 'geopandas', 'shapely', 'pyproj'], deps=False)
```
