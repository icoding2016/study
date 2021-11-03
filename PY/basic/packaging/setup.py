from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'

with open('readme.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name = 'webmon_demo',
    version = VERSION,
    description = 'A website monitor demo. Practise only, dont use :)',
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    author = 'icoding2016',
    author_email = 'icoding2016@gmail.com',
    url = 'https://github.com/icoding2016/study/tree/master/PY/web/aiven',

    python_requires = '>=3.6',
    install_requires = [
        'requests',
        'kafka-python',
        'psycopg2',  # psycopg2 need 'python<x.x>-dev', 'libpq-dev' as pre-install condition.. 
                     # e.g. sudo apt install python3.9-dev libpq-dev
    ],

    package_dir = {'': 'webmon'},
    packages = [''],
    # py_modules = ['monitor', ],
    package_data  = {
        '': ['config.json'],
    },
)


