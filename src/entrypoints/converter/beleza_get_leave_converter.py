from requests import Response
from url_parser import get_url

from src.entities.code import Code
from src.entities.enum.beleza_na_web_info_line import InfoLine
from src.entities.leave import Leave
from src.entities.price import Price
from src.entities.url import Url
from src.entrypoints.converter.beleza_abstract_converter import BelezaAbstractConverter


class BelezaGetLeaveConverter(BelezaAbstractConverter):
    def to_entity(self, response: Response) -> Leave:
        source = get_url(response.url).domain

        name, size, info_label, sku, leave_specs, price = self.get_elements(
            response)

        return Leave(
            name=name,
            brand=self.clear(leave_specs.get(InfoLine.BRAND.value)),
            brand_line=self.clear(leave_specs.get(InfoLine.LINE.value)),
            size=size,
            texture=self.clear(leave_specs.get(InfoLine.TEXTURE.value)) or None,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=self.clear(leave_specs.get(InfoLine.UTILITY.value)),
            size_unit=self.clear(leave_specs.get(InfoLine.SIZE.value)),
            hair_type=self.clear(leave_specs.get(
                InfoLine.HAIR_TYPE.value)),
            hair_shaft_condition=self.clear(leave_specs.get(
                InfoLine.HAIR_SHAFT_CONDITION.value)),
            properties=self.clear(leave_specs.get(
                InfoLine.PROPRIETIES.value)),
            control=self.clear(leave_specs.get(
                InfoLine.CONTROL.value)),
            products_for=self.clear(leave_specs.get(InfoLine.PRODUCTS_FOR.value)),
            url=[Url(**{'string': response.url, 'source': source})],

            code=[Code(**{'code': sku, 'source': source})]
        )
