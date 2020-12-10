from .provider_strategy import ProviderStrategy
from src.gateway.providers.ikesaki.ikesaki_spyder import IkesakiSpyder


class IkesakiStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return IkesakiSpyder().start_request(ref_product)
