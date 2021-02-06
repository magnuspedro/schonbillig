from src.gateway.providers.beleza.beleza_spyder import BelezaNaWebSpyder
from src.gateway.database.provider_strategy import ProviderStrategy


class BelezaNaWebStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return BelezaNaWebSpyder().start_request(ref_product)
