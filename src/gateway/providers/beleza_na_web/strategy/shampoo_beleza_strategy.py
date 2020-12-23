from src.config.config import Config
from src.gateway.providers.product_strategy import ProductStrategy


class ShampooBelezaStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['shampoo']
