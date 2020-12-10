from enum import Enum
from .beleza_na_web_strategy import BelezaNaWebStrategy
from .ikesaki_strategy import IkesakiStrategy


class Provider(Enum):
    BELEZA_NA_WEB = BelezaNaWebStrategy()
    IKESAKI = IkesakiStrategy()
