from enum import Enum

from src.gateway.providers.beleza_na_web.products.conditioner.conditioner_beleza_converter_strategy import \
    ConditionerBelezaConverterStrategy
from src.gateway.providers.beleza_na_web.products.finisher.finisher_beleza_converter_strategy import \
    FinisherBelezaConverterStrategy
from src.gateway.providers.beleza_na_web.products.shampoo.shampoo_beleza_converter_strategy import \
    ShampooBelezaConverterStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesak_converteri_strategy import ShampooIkesakiConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = ShampooBelezaConverterStrategy
    CONDITIONER_BELEZA = ConditionerBelezaConverterStrategy
    FINISHER_BELEZA = FinisherBelezaConverterStrategy
    SHAMPOO_IKESAKI = ShampooIkesakiConverterStrategy