from enum import Enum

from src.gateway.providers.beleza_na_web.strategy.conditioner_beleza_converter_strategy import \
    ConditionerBelezaConverterStrategy
from src.gateway.providers.beleza_na_web.strategy.finisher_beleza_converter_strategy import \
    FinisherBelezaConverterStrategy
from src.gateway.providers.beleza_na_web.strategy.shampoo_beleza_converter_strategy import \
    ShampooBelezaConverterStrategy
from src.gateway.providers.ikesaki.strategy.shampoo_ikesaki_strategy import ShampooIkesakiConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = ShampooBelezaConverterStrategy
    CONDITIONER_BELEZA = ConditionerBelezaConverterStrategy
    FINISHER_BELEZA = FinisherBelezaConverterStrategy
    SHAMPOO_IKESAKI = ShampooIkesakiConverterStrategy
