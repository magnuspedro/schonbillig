from enum import Enum

from src.gateway.providers.beleza_na_web.beleza_na_web_strategy import BelezaNaWebStrategy
from src.gateway.providers.ikesaki.ikesaki_strategy import IkesakiStrategy


class Provider(Enum):
    BELEZA_NA_WEB = BelezaNaWebStrategy()
    IKESAKI = IkesakiStrategy()
