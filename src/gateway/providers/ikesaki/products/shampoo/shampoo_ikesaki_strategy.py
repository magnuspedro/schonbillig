from src.config.config import Config
from src.gateway.bases.product_strategy import ProductStrategy


class ShampooIkesakiStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.IKESAKI_URLS.value['shampoo']
