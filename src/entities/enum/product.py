from enum import Enum

from src.gateway.providers.beleza_na_web.products.conditioner.conditioner_beleza_strategy \
    import ConditionerBelezaStrategy
from src.gateway.providers.beleza_na_web.products.finisher.finisher_beleza_strategy \
    import FinisherBelezaStrategy
from src.gateway.providers.beleza_na_web.products.shampoo.shampoo_beleza_strategy \
    import ShampooBelezaStrategy
from src.gateway.providers.ikesaki.products.shampoo.shampoo_ikesaki_strategy \
    import ShampooIkesakiStrategy


class Product(Enum):
    SHAMPOO_BELEZA = ShampooBelezaStrategy()
    CONDITIONER_BELEZA = ConditionerBelezaStrategy()
    FINISHER_BELEZA = FinisherBelezaStrategy()
    SHAMPOO_IKESAKI = ShampooIkesakiStrategy()
