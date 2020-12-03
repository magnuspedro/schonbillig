from config.logger.logging_module import PTLogger
from config.config import Config

from .beleza_na_web_request_itens import BelezaNaWebRequestItens

logger = PTLogger(name=__name__)


class BelezaNaWebPage():
    # logger.info(f'Getting links for requesting to {__name__}')
    def __init__(self, product, source):
        self.product = product
        self.source = source

    def start_request(self):
        logger.debug('[BelezaNaWeb] ', extra={'mdc': {'url': self.product}})
        yield from BelezaNaWebRequestItens(
            params=Config.BELEZA_PARAMAS.value,
            product=self.product,
            source=self.source,
        ).request_itens()
