import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires_base = [
    'Django==1.5.4',
    'django-braces==1.2.2',
    'django-model-utils==1.5.0',
    'South==0.8.2',
    'psycopg2==2.5.1',
    'django-compressor==1.3',
    'django-grappelli==2.4.6',
]

requires_dev = [
    'bpython',
    'Fabric==1.8.0',
    'fabtools==0.15.0',
    'django-debug-toolbar==0.9.4',
    # Build tools
    'wheel==0.22.0',
    'pip-tools==0.3.4',
    'flake8==2.0',
    # Deploy tools
    #'ansible==1.3.3',
]

extras_requires = {
    'base': requires_base,
    'testing': ['nose', 'coverage'] + requires_dev,
    'docs': ['sphinx'],
}

setup(name='farmerp',
      version='0.1a',
      description='Farm accounting software',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='aert',
      author_email='dev.aert@gmail.com',
      url='https://github.com/aert/aert-farmerp',
      keywords='farm bookkeeping accounting',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=extras_requires['base'],
      tests_require=extras_requires['testing'],
      extras_require=extras_requires,
      entry_points="""\
      [console_scripts]
      farmerp-web = farmerp.web.cli:main
      """,
      )
