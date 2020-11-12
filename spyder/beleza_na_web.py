from spyder.spyder import Spyder
from logger.logging_module import PTLogger

logger = PTLogger(name=__name__)


class BelezaNaWeb(Spyder):
    logger.info(f'Starting requesting to {__name__}')
    urls = [
        'https://www.belezanaweb.com.br/wella-professionals-invigo-nutrienrich-shampoo-50ml/',
        'https://www.belezanaweb.com.br/kerastase-densifique-bain-densite-shampoo-250ml/',
        'https://www.belezanaweb.com.br/keune-care-vital-nutrition-shampoo-1000ml/'
    ]

    def parse(self, response):
        logger.info('Parsing the response')
