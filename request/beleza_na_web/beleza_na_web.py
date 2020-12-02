from logger.logging_module import PTLogger
from request.beleza_na_web.beleza_na_web_request_itens import BelezaNaWebRequestItens
from request.request import Request

logger = PTLogger(name=__name__)


class BelezaNaWeb():
    #logger.info(f'Getting links for requesting to {__name__}')
    def __init__(self, urls, base_url):
        self.urls = urls
        self.base_url = base_url

    def start_request(self, urls=None):
        if urls is None:
            urls = self.urls

        for key, url in urls.items():
            logger.debug(f'[BelezaNaWeb]', extra={'mdc': {'url': url}})
            for items in BelezaNaWebRequestItens(params="&size=36&pagina=1", sub_item=key, sub_url=url, base_url=self.base_url).request_itens():
                yield items
