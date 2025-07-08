# base-library
Base library is a collection of all the reused common code.

## setup python venv
* activate venv: `python -m venv ./.venv && source .venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`

## how to use base-library
* build package: `python -m build`
* install build package: `pip install /Users/kuriankevin/Documents/Learning/base-library/dist/baselibrary-0.0.2-py3-none-any.whl`
* build and install package : `pip install /Users/kuriankevin/Documents/Learning/base-library`

## how to use base-library in requirements file
* install build package from local path: `baselibrary @ file:///Users/kuriankevin/Documents/Learning/base-library/dist/baselibrary-0.0.2-py3-none-any.whl`
* build and install package from local path: `baselibrary @ file:///Users/kuriankevin/Documents/Learning/base-library`
* build and install package from local folder in edit mode: `-e /Users/kuriankevin/Documents/Learning/base-library`

# Releases
## version 0.0.1
* file.check is_absolute(), exists(), is_writable()
* file.validate is_absolute(), exists(), is_writable()
* file.helper get_parent()
* folder.check is_absolute(), exists(), is_writable()
* folder.validate is_absolute(), exists(), is_writable()
* folder.helper get_parent()
* string.check is_snake_case()
* string.validate is_snake_case()
* logging.logger ApplicationLogger(), ApplicationLogger.get_logger(), LoggerUtil.mask()
* api.request Request.execute(), Url.validate(), Url.encode()
## version 0.0.2
* Fixes Issue: base-library cannot be used without initializing a logger
