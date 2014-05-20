"""Management utilities."""


from fabric.contrib.console import confirm
from fabric.api import abort, env, local, settings, task
import os
import local as local_setting

django_base_settings = __import__('Angelina.settings.%s' % local_setting.ENVIRONMENT, fromlist=[''])

if getattr(django_base_settings,'USE_HEROKU',False):
    env.run = 'heroku run python manage.py'
    import fabfiles.heroku
else:
    env.run = 'python manage.py '

import socket

########## HELPERS
def cont(cmd, message):
    """Given a command, ``cmd``, and a message, ``message``, allow a user to
    either continue or break execution if errors occur while executing ``cmd``.

    :param str cmd: The command to execute on the local system.
    :param str message: The message to display to the user on failure.

    .. note::
        ``message`` should be phrased in the form of a question, as if ``cmd``'s
        execution fails, we'll ask the user to press 'y' or 'n' to continue or
        cancel exeuction, respectively.

    Usage::

        cont('heroku run ...', "Couldn't complete %s. Continue anyway?" % cmd)
    """
    with settings(warn_only=True):
        result = local(cmd, capture=True)

    if message and result.failed and not confirm(message):
        abort('Stopped execution per user request.')

@task
def manage(cmd):
    """
    Run django management commands.
    fab manage:command 
    """
    local('%(run)s %(cmd)s' % {'run': env.run, 'cmd': cmd})

@task
def backup(output='initial_data.json'):
    """
    Backup data, exclude auth.Permisisons and 
    """
    local('%(run)s dumpdata --indent=4 --natural --exclude=auth.Permission --exclude=contenttypes%(out)s' % {'run': env.run, 'out': ' > ' + output if output != '' else ''})

@task
def pubserver(port='8000'):
    manage('runserver %(ip)s:%(port)s' % { 'ip': socket.gethostbyname_ex(socket.gethostname())[-1][0], 'port': port })

@task
def serve(): #within vagrant
    manage('runserver 0.0.0.0:8000')

@task
def shell():
    """ Run shell_plus if able, otherwise shell """
    if 'django_extensions' in django_base_settings.INSTALLED_APPS:
        manage('shell_plus')
    else:
        manage('shell')
########## END HELPERS


########## DATABASE MANAGEMENT
@task
def startdb():
    """Start a databse by running syncdb --all and then migrate --fake"""
    local('%(run)s syncdb --all --noinput' % env)
    local('%(run)s migrate --fake --noinput' % env)

@task
def syncdb():
    """Run a syncdb."""
    local('%(run)s syncdb --noinput' % env)

@task
def migrate(app=None):
    """Apply one (or more) migrations. If no app is specified, fabric will
    attempt to run a site-wide migration.

    :param str app: Django app name to migrate.
    """
    if app:
        local('%s migrate %s --noinput' % (env.run, app))
    else:
        local('%(run)s migrate --noinput' % env)
########## END DATABASE MANAGEMENT


########## FILE MANAGEMENT
@task
def collectstatic():
    """Collect all static files, and copy them to S3 for production usage."""
    local('%(run)s collectstatic --noinput --ignore "*.less"' % env)
########## END FILE MANAGEMENT

