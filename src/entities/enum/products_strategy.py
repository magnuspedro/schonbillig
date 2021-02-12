from enum import Enum

from src.gateway.providers.beleza.products.conditioner.beleza_conditioner_strategy \
    import BelezaConditionerStrategy
from src.gateway.providers.beleza.products.finisher.beleza_finisher_strategy \
    import BelezaFinisherStrategy
from src.gateway.providers.beleza.products.leave.beleza_leave_strategy import BelezaLeaveStrategy
from src.gateway.providers.beleza.products.permanent.beleza_permanent_strategy import BelezaPermanentStrategy
from src.gateway.providers.beleza.products.shampoo.beleza_shampoo_strategy \
    import BelezaShampooStrategy
from src.gateway.providers.beleza.products.shaper.beleza_shaper_strategy import BelezaShaperStrategy
from src.gateway.providers.beleza.products.treatment.beleza_treatment_strategy import BelezaTreatmentStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesaki_strategy \
    import ShampooIkesakiStrategy


class ProductsStrategy(Enum):
    SHAMPOO_BELEZA = BelezaShampooStrategy()
    CONDITIONER_BELEZA = BelezaConditionerStrategy()
    FINISHER_BELEZA = BelezaFinisherStrategy()
    TREATMENT_BELEZA = BelezaTreatmentStrategy()
    LEAVE_BELEZA = BelezaLeaveStrategy()
    SHAPER_BELEZA = BelezaShaperStrategy()
    PERMANENT_BELEZA = BelezaPermanentStrategy()
    SHAMPOO_IKESAKI = ShampooIkesakiStrategy()
