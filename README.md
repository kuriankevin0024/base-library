# base-library
collection of commonly used functions

## build package
`python -m build`
## install package
`pip install /Users/kuriankevin/Documents/GitHub/base-library/dist/baselibrary-0.0.2-py3-none-any.whl`

## build and install package
`pip install /Users/kuriankevin/Documents/GitHub/base-library`

## build and install local packages from requirements file
### install baselibrary from local folder
`baselibrary @ file:///Users/kuriankevin/Documents/GitHub/base-library/dist/baselibrary-0.0.2-py3-none-any.whl`
### build and install baselibrary from local folder
`baselibrary @ file:///Users/kuriankevin/Documents/GitHub/base-library`
### build and install baselibrary from local folder in editable mode
`-e /Users/kuriankevin/Documents/GitHub/base-library`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`

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