from src.entrypoints.converter.beleza_dye_converter import BelezaGetDyeConverter


class BelezaDyeConverterStrategy:

    @staticmethod
    def convert(response):
        return BelezaGetDyeConverter().to_entity(response)
