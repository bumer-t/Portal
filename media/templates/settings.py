import logging
import os.path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import local_settings

PROJECT_ROOT =  os.path.dirname(os.path.realpath(__file__))

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'mallpages.log')
#LOG_FILE = '/home/mallpages/webapps/django/mallpages/mallpages.log'


# Django settings for myproject project.
AUTH_PROFILE_MODULE = 'mpprofile.profile'
#GOOGLE_MAPS_API_KEY = 'ABQIAAAA2Ce8L8AHI-cfyz5bQVbAyBQa_BiYf6I59aGMMA6IAHGk42zKPBSAayai0yRN6gmcid2TzCY--LwlxA'

#GOOGLE_MAPS_API_KEY = 'ABQIAAAA2Ce8L8AHI-cfyz5bQVbAyBSXU4Z8PfBO8N997xbXZyT9yHd20xQNnVOJyVH-biHfmEM5-7LNd5zjJw'
GOOGLE_MAPS_API_KEY = 'ABQIAAAAamUxU8uRKqtrWJvk5Y5AWhQa_BiYf6I59aGMMA6IAHGk42zKPBSO1tRchzZlzZjOQ5nuoLeeJD3atg'

#DEFAULT_FROM_EMAIL = 'register@mallpages.com'
# Used for mail_admins() def

#EMAIL_HOST_USER = 'ratnagiri'
#EMAIL_HOST_PASSWORD = 'dasmail199'

SERVER_EMAIL = 'register@mallpages.com'
#EMAIL_HOST_USER = 'mallpages'
#EMAIL_HOST_PASSWORD = 'p@ssw0rd'
#EMAIL_HOST = 'smtp.webfaction.com'
#EMAIL_PORT = '587'
#EMAIL_USE_TLS = True


EMAIL_HOST = local_settings.email_host
EMAIL_PORT = local_settings.email_port
EMAIL_HOST_USER = local_settings.email_host_user
EMAIL_HOST_PASSWORD = local_settings.email_host_password
EMAIL_USE_TLS = local_settings.email_use_tls
DEFAULT_FROM_EMAIL = local_settings.default_from_email

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = local_settings.admins

MANAGERS = ADMINS

DATABASE_ENGINE = local_settings.db_engine #'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = local_settings.db_name #'mallpages_db'             # Or path to database file if using sqlite3.
DATABASE_USER = local_settings.db_user #'mallpages_db'             # Not used with sqlite3.
DATABASE_PASSWORD = local_settings.db_pass #'ratnagiri'         # Not used with sqlite3.
DATABASE_HOST = getattr(local_settings, 'db_host', '')           # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

#MEDIA_ROOT = '/home/mallpages/webapps/django/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

MEDIA_URL = "/media/" #'http://www.mallpages.com/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sa=!omlnt3$4=(7izw9jiag8z^p&psj85&ub8pd9r7-&m#2bo4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

AUTHENTICATION_BACKENDS = (
    'mallpages.emailauth.emailbackend.EmailBackend',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'mallpages.store.session.GetSessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'captcha.middleware.CaptchaMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'mallpages.urls'


TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        #'/home/mallpages/webapps/django/templates/',
		os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'templates/'),
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.humanize',
    
    'pagination',
    'sorl.thumbnail',
    'django_cron',
    'notification',
    'messages',
    'forum',
    'voting',
    'uni_form',
    'userprofile',    #django-profiles
    'captcha',    #easycaptcha
    'autocomplete',
    'project',
    'oembed',
    
    'mallpages.mpprofile',
    'mallpages.mall',
    'mallpages.store',
    'mallpages.home',
    'mallpages.gallery',
    'mallpages.friends',

    'south',
    
)



TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'mallpages.store.context_processors.store_object',
	'django.contrib.messages.context_processors.messages',
)

FORUM_BASE = '/forum'


# Invite api keys

#YAHOO_CONSUMER_KEY      = "dj0yJmk9OXpEOE9QZld4NEdNJmQ9WVdrOU1GSmpkRmx0TlRJbWNHbzlNakExTXpreE9URTJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD02ZA--"
#YAHOO_CONSUMER_SECRET   = "e3d143f8f519d6f55c4baf96cdabb6ab83cb63bf"
#YAHOO_APPLICATION_ID    = "0RctYm52"
YAHOO_CONSUMER_KEY      = "dj0yJmk9NE5wM01ZcVQ0MXVQJmQ9WVdrOU9VUTBWMk5CTkdVbWNHbzlNemswT0RNeE16WXkmcz1jb25zdW1lcnNlY3JldCZ4PWYz" # for local.bongomagic.com
YAHOO_CONSUMER_SECRET   = "a98e199b88aa995b3d074f715c68aa2b617abfe2" # for local.bongomagic.com
YAHOO_APPLICATION_ID    = 'ZUimiT5g'


# Windows Live config data for domain  .
WINDOWS_APPID = "000000004802F529"
WINDOWS_SECRET = "ITBWTcC2QocUMFfXVgbcldVMAAmEkMBy"

WINDOWS_LIVE_KEYFILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),'windows_live_config.xml')

WALL_GALLERY_NAME = u"Wall Photos"


COMMENTS_APP = "userprofile"

BASE_URL = local_settings.base_url

logging.basicConfig(filename=LOG_FILE,level=logging.DEBUG)

from local_settings import *
DAYS_PRODUCT_IS_NEW_FOR = 60
SESSION_COOKIE_AGE = 86400
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


DEBUG_PROPAGATE_EXCEPTIONS=False