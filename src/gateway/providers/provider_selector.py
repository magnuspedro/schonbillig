class ProviderSelector:

    def __init__(self, strategy):
        self._strategy = strategy

    def parse(self, ref_product):
        return self._strategy.choose_provider(ref_product)
