from {{ project_name }}.settings.base import *

CACHES = {
    'default': {
        # Uncomment below for memcached cache
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',

        # Uncomment below for redis cache
        # 'BACKEND': 'redis_cache.cache.RedisCache',
        # 'LOCATION': '127.0.0.1:6379',
        # 'KEY_PREFIX': '{{ project_name }}',
        # 'OPTIONS': {
        #     'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Uncomment below to setup ElasticSearch
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
#         'INDEX': '{{ project_name }}'
#     }
# }

INSTALLED_APPS += (
    # 'kombu.transport.django', # a messaging service that can be used with celery
    # 'gunicorn', # a server service
)
