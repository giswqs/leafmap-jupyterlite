# JupyterLite Demo

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org)

JupyterLite deployed as a static site to GitHub Pages, for demo purposes.

## ✨ Try it in your browser ✨

➡️ **https://demo.leafmap.org**

## Repository

➡️ **https://github.com/giswqs/leafmap-jupyterlite**

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

## How to get an updated version of JupyterLite

To clear local storage and sync with the latest version of JupyterLite site on GitHub, you can use:

Chrome Settings -> More tools -> Developer tools -> Application -> Storage -> IndexedDB -> JupyterLite Storage -> Right click files -> Clear

Then press F5 to refresh the page.

![](https://i.imgur.com/rL4rc6A.png)
