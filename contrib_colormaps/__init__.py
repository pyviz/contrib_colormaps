"""
Python bindings to contributor colormaps

Each of these colormaps can be accessed as a Bokeh palette or
Matplotlib colormap, either by string name:

  palette['name']
  cm['name']

or as Python attributes:

  palette.name
  cm.name

or as individually importable Python attributes:

  m_name
  b_name
"""


from .core import cmaps, palette, cm

# Add contributor cmaps to namespace
for name, cmap in cmaps.items():
    globals()[name] = cmap

for name, cmap in palette.items():
    globals()['b_{name}'.format(name=name)] = cmap

for name, cmap in cm.items():
    globals()['m_{name}'.format(name=name)] = cmap
