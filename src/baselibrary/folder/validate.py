import os
import pathlib

TYPE_ERROR_MESSAGE: str = 'only str and pathlib.Path types are accepted for path'


def is_absolute(path: str | pathlib.Path) -> None:
    message: str = f"folder path '{path}' is not absolute"
    if isinstance(path, str):
        if not os.path.isabs(s=path):
            raise ValueError(message)
    elif isinstance(path, pathlib.Path):
        if not path.is_absolute():
            raise ValueError(message)
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def exists(path: str | pathlib.Path) -> None:
    message: str = f"folder '{path}' does not exist"
    if isinstance(path, str):
        if not os.path.isdir(s=path):
            raise FileNotFoundError(message)
    elif isinstance(path, pathlib.Path):
        if not path.is_dir():
            raise FileNotFoundError(message)
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def is_writable(path: str | pathlib.Path) -> None:
    if isinstance(path, (str, pathlib.Path)):
        if not os.access(path=path, mode=os.W_OK):
            raise PermissionError(f"folder '{path}' doesnt have write permissions")
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
