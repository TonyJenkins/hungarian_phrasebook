# Configuration file for the Sphinx documentation builder.


project = 'Python Book'
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
}

html_logo = "_images/python-powered-h-140x182.png"

html_title = 'The Python Book'

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

latex_logo = html_logo
