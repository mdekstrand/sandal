# list the tasks in this project (default)
list-tasks:
    just --list

# clean up build artifacts
clean:
    rm -rf build dist *.egg-info

# build the modules and wheels
build:
    python -m build -n

# install the package
[confirm("this installs package from a wheel, continue [y/N]?")]
install:
    pip install .

# install the package (editable)
install-editable:
    pip install -e .

# set up for development in non-conda environments
install-dev:
    pip install -e '.[dev,test,doc]'

# run tests with default configuration
test:
    python -m pytest

# run tests matching a keyword query
test-matching query:
    python -m pytest -k 

# build documentation
docs:
    sphinx-build docs build/doc

# preview documentation with live rebuild
preview-docs:
    sphinx-autobuild --watch sandal docs build/doc

# update source file headers
update-headers:
    unbehead
