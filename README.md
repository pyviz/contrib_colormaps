# contrib_colormaps: User-contributed colormaps

|    |    |
| --- | --- |
| Build Status | [![Linux/MacOS Build Status](https://travis-ci.org/pyviz/contrib_colormaps.svg?branch=master)](https://travis-ci.org/pyviz/contrib_colormaps) [![Windows Build status](https://img.shields.io/appveyor/ci/pyviz/contrib_colormaps/master.svg?logo=appveyor)](https://ci.appveyor.com/project/pyviz/contrib_colormaps/branch/master) |
| Latest dev release | [![Github tag](https://img.shields.io/github/tag/pyviz/contrib_colormaps.svg?label=tag&colorB=11ccbb)](https://github.com/pyviz/contrib_colormaps/tags) |
| Latest release | [![Github release](https://img.shields.io/github/release/pyviz/contrib_colormaps.svg?label=tag&colorB=11ccbb)](https://github.com/pyviz/contrib_colormaps/releases) [![PyPI version](https://img.shields.io/pypi/v/contrib_colormaps.svg?colorB=cc77dd)](https://pypi.python.org/pypi/contrib_colormaps) [![contrib_colormaps version](https://img.shields.io/conda/v/pyviz/contrib_colormaps.svg?colorB=4488ff&style=flat)](https://anaconda.org/pyviz/contrib_colormaps) [![conda-forge version](https://img.shields.io/conda/v/conda-forge/contrib_colormaps.svg?label=conda%7Cconda-forge&colorB=4488ff)](https://anaconda.org/conda-forge/contrib_colormaps) [![defaults version](https://img.shields.io/conda/v/anaconda/contrib_colormaps.svg?label=conda%7Cdefaults&style=flat&colorB=4488ff)](https://anaconda.org/anaconda/contrib_colormaps) |
| Docs | [![gh-pages](https://img.shields.io/github/last-commit/pyviz/contrib_colormaps/gh-pages.svg)](https://github.com/pyviz/contrib_colormaps/tree/gh-pages) [![site](https://img.shields.io/website-up-down-green-red/http/contrib_colormaps.pyviz.org.svg)](http://contrib_colormaps.pyviz.org) |


## What is it?

contrib_colormaps is a collection of user-contributed colormaps
for use with Python plotting programs like
[bokeh](http://bokeh.pydata.org),
[matplotlib](http://matplotlib.org), and
[holoviews](http://holoviews.org).


## Installation

contrib_colormaps supports Python 2.7, 3.5, 3.6 and 3.7 on Linux, Windows, or Mac
and can be installed with conda:

```
    conda install contrib_colormaps
```

or with pip:

```
    pip install contrib_colormaps
```

## Contributing a colormap

To add a colormap, open a pull request on this repository adding a csv of RGB values to the contrib_colormaps/colormaps
directory. This file should look like:

```
0,0.20755,0.97632
0,0.22113,0.96201
```

This PR should also include a new notebook in



## About PyViz

contrib_colormaps is part of the PyViz initiative for making Python-based visualization tools work well together.
See [pyviz.org](http://pyviz.org).