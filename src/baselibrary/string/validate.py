import re

TYPE_ERROR_MESSAGE: str = 'only str type is accepted for value'


def is_snake_case(value: str) -> None:
    if isinstance(value, str):
        pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
        if not bool(pattern.fullmatch(string=value)):
            raise ValueError(f'not valid snake case. value:{value}')
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
