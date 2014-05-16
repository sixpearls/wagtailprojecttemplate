import os

from {{ project_name }}.settings.base import *

INSTALLED_APPS += [
    'django_extensions',
]

DEBUG = TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8111'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "dev.db"),
    },
}
