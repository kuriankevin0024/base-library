import time
import requests
import urllib.parse
from http import HTTPStatus
from typing import Optional
from requests import Response
from urllib.parse import ParseResult

import logging
import baselibrary.logging.logger as logger

log: logging.Logger = logger.ApplicationLogger.get_logger()


class Url:
    @staticmethod
    def validate(url: str) -> None:
        parsed_url: ParseResult = urllib.parse.urlparse(url=url)
        if not (bool(parsed_url.scheme) and bool(parsed_url.netloc)):
            raise ValueError(f'invalid url:{url}')

    @staticmethod
    def encode(value: str) -> str:
        return urllib.parse.quote(value)


class RequestError(Exception):
    pass


class Request:
    @staticmethod
    def execute(url: str, method: str = 'GET', headers: dict = None, params: dict = None, payload: dict = None,
                files: dict = None, stream: bool = False, verify: bool = True, timeout: int = 60,
                retry_count: int = 2) -> Response:

        Url.validate(url=url)
        log.debug(f'request - url:{url} method:{method} headers:{headers} params:{params} payload:{payload} '
                  f'verify:{verify} timeout:{timeout} retry_count:{retry_count}')

        delay: int = 1
        times_retried: int = 0

        while times_retried <= retry_count:
            if times_retried > 0:
                log.info(f'will retry after {delay} secs...')
                time.sleep(delay)

            try:
                response: Optional[Response] = requests.request(
                    method=method.upper(), url=url, headers=headers, params=params, json=payload, files=files,
                    stream=stream, timeout=timeout, verify=verify)
            except Exception as e:
                log.error(f'exception while executing request - url:{url} method:{method} attempt:{times_retried + 1} error:{e}')
                response: Optional[Response] = None

            if response is not None:
                if HTTPStatus.OK.value <= response.status_code < HTTPStatus.MULTIPLE_CHOICES.value:
                    log.debug(f'successful response - status_code:{response.status_code} text:{response.text}')
                    return response
                else:
                    log.warning(f'unsuccessful response - status_code:{response.status_code} text:{response.text}')

            times_retried += 1
            delay = min(delay * 2, 60)

        raise RequestError(f'failed to execute request - url:{url} method:{method}')
