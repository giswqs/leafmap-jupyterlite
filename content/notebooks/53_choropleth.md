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

[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.leafmap.org/lab/index.html?path=notebooks/53_choropleth.ipynb)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/giswqs/leafmap/blob/master/examples/notebooks/53_choropleth.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/leafmap-binder)


```{code-cell} ipython3
%pip install -q leafmap
```

```{code-cell} ipython3
import leafmap
```

```{code-cell} ipython3
data = leafmap.examples.datasets.countries_geojson
```

Available classification schemes: 
* BoxPlot
* EqualInterval
* FisherJenks
* FisherJenksSampled
* HeadTailBreaks
* JenksCaspall
* JenksCaspallForced
* JenksCaspallSampled
* MaxP
* MaximumBreaks
* NaturalBreaks
* Quantiles
* Percentiles
* StdMean
* UserDefined

```{code-cell} ipython3
m = leafmap.Map()
m.add_data(
    data, column='POP_EST', scheme='Quantiles', cmap='Blues', legend_title='Population'
)
m
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_data(
    data,
    column='POP_EST',
    scheme='EqualInterval',
    cmap='Blues',
    legend_title='Population',
)
m
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_data(
    data,
    column='POP_EST',
    scheme='FisherJenks',
    cmap='Blues',
    legend_title='Population',
)
m
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_data(
    data,
    column='POP_EST',
    scheme='JenksCaspall',
    cmap='Blues',
    legend_title='Population',
)
m
```
