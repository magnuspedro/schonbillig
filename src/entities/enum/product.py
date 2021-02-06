from enum import Enum

from src.gateway.providers.beleza.products.conditioner.conditioner_beleza_strategy \
    import ConditionerBelezaStrategy
from src.gateway.providers.beleza.products.finisher.finisher_beleza_strategy \
    import FinisherBelezaStrategy
from src.gateway.providers.beleza.products.shampoo.shampoo_beleza_strategy \
    import ShampooBelezaStrategy
from src.gateway.providers.beleza.products.treatment.treatment_beleza_strategy import TreatmentBelezaStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesaki_strategy \
    import ShampooIkesakiStrategy


class Product(Enum):
    SHAMPOO_BELEZA = ShampooBelezaStrategy()
    CONDITIONER_BELEZA = ConditionerBelezaStrategy()
    FINISHER_BELEZA = FinisherBelezaStrategy()
    TREATMENT_BELEZA = TreatmentBelezaStrategy()
    SHAMPOO_IKESAKI = ShampooIkesakiStrategy()
