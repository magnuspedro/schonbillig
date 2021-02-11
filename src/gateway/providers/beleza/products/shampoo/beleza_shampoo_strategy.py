from src.config.config import Config
from src.gateway.providers.bases.product_strategy import ProductStrategy


class BelezaShampooStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['shampoo']
