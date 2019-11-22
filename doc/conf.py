# noqa
from nbsite.shared_conf import *

project = u'contrib_colormaps'
authors = u'PyViz authors'
copyright = u' 2019, ' + authors
description = 'Collection of user-contributed colormaps.'

import contrib_colormaps
version = release = contrib_colormaps.__version__

html_static_path += ['_static']
html_favicon = '_static/favicon.ico'
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'page_width': '100%',
    'font_family': "Ubuntu, sans-serif",
    'font_size': '0.9em',
    'link': '#347ab4',
    'link_hover': '#1c4669',
    'extra_nav_links': {
        'Github': 'https://github.com/pyviz/contrib_colormaps',
    },
    'show_powered_by': False,
}

extensions += ['nbsite.gallery']

nbsite_gallery_conf = {
    'github_org': 'pyviz',
    'github_project': 'contrib_colormaps',
    'galleries': {
        'colormaps': {
            'title': 'Colormaps',
            'intro': 'Gallery of colormaps included in contrib_colormaps'
        }
    },
}

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # WEBSITE_SERVER is optional for tests and local builds, but allows defining a canonical URL for search engines
    'WEBSITE_SERVER': 'https://contrib_colormaps.pyviz.org',
})
