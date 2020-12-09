class ConverterSelector:

    def __init__(self, strategy):
        self._strategy = strategy

    def convert(self, response):
        return self._strategy.convert(response)
