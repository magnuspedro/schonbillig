from src.entrypoints.converter.ikesaki_get_shampoo_converter \
    import GetShampooIkesakiConverter


class ShampooIkesakiConverterStrategy:

    @staticmethod
    def convert(response):
        return GetShampooIkesakiConverter().to_entity(response)
