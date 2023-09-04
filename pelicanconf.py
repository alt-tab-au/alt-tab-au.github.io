from pelican import readers

AUTHOR = 'alt-tab'
SITENAME = 'alt-tab.au'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Perth'

THEME = 'themes/main'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
DEFAULT_DATE_FORMAT = '%d %b %y'

STATIC_PATHS = ['static', 'posts']
EXTRA_PATH_METADATA = {
	'static/robots.txt': {'path': 'robots.txt'},
	'static/favicon.ico': {'path': 'favicon.ico'},
	'static/img/': {'path': 'img/'},
	'static/CNAME': {'path': 'CNAME'}
}
STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'

MENUITEMS = [
	# linktitle, link (without leading /)
	('about', 'about'),
	('contact', 'contact')
]

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tagged/{slug}/'
TAG_SAVE_AS = 'tagged/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_PAGE_URL = 'drafts/pages/{slug}/'
DRAFT_PAGE_SAVE_AS = 'drafts/pages/{slug}.html'
# disabled:
AUTHOR_SAVE_AS = "" 
AUTHORS_SAVE_AS = ""
TAGS_URL = "tagged/"
TAGS_SAVE_AS = ""

JINJA_ENVIRONMENT = {'line_statement_prefix': '%'}


readers.METADATA_PROCESSORS['extras'] = lambda x, y: (
	[e.strip().split('|') for e in x.split(',')])