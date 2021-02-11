from src.entrypoints.converter.beleza_get_shampoo_converter \
    import BelezaGetShampooConverter


class BelezaShampooConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetShampooConverter().to_entity(response)
