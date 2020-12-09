from enum import Enum
from .beleza_na_web_strategy import BelezaNaWebStrategy


class Provider(Enum):
    BELEZA_NA_WEB = BelezaNaWebStrategy()
