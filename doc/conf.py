# noqa
from nbsite.shared_conf import *

project = u'contrib_colormaps'
authors = u'PyViz authors'
copyright = u' 2019, ' + authors
description = 'Collection of user-contributed colormaps.'

import contrib_colormaps
version = release = contrib_colormaps.__version__

html_static_path += ['_static']
html_favicon = 'favicon.ico'
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'page_width': '90%',
    'font_family': "Ubuntu, sans-serif",
    'font_size': '0.9em',
    'link': '#347ab4',
    'link_hover': '#1c4669',
    'extra_nav_links': {
        'Github': 'https://github.com/pyviz/contrib_colormaps',
    },
    'show_powered_by': False,
}

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # WEBSITE_SERVER is optional for tests and local builds, but allows defining a canonical URL for search engines
    'WEBSITE_SERVER': 'https://contrib_colormaps.pyviz.org',
})
