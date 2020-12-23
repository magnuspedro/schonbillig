from bs4 import BeautifulSoup
from requests import Response
from url_parser import get_url

from src.config.logger.logging_module import PTLogger
from src.entities.code import Code
from src.entities.price import Price
from src.entities.shampoo import Shampoo
from src.entities.url import Url

logger = PTLogger(name=__name__)


class GetShampooIkesakiConverter:
    def to_entity(self, response: Response) -> Shampoo:
        source = get_url(response.url).domain

        name, size, price, code, brand = self.get_elements(response)

        return Shampoo(
            name=name,
            brand=brand,
            brand_line=None,
            vegan=False,
            size=size,
            price=[
                Price(**{'price': float(price), 'source': source})],
            utility=None,
            size_unit=None,
            hair_type=None,
            hair_shaft_condition=None,
            texture=None,
            url=[Url(**{'string': response.url, 'source': source})],
            code=[Code(**{'code': code, 'source': source})]
        )

    def get_elements(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        name = soup.select('.productName')[0].text.strip()
        size = response.url.split('-')[-1].strip('/')
        code = soup.select('.productReference')[0].text.strip()
        brand = soup.select('.brandName')[0].text.strip()
        price = soup.select('.skuBestPrice')
        if price:
            price = price[0].text.strip().split(
                '$')[1].strip().replace('.', '').replace(',', '.')
        else:
            price = 'nan'

        return name, size, price, code, brand
