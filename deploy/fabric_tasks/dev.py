from os.path import join, basename
from os import environ
import hashlib

from fabric.api import *
from fabric import colors


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
    sudo("passwd root")
    sudo("apt-get update")
    local("ssh-copy-id root@192.168.111.222")
