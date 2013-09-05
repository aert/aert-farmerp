import os
from invoke import run, task


@task
def clean():
    run('rm -rf build/*')
    run('pyclean .')


@task
def test():
    run('py.test', pty=True)


@task
def deploy_vagrant():
    print("[ Starting vagrant... ]")
    run('vagrant up', pty=True)
    print("[ Running ansible playbooks... ]")
    cwd = os.getcwd()
    os.chdir('deploy/ansible')
    run('ansible-playbook -i hosts/vagrant top.yml -v', pty=True)
    os.chdir(cwd)


@task
def bootstrap_vagrant():
    print("[ Initializing vagrant... ]")
    run('vagrant destroy')
    run('vagrant up', pty=True)

    print("[ Running fabric tasks... ]")
    cwd = os.getcwd()
    os.chdir('deploy/fabric')
    run('fab dev.h_vagrant dev.setup_ssh_vagrant', pty=True)
    os.chdir(cwd)
