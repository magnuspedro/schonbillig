class ProviderSelector:

    def __init__(self, strategy):
        self._strategy = strategy

    def parse(self):
        return self._strategy.choose_provider()
