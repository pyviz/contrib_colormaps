# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = 'contrib_colormaps'
authors = u'PyViz Developers'
copyright = u'2017-2019 ' + authors
description = 'Collection of user-contributed colormaps'

import contrib_colormaps
version = release = contrib_colormaps.__version__

nbbuild_cell_timeout = 10000
html_static_path += ['_static']

_NAV = (
    ('Introduction', 'index'),
    ('Colormaps', 'colormaps/index'),
    ('About', 'about'),
)

_SOCIAL = (
    ('Github', 'https://github.com/pyviz/' + project),
    ('Gitter', 'https://gitter.im/pyviz/pyviz'),
    ('PyViz', 'http://pyviz.org')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'WEBSITE_SERVER': 'http://{}.pyviz.org'.format(project),
    'VERSION': version,
    'NAV': _NAV ,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': _SOCIAL
})
