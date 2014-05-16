import sys, os
#INTERP = "YOUR/VIRTUALENV/HERE"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append('') # YOUR PROJECT ROOT HERE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(application, debug=True)
