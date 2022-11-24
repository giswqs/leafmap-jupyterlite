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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/19_map_to_html.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/19_map_to_html.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)

**Saving maps as a html file**


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.foliumap as leafmap
```

Create an interactive map.

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("HYBRID")
m
```

Specify the output HTML file name to save the map as a web page.

```{code-cell} ipython3
m.to_html("mymap.html")
```

If the output HTML file name is not provided, the function will return a string containing contain the source code of the HTML file.

```{code-cell} ipython3
html = m.to_html()
```

```{code-cell} ipython3
# print(html)
```
