#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OpenNebula documentation build configuration file, created by
# sphinx-quickstart on Wed Dec  4 12:12:49 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import yaml

import sphinx_rtd_theme

sys.path.append(os.path.abspath('ext'))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.graphviz',
              'sphinx.ext.todo',
              'versions',
              'sphinx-prompt',
              'sphinx_substitution_extensions']

todo_include_todos = False

site_conf = yaml.safe_load(open('site_conf.yml').read())

versions  = site_conf['versions']

github_version = 'master/'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OpenNebula'
copyright = '2023, OpenNebula Team <contact@opennebula.io>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '6.8'
# The full version, including alpha/beta/rc tags.
release = '6.8.0'
# The context packages released version
context_release = '6.6.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Github path
github_repo   = "https://github.com/OpenNebula/docs"
github_branch = "master"

# i18n
locale_dirs = ['locale/']
gettext_compact = False

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'logo_only': True}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "opennebula-white.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'css/opennebula.css'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': [],
    '**': ['alltoc.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenNebuladoc'

# -- Options for LaTeX output --------------------------------------------------

guide_main_title = "OpenNebula %s " % (version,)
file_main_title  = "opennebula_%s_" % (version,)
latex_author     = "OpenNebula Systems"

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',
'classoptions': ',openany,oneside',
'babel': '\\usepackage[english]{babel}',
'maketitle': '\\maketitle\nThis document is being provided by OpenNebula Systems under the Creative Commons Attribution-NonCommercial-Share Alike License.\\newline{}\\newline{}THE DOCUMENT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE DOCUMENT.'
# Additional stuff for the LaTeX preamble.
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
# WARNING: This is outdated!!
latex_documents = [
  ( 'intro_release_notes/index',
    file_main_title  + 'intro_release_notes.tex',
    guide_main_title + 'Introduction and Release Notes',
    latex_author,
    'manual'),

  ( 'deployment/index',
    file_main_title  + 'deployment_guide.tex',
    guide_main_title + 'Deployment guide',
    latex_author,
    'manual'),

  ( 'operation/index',
    file_main_title  + 'operation_guide.tex',
    guide_main_title + 'Operation Guide',
    latex_author,
    'manual'),

  ( 'advanced_components/index',
    file_main_title  + 'advanced_components_guide.tex',
    guide_main_title + 'Advanced Components Guide',
    latex_author,
    'manual'),

  ( 'integration/index',
    file_main_title  + 'integration_guide.tex',
    guide_main_title + 'Integration Guide',
    latex_author,
    'manual'),
]

latex_logo = "_static/opennebula.png"

# The name of an image file (relative to this directory) to place at the top of
# the title page.

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'opennebula', 'OpenNebula Documentation',
     ['OpenNebula Team <contact@opennebula.org>'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'OpenNebula', 'OpenNebula Documentation',
   'OpenNebula Team <contact@opennebula.org>', 'OpenNebula', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

rst_prolog = """
 .. |release| replace:: {release}
 .. |version| replace:: {version}
 .. |context_release| replace:: {context_release}
""".format(
        release=release,
        version=version,
        context_release=context_release)
