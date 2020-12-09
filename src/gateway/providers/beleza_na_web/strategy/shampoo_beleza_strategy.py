from ...product_strategy import ProductStrategy
from src.config.config import Config


class ShampooBelezaStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['shampoo']
