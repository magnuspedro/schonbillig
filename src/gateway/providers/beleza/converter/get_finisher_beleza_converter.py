from bs4 import BeautifulSoup
from requests import Response
from url_parser import get_url

from src.config.logger.logging_module import PTLogger
from src.entities.code import Code
from src.entities.finisher import Finisher
from src.entities.price import Price
from src.entities.url import Url
from src.entities.enum.beleza_na_web_info_line import InfoLine

logger = PTLogger(name=__name__)


class GetFinisherBelezaConverter:
    def to_entity(self, response: Response) -> Finisher:
        source = get_url(response.url).domain

        name, size, info_label, sku, finisher_specs, price = self.get_elements(
            response)

        return Finisher(
            name=name,
            brand=finisher_specs.get(InfoLine.BRAND.value),
            brand_line=finisher_specs.get(InfoLine.LINE.value),
            vegan=False,
            size=size,
            texture=finisher_specs.get(InfoLine.TEXTURE.value) or None,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=finisher_specs.get(InfoLine.UTILITY.value),
            size_unit=finisher_specs.get(InfoLine.SIZE.value),
            hair_type=finisher_specs.get(
                InfoLine.HAIR_TYPE.value),
            hair_shaft_condition=finisher_specs.get(
                InfoLine.HAIR_SHAFT_CONDITION.value),
            url=[Url(**{'string': response.url, 'source': source})],
            code=[Code(**{'code': sku, 'source': source})]
        )

    def get_elements(self, response: Response) -> list:
        soup = BeautifulSoup(response.text, features="lxml")

        name = soup.select(
            '.nproduct-title')[0].text.strip()
        size = response.url.split('-')[-1].strip('/')
        sku = soup.select('.product-sku')[0].text.strip().split(':')[1].strip()
        info_label = soup.select('.info-line')
        finisher_specs = self.specs(info_label)
        price = soup.select('.nproduct-price-value')
        if price:
            price = price[0].text.strip().split(
                '$')[1].strip().replace('.', '').replace(',', '.')
        else:
            price = 'nan'
        return name, size, info_label, sku, finisher_specs, price

    def specs(self, info_label: str) -> dict:
        finisher_specs = {}
        for info in info_label:
            if not info.strong:
                spec = info.span.find_next('span').text.strip()
            else:
                spec = info.strong.a.text.strip()
            finisher_specs[info.span.text.strip()] = spec
        return finisher_specs
