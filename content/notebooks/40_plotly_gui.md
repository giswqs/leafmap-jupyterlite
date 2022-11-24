---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/40_plotly_gui.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/40_plotly_gui.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap.plotlymap as leafmap
```

**Note:** For best experience, please use Jupyter notebook. The toolbar GUI is not working very well with JupyterLab at the moment.

```{code-cell} ipython3
m = leafmap.Map()
```

```{code-cell} ipython3
m.add_basemap("Stamen.Terrain")
```

```{code-cell} ipython3
m.add_heatmap_demo()
```

```{code-cell} ipython3
m.add_scatter_plot_demo()
```

```{code-cell} ipython3
m.show()
```

![](https://i.imgur.com/BJZbi9U.gif)
