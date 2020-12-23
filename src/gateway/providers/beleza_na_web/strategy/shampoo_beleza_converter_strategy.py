from src.gateway.providers.beleza_na_web.converter.get_shampoo_beleza_converter \
    import GetShampooBelezaConverter


class ShampooBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetShampooBelezaConverter().to_entity(response)
