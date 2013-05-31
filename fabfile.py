from fabric.api import *

SETTINGS_FORMAT = 'aert_bookkeeping_site.settings.{}'

@task
def runserver(env="local"):
    settings=SETTINGS_FORMAT.format(env)
    local('django-admin.py runserver --settings={}'\
          .format(settings))

@task
def syncdb(env="local"):
    settings=SETTINGS_FORMAT.format(env)
    local('django-admin.py syncdb --settings={}'\
          .format(settings))

