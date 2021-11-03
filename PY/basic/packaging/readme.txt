Create package

# install tools
pip install setuptools wheel
python3 -m pip install --user --upgrade twine

# create setup.py

# build package
python setup.py.build

python setup.py sdist
python setup.py bdist_wheel
or 
python setup.py sdist bdist_wheel

# local install
pip install <path-to-package>

# upload to pypi
# ? python setup.py sdist upload
# ? python setup.py bdist_wheel uplaod
python -m twine upload  dist/*

# install package
pip install <package>
