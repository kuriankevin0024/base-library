from typing import Any


def is_instance(__value: Any, __type: type | tuple[type, ...], __message: str, /) -> None:
    if not isinstance(__value, __type):
        raise TypeError(__message)
