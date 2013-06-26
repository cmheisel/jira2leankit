"""sphinx config"""
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'jira2leankit'
copyright = u'2013, Chris Heisel'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'jira2leankitdoc'


# -- Options for LaTeX output -----------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

latex_documents = [
    ('index', 'jira2leankit.tex', u'jira2leankit Documentation',
     u'Chris Heisel', 'manual'),
]

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'jira2leankit', u'jira2leankit Documentation',
     [u'Chris Heisel'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'jira2leankit', u'jira2leankit Documentation',
     u'Chris Heisel', 'jira2leankit', 'One line description of project.',
     'Miscellaneous'),
]
