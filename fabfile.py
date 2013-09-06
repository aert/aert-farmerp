from fabric.api import local, task, lcd
from fabric import colors


@task
def run_tests():
    """ Run test suite """
    local('py.test sources')


@task
def build_clean():
    """ Delete build dir content & pyc files """
    local('rm -rf build/*')
    local('pyclean .')


@task
def build_wheel():
    """ Create new wheel file """
    with lcd('deploy/fabric'):
        local('fab build.wheel')


@task
def vagrant_run_ansible():
    """ Start vagrant and run top.yml """
    print colors.yellow("[ Starting vagrant... ]")
    local('vagrant up')
    print colors.yellow("[ Running ansible playbooks... ]")
    with lcd('deploy/ansible'):
        local('ansible-playbook -i hosts/vagrant top.yml -v')


@task
def vagrant_init():
    """ Destroy vagrant & recreate it """
    print colors.yellow("[ Initializing vagrant... ]")
    local('vagrant destroy')
    local('vagrant up')

    print colors.yellow("[ Running fabric tasks... ]")
    with lcd('deploy/fabric'):
        local('fab staging.h_vagrant staging.setup_ssh_vagrant')
