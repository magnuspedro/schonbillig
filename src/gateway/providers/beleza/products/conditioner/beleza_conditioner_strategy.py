from src.config.config import Config
from src.gateway.bases.product_strategy import ProductStrategy


class BelezaConditionerStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['conditioner']
