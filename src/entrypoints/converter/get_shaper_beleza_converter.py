from requests import Response
from url_parser import get_url

from src.entities.code import Code
from src.entities.enum.beleza_na_web_info_line import InfoLine
from src.entities.price import Price
from src.entities.shaper import Shaper
from src.entities.url import Url
from src.entrypoints.converter.abstract_converter import AbstractConverter


class GetShaperBelezaConverter(AbstractConverter):
    def to_entity(self, response: Response) -> Shaper:
        source = get_url(response.url).domain

        name, size, info_label, sku, shapper_specs, price = self.get_elements(
            response)

        return Shaper(
            name=name.replace('\n', '').split('-')[0].strip(),
            brand=self.clear(shapper_specs.get(InfoLine.BRAND.value)),
            brand_line=self.clear(shapper_specs.get(InfoLine.LINE.value)),
            vegan=False,
            size=size,
            texture=self.clear(shapper_specs.get(InfoLine.TEXTURE.value)) or None,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=self.clear(shapper_specs.get(InfoLine.UTILITY.value)),
            size_unit=self.clear(shapper_specs.get(InfoLine.SIZE.value)),
            hair_type=self.clear(shapper_specs.get(
                InfoLine.HAIR_TYPE.value)),
            hair_shaft_condition=self.clear(shapper_specs.get(
                InfoLine.HAIR_SHAFT_CONDITION.value)),
            properties=self.clear(shapper_specs.get(
                InfoLine.PROPRIETIES.value)),
            control=self.clear(shapper_specs.get(
                InfoLine.CONTROL.value)),
            products_for=self.clear(shapper_specs.get(InfoLine.PRODUCTS_FOR.value)),
            url=[Url(**{'string': response.url, 'source': source})],

            code=[Code(**{'code': sku, 'source': source})]
        )