ENVIRONMENT = 'development'
SECRET_KEY = "{{ secret_key }}"
SQL_PARAMS = {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': 'dev.db',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }

# Use this for any settings that are specific to this one installation, such as developer API keys.
# local.py should not be checked in to version control.

# EMBEDLY_KEY = 'get-one-from-http://embed.ly/'
# GOOGLE_MAPS_KEY = 'get-one-from-https://code.google.com/apis/console/?noredirect'


# When developing Wagtail templates, we recommend django-debug-toolbar
# for keeping track of page rendering times. To use it:
#     pip install django-debug-toolbar==1.0.1
# and uncomment the lines below.

# from .base import INSTALLED_APPS, MIDDLEWARE_CLASSES
INSTALLED_APPS = [
    # 'debug_toolbar',
]

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS = [
]

# django-debug-toolbar settings
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


# If you're developing Wagtail itself (as opposed to building a Wagtail-powered site), you'll
# want to tweak the Python path so that it picks up your working copy of the Wagtail code
# rather than the packaged copy - uncomment the lines below to do that.
# Here we assume that you have it in a 'wagtail' directory at the same level as your
# '{{ project_name }}' checkout - adjust the path as appropriate.

# import sys
# import os
# PATH_TO_WAGTAIL = os.path.join(os.path.dirname(__file__), '..', 'wagtail')
# sys.path.insert(1, PATH_TO_WAGTAIL)
