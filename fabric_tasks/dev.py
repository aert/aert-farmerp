from fabric.api import *
from fabric import colors
from fabtools.python import virtualenv
from os import path

import os, hashlib

# Local paths
LOCAL_ROOT = path.dirname(path.dirname(os.path.realpath(__file__)))
VENV_PATH = "/home/ari/Dev/Envs/aert-bookkeeping"


# Server paths
PROJECT_NAME = "aert_bookkeeping"

WHEEL_PATH = path.join(LOCAL_ROOT, "wheel")
WHEEL_NAME = "wheel-requirements.tar.gz"

# Other
SETTINGS_FORMAT = 'aert_bookkeeping_site.settings.{}'
REQUIRE_FORMAT = 'requirements/{}.txt'

def _md5_for_file(filename, block_size=2**20):
    f = open(filename)
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.close()
    return md5.hexdigest()

@task
def make_wheel(env='staging'):
    """ Create new wheel requirements file """
    require_path = path.join(LOCAL_ROOT,
                             REQUIRE_FORMAT.format(env))

    with prefix('. {}/bin/activate'.format(VENV_PATH)):
        # Get all the requirements
        print colors.green("Downloading and compiling requirements. This could take several minutes...")
        local('pip wheel --wheel-dir={wheel} -r {require_path}'\
                               .format(wheel=WHEEL_PATH + '/' + PROJECT_NAME,
                                       require_path=require_path))

    # Zip up
    print colors.green("Zipping all the requirements into one file...")
    with lcd(WHEEL_PATH):
        local('tar czf {name} {project}/'.format(name=WHEEL_NAME,
                                                 project=PROJECT_NAME))

    # Create a MD5
    md5 = _md5_for_file(WHEEL_PATH + '/' + WHEEL_NAME)
    print colors.green('Upload the requirements and set the following MD5 in your pillar configuration: {md5}'.format(md5=md5))
