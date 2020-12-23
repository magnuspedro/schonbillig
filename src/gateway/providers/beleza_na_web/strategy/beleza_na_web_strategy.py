from src.gateway.providers.beleza_na_web.beleza_na_web_spyder import BelezaNaWebSpyder
from src.gateway.providers.strategy.provider_strategy import ProviderStrategy


class BelezaNaWebStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return BelezaNaWebSpyder().start_request(ref_product)
