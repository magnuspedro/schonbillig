from config.logger.logging_module import PTLogger

logger = PTLogger(name=__name__)


class Spyder:
    urls: list

    def start_request(self, urls=None):
        raise NotImplementedError

    def parse(self):
        raise NotImplementedError
