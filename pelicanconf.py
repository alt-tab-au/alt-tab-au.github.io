AUTHOR = 'alt-tab'
SITENAME = 'alt-tab.au'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Perth'

THEME = 'themes/main'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
DEFAULT_DATE_FORMAT = '%d %b %y'

STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {
	'static/robots.txt': {'path': 'robots.txt'},
	'static/favicon.ico': {'path': 'favicon.ico'},
	'static/img/': {'path': 'img/'}
}
STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'

MENUITEMS = [
	('about', 'about'),
	('contact', 'contact')
]

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tagged/{slug}/'
TAG_SAVE_AS = 'tagged/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_PAGE_URL = 'drafts/pages/{slug}/'
DRAFT_PAGE_SAVE_AS = 'drafts/pages/{slug}.html'
AUTHOR_SAVE_AS = "" # disabled

JINJA_ENVIRONMENT = {'line_statement_prefix': '%'}
