from gateway.providers.strategy.provider_selector import ProviderSelector
from gateway.providers.strategy.provider import Provider
from gateway.database.beleza_product import BelezaProduct


class GetShampoo:

    @staticmethod
    def execute():
        for product in ProviderSelector(Provider.BELEZA_NA_WEB.value).parse():
            BelezaProduct.insert_product(product)
