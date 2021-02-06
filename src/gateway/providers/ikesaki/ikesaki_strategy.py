from src.gateway.providers.ikesaki.ikesaki_spyder import IkesakiSpyder
from src.gateway.database.provider_strategy import ProviderStrategy


class IkesakiStrategy(ProviderStrategy):

    def choose_provider(self, ref_product):
        return IkesakiSpyder().start_request(ref_product)
