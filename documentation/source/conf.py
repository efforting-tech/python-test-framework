import sys
sys.path.insert(0, '.')	#This hack makes sure we use local modules before site modules (and unfortunately also core modules, we should make a better solution for this, like preventing sphinx from using the site packages at all)

import git

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Efforting.Tech Python Testing Framework'
copyright = '2022, Mikael Lövqvist'
author = 'Mikael Lövqvist'

# The full version, including alpha/beta/rc tags
release = git.get_branch()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	"sphinx.ext.autodoc",
	"sphinx.ext.intersphinx",
	"efforting_sphinx_extensions",
    #'sphinx_collapse',  #https://github.com/dgarcia360/sphinx-collapse
	#"sphinx_paramlinks",	This is third party that we don't have installed
#	"sphinx.ext.linkcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = 'efforting.tech-header.svg'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#NOTE: https://github.com/pydata/pydata-sphinx-theme/blob/355fe0b39613b14c7833845c43d378e7791ff3c2/docs/user_guide/version-dropdown.rst

html_theme_options = dict(
    switcher = dict(
        json_url = 'https://docs.efforting.tech/python-testing-framework/versions.json',
        version_match = release,
    ),
    navbar_start = ['navbar-logo', 'version-switcher'],
)

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

add_module_names = False

html_baseurl = f'/python-testing-framework/{release}'

import sys
from pathlib import Path
#Paths are relative to source
#TODO - this should be different and this should be a git submodule
sys.path.append(str(Path('../../efforting-sphinx-extensions').resolve()))

