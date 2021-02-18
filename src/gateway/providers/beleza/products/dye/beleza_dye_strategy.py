from src.config.config import Config
from src.gateway.bases.product_strategy import ProductStrategy


class BelezaDyeStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['dye']
