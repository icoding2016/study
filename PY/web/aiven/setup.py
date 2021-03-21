from setuptools import setup
from setuptools import find_packages

VERSION = '0.1.0'

with open('readme.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name = 'webmon_demo',
    version = VERSION,
    description = 'A website monitor demo',
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    author = 'icoding2016',
    author_email = 'icoding2016@gmail.com',
    url = 'https://github.com/icoding2016/study/tree/master/PY/web/aiven',

    py_modules = ['webmon'],
    python_requires = '>=3.6',
    install_requires = [
        'requests>=2.19.0',
        'kafka-python>=2.0.0',
        'psycopg2>=2.8.0',
    ],

    # package_dir = {'': 'webmon'},
    packages = ['webmon'],
    data_files = [
        ('config', ['config.json'],),
    ],
)


