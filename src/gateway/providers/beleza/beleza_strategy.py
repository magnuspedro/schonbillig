from src.gateway.database.provider_strategy import ProviderStrategy
from src.gateway.providers.beleza.beleza_spyder import BelezaSpyder


class BelezaNaWebStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return BelezaSpyder().start_request(ref_product)
