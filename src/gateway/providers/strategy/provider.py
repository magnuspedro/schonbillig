from enum import Enum

from src.gateway.providers.beleza_na_web.strategy.beleza_na_web_strategy import BelezaNaWebStrategy
from src.gateway.providers.ikesaki.strategy.ikesaki_strategy import IkesakiStrategy


class Provider(Enum):
    BELEZA_NA_WEB = BelezaNaWebStrategy()
    IKESAKI = IkesakiStrategy()
