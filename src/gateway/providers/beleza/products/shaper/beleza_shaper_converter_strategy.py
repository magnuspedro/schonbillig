from src.entrypoints.converter.beleza_get_shaper_converter import BelezaGetShaperConverter


class BelezaShaperConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetShaperConverter().to_entity(response)
