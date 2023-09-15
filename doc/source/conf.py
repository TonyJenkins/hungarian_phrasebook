# Configuration file for the Sphinx documentation builder.

project = 'Yet Another Python Book'
copyright = '2023, Tony Jenkins'
author = 'Tony Jenkins'
release = '0.5beta'

web = 'http://www.tony-jenkins.org.uk/'

rst_epilog = '.. |web| replace:: %s' % web

extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = []

autosectionlabel_prefix_document = True

html_static_path = ['_static']

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'home_page_in_toc': True,
    'repository_url': 'https://github.com/TonyJenkins/hungarian_phrasebook',
    'use_repository_button': True,
    'pygment_light_style': 'xcode',
    'pygment_dark_style': 'nord',
    'primary_sidebar_end': [
        'indices.html',
    ],
    'use_sidenotes': True,
    'logo': {
        'image_light': '_images/python_britannica_small.png',
        'image_dark': '_images/python_britannica_inverted_small.png',
    },
}

html_last_updated_fmt = "%A %d %B, %Y"
# html_logo = "_images/python_britannica.png"
html_title = 'Yet Another Python Book'

html_use_index = True
html_split_index = True

copybutton_exclude = '.linenos, .gp'

smartquotes = True

latex_elements = {
    'papersize' : 'a4paper',
    'pointsize' : '11pt',
    'preamble': r'''
        \usepackage{bitter}
        \usepackage[defaultsans]{lato}
        \usepackage{cascadia-code}
    ''',
}

latex_show_urls = 'footnote'

latex_logo = '_static/python_britannica_cover.png'
latex_theme = 'manual'
