from dataclasses import asdict, dataclass

from src.config.db import db
from src.utils.utils import Utils


class BelezaProduct:

    @staticmethod
    def insert_product(product_dataclass: dataclass, product_type: str):
        product_dict = Utils.del_none(asdict(product_dataclass))
        find_query = {'code.code': product_dict['code'][0]['code']}

        product = db[product_type].find_one(find_query)
        if not product:
            db[product_type].insert_one(product_dict)
        else:
            db[product_type].update_one(find_query,
                                        {'$push':
                                             {'price': product_dict['price'][0]}})

    @staticmethod
    def find_product(product_type: str, brand: str) -> list:
        products = db[product_type].find({'brand': brand}, {'name': 1, 'code': 1, '_id': 0})
        return products
