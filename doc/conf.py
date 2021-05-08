#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# scikit-survival documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import inspect
import os
from pathlib import Path
import re
import sys

from nbconvert.preprocessors import Preprocessor
import nbsphinx
from setuptools_scm import get_version

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
# https://docs.readthedocs.io/en/latest/faq.html?highlight=environ#how-do-i-change-behavior-for-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
if on_rtd:
    sys.path.insert(0, os.path.abspath(os.path.pardir))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'nbsphinx',
]

autosummary_generate = True
autodoc_default_options = {
    'members': None,
    'inherited-members': None,
}

# Napoleon settings
napoleon_google_docstring = False
napoleon_include_init_with_doc = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'scikit-survival'
copyright = '2015-2021, Sebastian Pölsterl'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
if on_rtd:
    release = get_version(root='..', relative_to=__file__)
else:
    import sksurv
    release = sksurv.__version__

# The short X.Y.Z version.
version = '.'.join(release.split('.')[:3])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# The default language to highlight source code in.
highlight_language = 'none'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**/README.*', 'Thumbs.db', '.DS_Store']

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
# pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


nbsphinx_execute = 'never'

nbsphinx_prolog = r"""
{% set docname = "doc/" + env.doc2path(env.docname, base=None) %}
{% set notebook = env.doc2path(env.docname, base=None)|replace("user_guide/", "notebooks/") %}
{% set branch = 'master' if 'dev' in env.config.release else 'v{}'.format(env.config.release) %}

.. raw:: html

    <div class="admonition note" style="line-height: 150%;">
      This page was generated from
      <a class="reference external" href="https://github.com/sebp/scikit-survival/blob/{{ branch|e }}/{{ docname|e }}">{{ docname|e }}</a>.<br/>
      Interactive online version:
      <span style="white-space: nowrap;"><a href="https://mybinder.org/v2/gh/sebp/scikit-survival/{{ branch|e }}?urlpath=lab/tree/{{ notebook|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>.</span>
    </div>
"""


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_url": "https://github.com/sebp/scikit-survival",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "scikit-survival {0}".format(version)

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

html_css_files = ['custom.css']
html_js_files = ['buttons.js']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object

    Adapted from scipy.
    """
    import sksurv

    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except AttributeError:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except TypeError:
        fn = None
    if fn is None and hasattr(obj, '__module__'):
        fn = inspect.getsourcefile(sys.modules[obj.__module__])
    if fn is None:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except ValueError:
        lineno = None

    if lineno:
        linespec = '#L%d-L%d' % (lineno, lineno + len(source) - 1)
    else:
        linespec = ''

    startdir = Path(sksurv.__file__).parent.parent.absolute()
    if not fn.startswith(str(startdir)):  # not in sksurv
        return None
    fn = '/'.join(Path(fn).relative_to(startdir).parts)

    if fn.startswith('sksurv/'):
        m = re.match(r'^.*dev[0-9]+\+g([a-f0-9]+)$', release)
        if m:
            branch = m.group(1)
        elif 'dev' in release:
            branch = 'master'
        else:
            branch = 'v{}'.format(release)
        return 'https://github.com/sebp/scikit-survival/blob/{branch}/{filename}{linespec}'.format(
            branch=branch,
            filename=fn,
            linespec=linespec
        )
    else:
        return None


class RTDUrlPreprocessor(Preprocessor):
    """Convert URLs to RTD in notebook to relative urls."""
    URL_PATTERN = re.compile(
        r'\(https://scikit-survival\.readthedocs\.io/.+?/.+?/([-._a-zA-Z0-9/]+)/(.+?)\.html.*?\)'
    )
    DOC_DIR = Path(__file__).parent

    def preprocess_cell(self, cell, resources, index):
        # path of notebook directory, relative to conf.py
        nb_path = Path(resources['metadata']['path']).relative_to(self.DOC_DIR)
        to_root = [os.pardir] * len(nb_path.parts)

        if cell.cell_type == 'markdown':
            text = cell.source
            replace = []
            for match in self.URL_PATTERN.finditer(text):
                path = to_root[:]
                path.append(match.group(1))

                rel_url = "/".join(path)
                filename = match.group(2)
                replace.append((match.group(0), '({}/{}.rst)'.format(rel_url, filename)))

            for s, r in replace:
                text = text.replace(s, r)
            cell.source = text
            return cell, resources
        return cell, resources


def _from_notebook_node(self, nb, resources, **kwargs):
    filters = [RTDUrlPreprocessor(), ]
    for f in filters:
        nb, resources = f.preprocess(nb, resources=resources)

    return nbsphinx_from_notebook_node(self, nb, resources=resources, **kwargs)


# see https://github.com/spatialaudio/nbsphinx/issues/305#issuecomment-506748814-permalink
nbsphinx_from_notebook_node = nbsphinx.Exporter.from_notebook_node
nbsphinx.Exporter.from_notebook_node = _from_notebook_node


# ------------------------
# Mock dependencies on RTD
# ------------------------


if on_rtd:
    MOCK_MODULES = [
        # external dependencies
        'ecos',
        'joblib',
        'numexpr',
        'numpy',
        'osqp',
        'pandas',
        'pandas.api.types',
        'scipy',
        'scipy.integrate',
        'scipy.io.arff',
        'scipy.linalg',
        'scipy.optimize',
        'scipy.sparse',
        'scipy.special',
        'scipy.stats',
        'sklearn',
        'sklearn.base',
        'sklearn.dummy',
        'sklearn.ensemble',
        'sklearn.ensemble._base',
        'sklearn.ensemble._forest',
        'sklearn.ensemble._gb',
        'sklearn.ensemble._gb_losses',
        'sklearn.ensemble._gradient_boosting',
        'sklearn.ensemble.base',
        'sklearn.ensemble.forest',
        'sklearn.ensemble.gradient_boosting',
        'sklearn.exceptions',
        'sklearn.externals.joblib',
        'sklearn.linear_model',
        'sklearn.metrics',
        'sklearn.metrics.pairwise',
        'sklearn.model_selection',
        'sklearn.pipeline',
        'sklearn.preprocessing',
        'sklearn.svm',
        'sklearn.tree',
        'sklearn.tree._classes',
        'sklearn.tree._splitter',
        'sklearn.tree._tree',
        'sklearn.tree.tree',
        'sklearn.utils',
        'sklearn.utils._joblib',
        'sklearn.utils.extmath',
        'sklearn.utils.fixes',
        'sklearn.utils.metaestimators',
        'sklearn.utils.validation',
        # our C modules
        'sksurv.bintrees._binarytrees',
        'sksurv.ensemble._coxph_loss',
        'sksurv.kernels._clinical_kernel',
        'sksurv.linear_model._coxnet',
        'sksurv.svm._minlip',
        'sksurv.svm._prsvm',
        'sksurv.tree._criterion']

    MOCK_VERSIONS = {
        'pandas': '0.25.0',
        'sklearn': '0.22.0',
    }

    from unittest.mock import Mock

    class MockModule(Mock):
        """mock imports"""

        @classmethod
        def __getattr__(cls, name):
            if name in ('__file__', '__path__'):
                return '/dev/null'
            elif name[0] == name[0].upper() and name[0] != "_":
                # Not very good, we assume Uppercase names are classes...
                mocktype = type(name, (), {})
                mocktype.__module__ = __name__
                return mocktype
            else:
                return MockModule()

    sys.modules.update((mod_name, MockModule()) for mod_name in MOCK_MODULES)
    for mod, ver in MOCK_VERSIONS.items():
        setattr(sys.modules[mod], '__version__', ver)
