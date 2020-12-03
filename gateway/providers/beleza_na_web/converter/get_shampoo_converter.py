from bs4 import BeautifulSoup
from config.logger.logging_module import PTLogger
from ..enum.info_line import InfoLine
from entities.price import Price
from entities.shampoo import Shampoo

logger = PTLogger(name=__name__)


class GetShampooConverter:
    def to_entity(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        name = soup.select(
            '.nproduct-title')[0].text.strip().split('-')[0].strip()
        size = response.url.split('-')[-1].strip('/')
        sku = soup.select('.product-sku')[0].text.strip().split(':')[1].strip()
        info_label = soup.select('.info-line')
        shampoo_specs = self.specs(info_label)
        price = soup.select('.nproduct-price-value')
        if price:
            price = price[0].text.strip().split(
                '$')[1].strip().replace(',', '.')
        else:
            price = 'nan'

        return Shampoo(name=name,
                       brand=shampoo_specs.get(InfoLine.BRAND.value),
                       brand_line=shampoo_specs.get(InfoLine.LINE.value),
                       vegan=False,
                       size=size,
                       price=[Price(**{'price': float(price)})],
                       utility=shampoo_specs.get(InfoLine.UTILITY.value),
                       size_unit=shampoo_specs.get(InfoLine.SIZE.value),
                       hair_type=shampoo_specs.get(
                           InfoLine.HAIR_TYPE.value),
                       hair_shaft_condition=shampoo_specs.get(
                           InfoLine.HAIR_SHAFT_CONDITION.value),
                       sku=sku
                       )

    def specs(self, info_label):
        shampoo_specs = {}
        for info in info_label:
            spec = ''
            if not info.strong:
                spec = info.span.find_next('span').text.strip()
            else:
                spec = info.strong.a.text.strip()
            shampoo_specs[info.span.text.strip()] = spec
        return shampoo_specs
