from requests import Request

from src.config.logger.logging_module import PTLogger

logger = PTLogger(name=__name__)


class Spyder:
    urls: list

    def start_request(self, urls: str = None) -> Request:
        raise NotImplementedError

    def parse(self):
        raise NotImplementedError
