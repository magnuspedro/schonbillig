from enum import Enum

from src.gateway.providers.beleza.products.conditioner.conditioner_beleza_converter_strategy import \
    ConditionerBelezaConverterStrategy
from src.gateway.providers.beleza.products.finisher.finisher_beleza_converter_strategy import \
    FinisherBelezaConverterStrategy
from src.gateway.providers.beleza.products.leave.leave_beleza_converter_strategy import LeaveBelezaConverterStrategy
from src.gateway.providers.beleza.products.shampoo.shampoo_beleza_converter_strategy import \
    ShampooBelezaConverterStrategy
from src.gateway.providers.beleza.products.treatment.treatment_beleza_converter_strategy import \
    TreatmentBelezaConverterStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesak_converteri_strategy import \
    ShampooIkesakiConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = ShampooBelezaConverterStrategy
    CONDITIONER_BELEZA = ConditionerBelezaConverterStrategy
    TREATMENT_BELEZA = TreatmentBelezaConverterStrategy
    FINISHER_BELEZA = FinisherBelezaConverterStrategy
    LEAVE_BELEZA = LeaveBelezaConverterStrategy
    SHAMPOO_IKESAKI = ShampooIkesakiConverterStrategy
