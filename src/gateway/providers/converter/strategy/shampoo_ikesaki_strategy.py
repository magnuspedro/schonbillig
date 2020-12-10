from src.gateway.providers.ikesaki.converter.get_shampoo_ikesaki_converter\
    import GetShampooIkesakiConverter


class ShampooIkesakiConverterStrategy():

    def convert(self, response):
        return GetShampooIkesakiConverter().to_entity(response)
