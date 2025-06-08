import os
import pathlib

TYPE_ERROR_MESSAGE: str = 'only str and pathlib.Path types are accepted for path'


def is_absolute(path: str | pathlib.Path) -> bool:
    if isinstance(path, str):
        return os.path.isabs(s=path)
    elif isinstance(path, pathlib.Path):
        return path.is_absolute()
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def exists(path: str | pathlib.Path) -> bool:
    if isinstance(path, str):
        return os.path.isfile(path=path)
    elif isinstance(path, pathlib.Path):
        return path.is_file()
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def is_writable(path: str | pathlib.Path) -> bool:
    if isinstance(path, (str, pathlib.Path)):
        return os.access(path=path, mode=os.W_OK)
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
