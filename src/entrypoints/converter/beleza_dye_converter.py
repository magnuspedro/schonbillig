import re

from bs4 import BeautifulSoup
from requests import Response
from url_parser import get_url

from src.entities.code import Code
from src.entities.dye import Dye
from src.entities.enum.beleza_na_web_info_line import InfoLine
from src.entities.price import Price
from src.entities.url import Url
from src.entrypoints.converter.beleza_abstract_converter import BelezaAbstractConverter


class BelezaGetDyeConverter(BelezaAbstractConverter):
    REGEX = r'([0-9]+)([-]*)(ml|g|L|l|kg)'

    def to_entity(self, response: Response) -> Dye:
        source = get_url(response.url).domain

        name, size, info_label, sku, dye_specs, price, color_number = self.get_elements(
            response)
        return Dye(
            name=name.replace('\n', '').split('-')[0].strip(),
            brand=self.clear(dye_specs.get(InfoLine.BRAND.value)),
            brand_line=self.clear(dye_specs.get(InfoLine.LINE.value)),
            size=size,
            texture=self.clear(dye_specs.get(InfoLine.TEXTURE.value)) or None,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=self.clear(dye_specs.get(InfoLine.UTILITY.value)),
            size_unit=self.clear(dye_specs.get(InfoLine.SIZE.value)),
            hair_type=self.clear(dye_specs.get(
                InfoLine.HAIR_TYPE.value)),
            hair_shaft_condition=self.clear(dye_specs.get(
                InfoLine.HAIR_SHAFT_CONDITION.value)),
            properties=self.clear(dye_specs.get(
                InfoLine.PROPRIETIES.value)),
            control=self.clear(dye_specs.get(
                InfoLine.CONTROL.value)),
            products_for=self.clear(dye_specs.get(InfoLine.PRODUCTS_FOR.value)),
            color=self.clear(dye_specs.get(InfoLine.COLOR.value)),
            volume=self.clear(dye_specs.get(InfoLine.VOLUME.value)),
            dyeing_type=self.clear(dye_specs.get(InfoLine.DYEING_TYPE.value)),
            tone=self.clear(dye_specs.get(InfoLine.TONE.value)),
            color_number=color_number,
            url=[Url(**{'string': response.url, 'source': source})],
            code=[Code(**{'code': sku, 'source': source})],
        )

    def get_elements(self, response: Response) -> list:
        soup = BeautifulSoup(response.text, features="lxml")

        name = soup.select(
            '.nproduct-title')[0].text.strip()
        size = self.clean_size(re.findall(self.REGEX, soup.select('.nproduct-title')[
            0].text))  # self.find_size(re.findall(self.REGEX, response.url))
        sku = soup.select('.product-sku')[0].text.strip().split(':')[1].strip()
        info_label = soup.select('.info-line')
        dye_specs = self.specs(info_label)
        price = soup.select('.nproduct-price-value')
        if price:
            price = price[0].text.strip().split(
                '$')[1].strip().replace('.', '').replace(',', '.')
        else:
            price = 'nan'
        color_number = soup.select('.product-group-name')
        if color_number:
            color_number = color_number[0].text.strip()
        else:
            color_number = None
        return name, size, info_label, sku, dye_specs, price, color_number
