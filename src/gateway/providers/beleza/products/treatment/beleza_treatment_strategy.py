from src.config.config import Config
from src.gateway.bases.product_strategy import ProductStrategy


class BelezaTreatmentStrategy(ProductStrategy):

    def choose_product(self) -> str:
        return Config.BELEZA_URLS.value['treatment']
