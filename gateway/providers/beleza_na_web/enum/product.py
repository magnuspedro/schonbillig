from enum import Enum
from gateway.providers.beleza_na_web.strategy.shampoo_strategy \
    import ShampooStrategy


class Product(Enum):
    SHAMPOO = ShampooStrategy()
