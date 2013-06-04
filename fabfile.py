from fabric.api import *

SETTINGS_FORMAT = 'aert_bookkeeping_site.settings.{}'


@task
def runserver(env="local"):
    run_admin('runserver', env)

@task
def syncdb(env="local"):
    run_admin('syncdb', env)

@task
def validate(env="local"):
    run_admin('validate', env)

def run_admin(cmd, env):
    settings=SETTINGS_FORMAT.format(env)
    local('django-admin.py {} --settings={}'\
          .format(cmd, settings))
