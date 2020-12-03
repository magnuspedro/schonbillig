class ProductSelector:

    def __init__(self, strategy):
        self._strategy = strategy

    def choose_product(self) -> str:
        return self._strategy.choose_product()
