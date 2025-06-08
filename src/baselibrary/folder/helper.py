import os
import pathlib

TYPE_ERROR_MESSAGE: str = 'only str and pathlib.Path types are accepted for path'


def get_parent(path: str | pathlib.Path) -> str | pathlib.Path:
    if isinstance(path, str):
        return os.path.dirname(p=path)
    elif isinstance(path, pathlib.Path):
        return path.resolve().parent
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
