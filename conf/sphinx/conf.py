# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Writing Precisely'
copyright = '2026 Borys Belinsky (borys.belinsky@protonmail.com). Content licensed under CC BY 4.0.'
author = 'Borys Belinsky'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['templates']
exclude_patterns = ['drafts']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'breeze'
html_title = "Writing • Precisely"
# html_theme_options = {'header_tabs': False}
html_static_path = ['static']
