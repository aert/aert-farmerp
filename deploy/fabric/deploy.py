from os.path import join, basename
from os import environ
import hashlib

from fabric.api import *
from fabric import colors


# Local paths
VENV_ENV = environ['VIRTUAL_ENV']
VENV_PROJECT = join(environ['PROJECT_HOME'], basename(VENV_ENV))


# Server paths
PROJECT_NAME = "aert_bookkeeping"

WHEEL_TMP_PATH = join(VENV_PROJECT, "build", "wheel")
WHEEL_DEPLOY_PATH = join(VENV_PROJECT, "build")
WHEEL_NAME = "{}_wheel-reqs.tar.gz".format(PROJECT_NAME)

# Other
SETTINGS_FORMAT = 'aert_bookkeeping_site.settings.{}'
REQUIRE_PATH_FMT = 'deployment/requirements/{}.txt'


def _md5_for_file(filename, block_size=2 ** 20):
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
    require_path = join(VENV_PROJECT,
                        REQUIRE_PATH_FMT.format(env))

    with prefix('. {}/bin/activate'.format(VENV_ENV)):
        # Get all the requirements
        print colors.green("Downloading and compiling requirements."
                           "This could take several minutes...")
        local('pip wheel --wheel-dir={wheel} -r {require_path}'
              .format(wheel=WHEEL_TMP_PATH + '/' + PROJECT_NAME,
              require_path=require_path))

    # Zip up
    print colors.green("Zipping all the requirements into one file...")
    with lcd(WHEEL_TMP_PATH):
        local('tar czf {name} {project}/'.format(name=WHEEL_NAME,
                                                 project=PROJECT_NAME))
        local('mv {name} {deploy_path}/{name}'
              .format(name=WHEEL_NAME, deploy_path=WHEEL_DEPLOY_PATH))

    # Remove working dir
    local('rm -rf {}'.format(WHEEL_TMP_PATH))

    # Create a MD5
    wheel_archive = join(WHEEL_DEPLOY_PATH, WHEEL_NAME)
    md5 = _md5_for_file(wheel_archive)
    with open(wheel_archive + ".md5", "a") as out:
        out.write(md5)
    print colors.green("Upload the requirements and set the following MD5 in"
                       " your pillar configuration: {md5}".format(md5=md5))
