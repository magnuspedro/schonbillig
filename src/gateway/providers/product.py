from enum import Enum
from src.gateway.providers.beleza_na_web.strategy.shampoo_beleza_strategy \
    import ShampooBelezaStrategy
from src.gateway.providers.beleza_na_web.strategy.conditioner_beleza_strategy \
    import ConditionerBelezaStrategy
from src.gateway.providers.beleza_na_web.strategy.finisher_beleza_strategy \
    import FinisherBelezaStrategy
from src.gateway.providers.ikesaki.strategy.shampoo_beleza_strategy \
    import ShampooIkesakiStrategy


class Product(Enum):
    SHAMPOO_BELEZA = ShampooBelezaStrategy()
    CONDITIONER_BELEZA = ConditionerBelezaStrategy()
    FINISHER_BELEZA = FinisherBelezaStrategy()
    SHAMPOO_IKESAKI = ShampooIkesakiStrategy()
