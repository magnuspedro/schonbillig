from src.entrypoints.converter.beleza_get_permanent_converter import BelezaGetPermanentConverter


class BelezaPermanentConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetPermanentConverter().to_entity(response)
