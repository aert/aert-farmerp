from fabric.api import *

# Other
SETTINGS_FORMAT = 'aert_bookkeeping_site.settings.{}'


@task
def manage_py(command, env="local"):
    """ Runs a manage.py command on the server """
    settings = SETTINGS_FORMAT.format(env)
    cmd = 'django_admin.py {command} --settings={settings}'
    run(cmd.format(command=command,
                   settings=settings))


@task
def syncdb(env="local"):
    """ Django syncdb command."""
    manage_py("syncdb --noinput", env)


@task
def migrate(env="local"):
    """ Django South migrate command."""
    manage_py("migrate", env)
