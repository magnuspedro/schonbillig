from src.entrypoints.converter.get_shampoo_beleza_converter \
    import GetShampooBelezaConverter


class ShampooBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetShampooBelezaConverter().to_entity(response)
