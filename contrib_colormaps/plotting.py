"""
This module is not required for contrib_colormaps. It contains functions
to facilitate plotting of colormaps and is mainly used in the
documentation.
"""

import numpy as np
import holoviews as hv
from holoviews import opts

from . import palette, cm

array = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))[0]

def swatch(name, bounds=None, array=array, **kwargs):
    """Show swatch using matplotlib or bokeh via holoviews"""
    if bounds is None:
        bounds = (0, 0, 256, 1)

    plot = hv.Image(array, bounds=bounds, group=name)
    backends = hv.Store.loaded_backends()
    if 'bokeh' in backends:
        width = kwargs.pop('width', 900)
        height = kwargs.pop('height', 100)
        plot.opts(opts.Image(backend='bokeh', width=width, height=height, toolbar='above',
                             default_tools=['xwheel_zoom', 'xpan', 'save', 'reset'],
                             cmap=palette[name]))
    if 'matplotlib' in backends:
        aspect = kwargs.pop('aspect', 15)
        fig_size = kwargs.pop('fig_size', 350)
        plot.opts(opts.Image(backend='matplotlib', aspect=aspect, fig_size=fig_size,
                             cmap=cm[name]))
    return plot.opts(opts.Image(xaxis=None, yaxis=None), opts.Image(**kwargs))
