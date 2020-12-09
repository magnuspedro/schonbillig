from .provider_strategy import ProviderStrategy
from ..beleza_na_web.beleza_na_web_spyder import BelezaNaWebSpyder


class BelezaNaWebStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return BelezaNaWebSpyder().start_request(ref_product)
