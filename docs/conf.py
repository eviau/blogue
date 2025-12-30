# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'eviau'
copyright = '2022, Edith Viau'
author = 'Edith Viau'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['ablog']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

blog_baseurl = "https://www.eviau.net/blogue"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "edith viau: documentation"
html_theme = 'theme'
html_theme_path = ['.']
html_static_path = ['_static']

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

blog_authors = {
    'Édith Viau': ('Édith viau', 'http://eviau.net')}
