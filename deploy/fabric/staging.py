from fabric.api import local, sudo, task, env


@task
def h_vagrant():
    "Use Vagrant for testing"
    env.user = 'vagrant'
    env.hosts = ['192.168.111.222']

    # retrieve the IdentityFile:
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1].replace('"', '')  # parse IdentityFile


@task
def setup_ssh_vagrant():
    "Set up vagrant"
    sudo("echo 'root:root' | chpasswd")
    sudo("apt-get update")
    local("sshpass -p root ssh-copy-id root@192.168.111.222")
