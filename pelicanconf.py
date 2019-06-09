#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'maatemantram'
SITENAME = 'మాటేమంత్రం'
# SITEURL = 'https://maatemantram.com'
SITEURL = 'http://localhost:8000'


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


STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


''' We have the option to define where Pelican should look for our blog's pages. 
By default Pelican expects them to be in the content/pages folder. 
It is not necessary to state the path but it is a good practice to do so. '''
# PAGE_PATHS = ['pages']

'''To change the URL to show the content type and date as well. 
The ARTICLE_URL variable states what should display in the web browser's address bar 
while the ARTICLE_SAVE_AS variable defines where the article being generated should be output to.
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/' '''
USE_FOLDER_AS_CATEGORY = True

# ARTICLE_PATHS = ['articles',]
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'


THEME='themes/pelican-fresh'
# Theme specific configuration

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["tag_cloud"]


# GOOGLE_CUSTOM_SEARCH = 'your search engine unique ID'

HIDE_CATEGORIES_FROM_MENU = True

# SHARETHIS_PUB_KEY = 'your ShareThis Pub Key'

