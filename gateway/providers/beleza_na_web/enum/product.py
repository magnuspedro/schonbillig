from enum import Enum
from ..strategy.shampoo_strategy import ShampooStrategy


class Product(Enum):
    SHAMPOO = ShampooStrategy()
