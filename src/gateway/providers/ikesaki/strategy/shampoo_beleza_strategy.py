from ...product_strategy import ProductStrategy
from src.config.config import Config


class ShampooIkesakiStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.IKESAKI_URLS.value['shampoo']
