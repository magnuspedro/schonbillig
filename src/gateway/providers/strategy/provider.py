from enum import Enum

from src.gateway.providers.strategy.beleza_na_web_strategy import BelezaNaWebStrategy
from src.gateway.providers.strategy.ikesaki_strategy import IkesakiStrategy


class Provider(Enum):
    BELEZA_NA_WEB = BelezaNaWebStrategy()
    IKESAKI = IkesakiStrategy()
