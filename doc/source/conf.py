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
html_title = 'The Python Book'

smartquotes = True
