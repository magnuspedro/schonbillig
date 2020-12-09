from enum import Enum

from .shampoo_beleza_converter_strategy \
    import ShampooBelezaConverterStrategy
from .conditioner_beleza_converter_strategy \
    import ConditionerBelezaConverterStrategy
from .finisher_beleza_converter_strategy \
    import FinisherBelezaConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = ShampooBelezaConverterStrategy()
    CONDITIONER_BELEZA = ConditionerBelezaConverterStrategy()
    FINISHER_BELEZA = FinisherBelezaConverterStrategy()
