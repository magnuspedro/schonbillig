from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import Enum

from tenacity import RetryError

from src.config.config import Config
from src.config.logger.logging_module import PTLogger
from src.gateway.bases.request import Request
from src.gateway.bases.spyder import Spyder
from src.gateway.providers.beleza.beleza_request_items import \
    BelezaRequestItems
from src.gateway.providers.product_selector import \
    ProductSelector

logger = PTLogger(name=__name__)


class BelezaSpyder(Spyder):
    source = Config.BELEZA_BASE_URL.value

    def start_request(self, ref_product: Enum) -> list:
        product = ProductSelector(ref_product.value).choose_product()
        logger.debug(f'[BelezaNaWeb] Requesting {ref_product.name} ', extra={
            'mdc': {'url': product, 'product': ref_product.name}})

        requests = BelezaRequestItems(
            params=Config.BELEZA_PARAMAS.value,
            product=product, source=self.source, ).request_items()
        return self.request_product(requests)

    def request_product(self, requests: list) -> list:
        responses = []
        with ThreadPoolExecutor(max_workers=Config.REQUEST_MAX_WORKERS.value) as executor:
            process = [(executor.submit(Request(self.source + request).request)) for request in requests]
        for task in as_completed(process):
            try:
                response = task.result()
            except RetryError as e:
                logger.error('The page was not found')  # Todo: Concertar esse log
                continue
            if response.ok:
                responses.append(response)
        return responses
