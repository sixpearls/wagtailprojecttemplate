import os, sys, imp

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))

local = imp.load_source('local',os.path.join(PROJECT_ROOT,'local.py'))
SECRET_KEY = local.SECRET_KEY

# Put your name
MANAGERS = ADMINS = [ ('admin', 'admin@example.com'),]
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

SITE_ID = 1

USE_I18N = True
USE_L10N = True

TIME_ZONE = "America/Los_Angeles"
LANGUAGE_CODE = "en-us"

# Media settings to handle user uploaded files
MEDIA_ROOT_PREFIX = os.path.join(PROJECT_ROOT, 'public/media')
MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'uploads')

MEDIA_URL_PREFIX = "/media/"
MEDIA_URL = '%suploads/' % MEDIA_URL_PREFIX

# These are for site static media (e.g. CSS and JS)
# This one is where static content is collected to.
STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')    
STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "{{ project_name }}/static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
    # "django.contrib.staticfiles.finders.DefaultStorageFinder",
]

# Template stuff   
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",    
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
) + local.MIDDLEWARE_CLASSES

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "{{ project_name }}/templates"),
] + local.TEMPLATE_DIRS


ROOT_URLCONF = "{{ project_name }}.urls"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            'filters': ['require_debug_false'],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    # "django.contrib.sites", 

    'compressor',
    'taggit',
    'modelcluster',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsites',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',

    'website',

] + local.INSTALLED_APPS

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = ""
EMAIL_HOST_PASSWORD = ""

WAGTAIL_SITE_NAME = '{{ project_name|lower }}'

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/less', 'lessc {infile} {outfile}'),
)

# Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'
