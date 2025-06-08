import re

TYPE_ERROR_MESSAGE: str = 'only str type is accepted for value'


def is_snake_case(value: str) -> bool:
    if isinstance(value, str):
        pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
        return bool(pattern.fullmatch(string=value))
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
