from bs4 import BeautifulSoup
from requests import Response
from url_parser import get_url

from src.entities.code import Code
from src.entities.conditioner import Conditioner
from src.entities.price import Price
from src.entities.url import Url
from src.entities.enum.beleza_na_web_info_line import InfoLine
from src.entrypoints.converter.abstract_converter import AbstractConverter


class GetConditionerBelezaConverter(AbstractConverter):
    def to_entity(self, response: Response) -> Conditioner:
        source = get_url(response.url).domain

        name, size, info_label, sku, conditioner_specs, price = self.get_elements(
            response)

        return Conditioner(
            name=name.replace('\n', '').split('-')[0].strip(),
            brand=self.clear(conditioner_specs.get(InfoLine.BRAND.value)),
            brand_line=self.clear(conditioner_specs.get(InfoLine.LINE.value)),
            vegan=False,
            size=size,
            texture=self.clear(conditioner_specs.get(InfoLine.TEXTURE.value)) or None,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=self.clear(conditioner_specs.get(InfoLine.UTILITY.value)),
            size_unit=self.clear(conditioner_specs.get(InfoLine.SIZE.value)),
            hair_type=self.clear(conditioner_specs.get(
                InfoLine.HAIR_TYPE.value)),
            hair_shaft_condition=self.clear(conditioner_specs.get(
                InfoLine.HAIR_SHAFT_CONDITION.value)),
            properties=self.clear(conditioner_specs.get(
                InfoLine.PROPRIETIES.value)),
            url=[Url(**{'string': response.url, 'source': source})],
            code=[Code(**{'code': sku, 'source': source})]
        )
