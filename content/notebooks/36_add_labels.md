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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/36_add_labels.ipynb)
<a href="https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/36_add_labels.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

Update the package if needed.

```{code-cell} ipython3
# leafmap.update_package()
```

Create an interactive map.

```{code-cell} ipython3
data = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.json"
```

```{code-cell} ipython3
Map = leafmap.Map(center=[40, -100], zoom=4, add_google_map=False, layers_control=True)
```

Labeling data.

```{code-cell} ipython3
Map.add_labels(
    data,
    "id",
    font_size="12pt",
    font_color="blue",
    font_family="arial",
    font_weight="bold",
)
Map
```

Remove labels

```{code-cell} ipython3
Map.remove_labels()
```

![](https://i.imgur.com/lELtitr.gif)
