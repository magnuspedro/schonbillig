from enum import Enum

from src.gateway.providers.converter.strategy.conditioner_beleza_converter_strategy import \
    ConditionerBelezaConverterStrategy
from src.gateway.providers.converter.strategy.finisher_beleza_converter_strategy import FinisherBelezaConverterStrategy
from src.gateway.providers.converter.strategy.shampoo_beleza_converter_strategy import ShampooBelezaConverterStrategy
from src.gateway.providers.converter.strategy.shampoo_ikesaki_strategy import ShampooIkesakiConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = ShampooBelezaConverterStrategy()
    CONDITIONER_BELEZA = ConditionerBelezaConverterStrategy()
    FINISHER_BELEZA = FinisherBelezaConverterStrategy()
    SHAMPOO_IKESAKI = ShampooIkesakiConverterStrategy()
