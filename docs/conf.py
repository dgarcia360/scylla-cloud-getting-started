# -*- coding: utf-8 -*-
import os
import sys
from datetime import date

from sphinx_scylladb_theme.utils import multiversion_regex_builder

# -- General configuration ------------------------------------------------

# Build documentation for the following tags and branches
TAGS = []
BRANCHES = ["main"]
# Set the latest version.
LATEST_VERSION = "main"
# Set which versions are not released yet.
UNSTABLE_VERSIONS = ["main"]
# Set which versions are deprecated
DEPRECATED_VERSIONS = []

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx_scylladb_theme",
    "sphinx_multiversion",
    "sphinx_sitemap",
    "recommonmark",
    "sphinx_markdown_tables"
]


# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = 'ScyllaDB Cloud Getting Started Documentation'
copyright = str(date.today().year) + ', ScyllaDB. All rights reserved.'
author = u'Scylla Project Contributors'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "sizing.md"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_scylladb_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'conf_py_path': 'docs/',
    'default_branch': 'main',
    'github_issues_repository': 'scylladb/scylla-cloud-getting-started',
    'github_repository': 'scylladb/scylla-cloud-getting-started',
    'hide_edit_this_page_button': 'false',
    'hide_feedback_buttons': 'false',
    'site_description': 'ScyllaDB Cloud Example Documentation',
    "versions_unstable": UNSTABLE_VERSIONS,
    "versions_deprecated": DEPRECATED_VERSIONS,
}

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%d %B %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {'**': ['side-nav.html']}

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScyllaDocumentationdoc'

# URL which points to the root of the HTML documentation. 
html_baseurl = 'https://scylla-getting-started.scylladb.com'

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {'html_baseurl': html_baseurl}

# A list of paths that contain custom static files. 
# They are copied to the output’s _static directory.
html_static_path = ["_static"]

# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template = "404.html"

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ""

# -- Options for sitemap extension ---------------------------------------

sitemap_url_scheme = "/stable/{link}"

# -- Options for multiversion --------------------------------------------

# Whitelist pattern for tags
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Defines which version is considered to be the latest stable version.
smv_latest_version = LATEST_VERSION
# Defines the new name for the latest version.
smv_rename_latest_version = "stable"
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r"^tags/.*$"
# Format for versioned output directories inside the build directory
smv_outputdir_format = "{ref.name}"
