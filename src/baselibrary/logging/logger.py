import sys
import typing
import logging
import pathlib
import dataclasses

import baselibrary.common.validate as validate
import baselibrary.string.validate as string_validate
import baselibrary.file.check as file_check
import baselibrary.file.validate as file_validate
import baselibrary.file.helper as file_helper
import baselibrary.folder.validate as folder_validate


class LoggerNotInitializedError(RuntimeError):
    pass


class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        super().__init__()
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level


@dataclasses.dataclass
class LoggerConfig:
    root_log_level: str = 'DEBUG'
    stdout_log_level: str = 'INFO'
    stderr_log_level: str = 'WARNING'
    file_log_level: str = 'DEBUG'

    def __post_init__(self) -> None:
        for f in dataclasses.fields(self):  # type: ignore[arg-type]
            value = getattr(self, f.name)
            validate.is_instance(value, str, f'only str type is accepted for {f.name}')


class LoggerUtil:
    @staticmethod
    def mask(object_: typing.Union[dict, list, typing.Any], patterns: list[str] = None) -> typing.Any:
        mask_pattern: str = "***MASKED***"
        if patterns is None:
            patterns = ['token']
        if isinstance(object_, dict):
            result: dict[str, typing.Any] = {}
            for key, value in object_.items():
                if any(patter.lower() in key.lower() for patter in patterns):
                    result[key] = mask_pattern
                else:
                    result[key] = LoggerUtil.mask(value, patterns)
            return result
        elif isinstance(object_, list):
            return [LoggerUtil.mask(item, patterns) for item in object_]
        else:
            return object_


class ApplicationLogger:
    __logger: logging.Logger = None

    def __init__(self, logger_name: str, logger_file: str | pathlib.Path = None, logger_config: LoggerConfig = LoggerConfig()):
        validate.is_instance(logger_name, str, 'only str type is accepted for logger_name')
        self.__logger_name: str = logger_name
        validate.is_instance(logger_file, (str, pathlib.Path), 'only str and pathlib.Path types are accepted for logger_file')
        self.__logger_file: str | pathlib.Path = logger_file
        validate.is_instance(logger_config, LoggerConfig, 'only LoggerConfig type is accepted for logger_config')
        self.__logger_config: LoggerConfig = logger_config
        if ApplicationLogger.__logger is None:
            ApplicationLogger.__logger = self.__initialize_logger()

    @staticmethod
    def __write_to_file(log_file: str | pathlib.Path) -> bool:
        if log_file is None:
            return False
        file_validate.is_absolute(path=log_file)

        log_path: str | pathlib.Path = file_helper.get_parent(path=log_file)
        folder_validate.exists(path=log_path)
        folder_validate.is_writable(path=log_path)

        if file_check.exists(log_file):
            file_validate.is_writable(path=log_file)

        return True

    def __initialize_logger(self) -> logging.Logger:
        formatter: logging.Formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')

        string_validate.is_snake_case(value=self.__logger_name)
        logger: logging.Logger = logging.getLogger(name=self.__logger_name)
        logger.setLevel(level=self.__logger_config.root_log_level)

        stdout_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(level=self.__logger_config.stdout_log_level)
        stdout_handler.addFilter(filter=MaxLevelFilter(logging.INFO))
        stdout_handler.setFormatter(fmt=formatter)
        logger.addHandler(hdlr=stdout_handler)

        stderr_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stderr)
        stderr_handler.setLevel(level=self.__logger_config.stderr_log_level)
        stderr_handler.setFormatter(fmt=formatter)
        logger.addHandler(hdlr=stderr_handler)

        if ApplicationLogger.__write_to_file(log_file=self.__logger_file):
            file_handler: logging.FileHandler = logging.FileHandler(filename=self.__logger_file)
            file_handler.setLevel(level=self.__logger_config.file_log_level)
            file_handler.setFormatter(fmt=formatter)
            logger.addHandler(hdlr=file_handler)

        return logger

    @classmethod
    def get_logger(cls) -> logging.Logger:
        if cls.__logger is None:
            raise LoggerNotInitializedError('create an ApplicationLogger instance before calling get_logger()')
        return cls.__logger
