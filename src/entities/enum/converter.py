from enum import Enum

from src.gateway.providers.beleza.products.conditioner.beleza_conditioner_converter_strategy import \
    BelezaConditionerConverterStrategy
from src.gateway.providers.beleza.products.dye.beleza_dye_converter_strategy import BelezaDyeConverterStrategy
from src.gateway.providers.beleza.products.finisher.beleza_finisher_converter_strategy import \
    BelezaFinisherConverterStrategy
from src.gateway.providers.beleza.products.leave.beleza_leave_converter_strategy import BelezaLeaveConverterStrategy
from src.gateway.providers.beleza.products.permanent.beleza_permanent_converter_strategy import \
    BelezaPermanentConverterStrategy
from src.gateway.providers.beleza.products.shampoo.beleza_shampoo_converter_strategy import \
    BelezaShampooConverterStrategy
from src.gateway.providers.beleza.products.shaper.beleza_shaper_converter_strategy import BelezaShaperConverterStrategy
from src.gateway.providers.beleza.products.treatment.beleza_treatment_converter_strategy import \
    BelezaTreatmentConverterStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesak_converteri_strategy import \
    ShampooIkesakiConverterStrategy


class Converter(Enum):
    SHAMPOO_BELEZA = BelezaShampooConverterStrategy
    CONDITIONER_BELEZA = BelezaConditionerConverterStrategy
    TREATMENT_BELEZA = BelezaTreatmentConverterStrategy
    FINISHER_BELEZA = BelezaFinisherConverterStrategy
    LEAVE_BELEZA = BelezaLeaveConverterStrategy
    SHAPER_BELEZA = BelezaShaperConverterStrategy
    PERMANENT_BELEZA = BelezaPermanentConverterStrategy
    DYE_BELEZA = BelezaDyeConverterStrategy
    SHAMPOO_IKESAKI = ShampooIkesakiConverterStrategy
