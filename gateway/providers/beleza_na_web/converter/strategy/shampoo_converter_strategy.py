from ..get_shampoo_converter import GetShampooConverter


class ShampooConverterStrategy():

    def convert(self, response):
        return GetShampooConverter().to_entity(response)
