from fabric.api import *

@task
def runserver(env="local"):
    settings='aert_bookkeeping.settings.{}'.format(env)
    local('django-admin.py runserver --settings={}'\
          .format(settings))
