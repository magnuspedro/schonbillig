from src.entrypoints.converter.get_shaper_beleza_converter import GetShaperBelezaConverter


class ShaperBelezaConverterStrategy:

    @staticmethod
    def convert(response):
        return GetShaperBelezaConverter().to_entity(response)
