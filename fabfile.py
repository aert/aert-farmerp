from fabric.api import local, task, lcd
from fabric import colors


@task
def init_env_local():
    """ Setup development env. """
    local('pip install -r deploy/requirements/local.txt')

    with lcd('sources'):
        local('add2virtualenv `pwd`')

    local("sudo npm install -g less")
    local("sudo npm install -g coffee-script")


@task
def init_env_vagrant():
    """ Re-create & configure vagrant vm. """
    _vagrant_init()
    _vagrant_run_ansible()


@task
def run_tests():
    """ Run test suite. """
    local('py.test sources')


@task
def clean():
    """ Delete build & public dir. """
    local('rm -rf docs/build/*')
    local('rm -rf build/*')
    local('rm -rf public/assets/*')
    local('pyclean .')


@task
def build_wheel():
    """ Create new wheel file. """
    with lcd('deploy/fabric'):
        local('fab build.wheel')


def _vagrant_run_ansible():
    """ Start vagrant and run top.yml. """
    print colors.yellow("[ Starting vagrant... ]")
    local('vagrant up')
    print colors.yellow("[ Running ansible playbooks... ]")
    with lcd('deploy/ansible'):
        local('ansible-playbook -i hosts/vagrant top.yml -v')


def _vagrant_init():
    """ Destroy vagrant & recreate it. """
    print colors.yellow("[ Initializing vagrant... ]")
    local('vagrant destroy')
    local('vagrant up')

    print colors.yellow("[ Running fabric tasks... ]")
    with lcd('deploy/fabric'):
        local('fab staging.h_vagrant staging.setup_ssh_vagrant')
