import os
import csv
from collections import OrderedDict
try:
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.cm import register_cmap
    matplotlib_available = True
except:
    matplotlib_available = False

HERE = os.path.abspath(os.path.dirname(__file__))
PATH = 'colormaps'


class AttrODict(OrderedDict):
    """Ordered dictionary with attribute access (e.g. for tab completion)"""
    def __dir__(self):
        return self.keys()

    def __delattr__(self, name):
        del self[name]

    def __getattr__(self, name):
        return self[name] if not name.startswith('_') else super(AttrODict, self).__getattr__(name)

    def __setattr__(self, name, value):
        if (name.startswith('_')):
            return super(AttrODict, self).__setattr__(name, value)
        self[name] = value

def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

def add_bokeh_palette(name, colorlist):
    palette[name] = [rgb_to_hex(int(r*255), int(g*255), int(b*255)) for r, g, b in colorlist]

def add_mpl_cm(name, colorlist):
    cm[name] = LinearSegmentedColormap.from_list(name, colorlist, N=len(colorlist))
    register_cmap(name, cmap=cm[name])

cmaps = AttrODict()
palette = AttrODict()
cm = AttrODict()
path = os.path.join(HERE, PATH)

for filename in sorted(os.listdir(path)):
    name, ext = os.path.splitext(filename)
    if ext == '.csv':
        with open(os.path.join(path, filename), 'r') as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            colorlist = [l for l in reader]
            cmaps[name] = colorlist
            add_bokeh_palette(name, colorlist)
            if matplotlib_available:
                add_mpl_cm(name, colorlist)
                add_mpl_cm('{name}_r'.format(name=name), list(reversed(colorlist)))
