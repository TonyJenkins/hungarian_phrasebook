# Configuration file for the Sphinx documentation builder.


project = 'The Python Book'
copyright = '2023, Tony Jenkins'
author = 'Tony Jenkins'
release = '0.01'

extensions = [
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']

html_theme = 'sphinx_book_theme'
html_theme_options = {
    'home_page_in_toc': True,
    'repository_url': 'https://github.com/TonyJenkins/hungarian_phrasebook',
    'use_repository_button': True,
    'pygment_light_style': 'igor',
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
html_title = 'The Python Book'

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

latex_logo = '_images/python_britannica.png'
latex_theme = 'manual'
