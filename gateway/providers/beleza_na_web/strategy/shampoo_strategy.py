from .product_strategy import ProductStrategy
from config.config import Config


class ShampooStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['shampoo']
