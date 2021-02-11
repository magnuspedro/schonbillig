import re
from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup
from requests import Response


class BelezaAbstractConverter(metaclass=ABCMeta):
    @abstractmethod
    def to_entity(self):
        raise NotImplemented

    def get_elements(self, response: Response) -> list:
        soup = BeautifulSoup(response.text, features="lxml")

        name = soup.select(
            '.nproduct-title')[0].text.strip()
        size = re.findall('[0-9]+-*ml', response.url)[0].replace('-', '')
        sku = soup.select('.product-sku')[0].text.strip().split(':')[1].strip()
        info_label = soup.select('.info-line')
        leave_specs = self.specs(info_label)
        price = soup.select('.nproduct-price-value')
        if price:
            price = price[0].text.strip().split(
                '$')[1].strip().replace('.', '').replace(',', '.')
        else:
            price = 'nan'
        return name, size, info_label, sku, leave_specs, price

    def specs(self, info_label: str) -> dict:
        leave_specs = {}
        for info in info_label:
            if not info.strong:
                spec = info.span.find_next('span').text.strip()
            else:
                spec = [tag.text.strip() for tag in info.findAll('a')]
            leave_specs[info.span.text.strip()] = spec
        return leave_specs

    def clear(self, array):
        if array is None:
            return None
        elif len(array) > 1 and isinstance(array, list):
            return array
        elif isinstance(array, str):
            return array
        return array[0]
