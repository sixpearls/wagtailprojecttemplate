from {{ project_name }}.settings.base import *

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': '{{ project_name }}',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

ALLOWED_HOSTS = [
    '.HOST.com', # Allow domain and subdomains
    '.HOST.com.', # Also allow FQDN and subdomains
]

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    "default": local.SQL_PARAMS
}

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': '{{ project_name }}'
    }
}

INSTALLED_APPS += (
    'djcelery',
    'kombu.transport.django',
    'gunicorn',    
)

# CELERY SETTINGS
import djcelery
djcelery.setup_loader()

BROKER_URL = 'redis://'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

