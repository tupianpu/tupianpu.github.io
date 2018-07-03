#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'johnny'
SITENAME = u'\u7684 \u5409\u4ed6\u8c31 \u7f51\u7ad9'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('飞飞机', 'http://feifeiji.com/'),
         ('图片谱', 'http://tupianpu.com/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images']
THEME = 'new-bootstrap'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
