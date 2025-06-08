import typing


def is_instance(__value: typing.Any, __type: type | tuple[type, ...], __message: str, /) -> None:
    if not isinstance(__value, __type):
        raise TypeError(__message)
