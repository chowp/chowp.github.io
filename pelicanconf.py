#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'alchemy'
AUTHOR = u'peichanghua'
SITENAME = u'our418.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DISQUS_SITENAME = 'our418'
DEFAULT_LANG = u'cn'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGES_ON_MENU = True
PROFILE_IMAGE = '/images/1.svg width="200" height="200"'
SHOW_ARTICLE_AUTHOR = None
SITE_SUBTEXT = 'keep fit, keep happy'
META_DESCRIPTION = '''This is the record of the travel in life!'''

EXTRA_FAVICON = True


MENU_ITEMS = (
    ('E-mail', ''),
)





# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
 #        ('Jinja2', 'http://jinja.pocoo.org/'),
  #       ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
GITHUB_ADDRESS = 'https://github.com/chowp'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
