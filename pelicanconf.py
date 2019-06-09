#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'maatemantram'
SITENAME = 'మాటేమంత్రం'
SITEURL = 'https://maatemantram.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["tag_cloud"]


THEME='themes/pelican-fresh'
# Theme specific configuration

GOOGLE_CUSTOM_SEARCH = 'your search engine unique ID'

HIDE_CATEGORIES_FROM_MENU = False

# SHARETHIS_PUB_KEY = 'your ShareThis Pub Key'

