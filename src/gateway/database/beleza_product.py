from src.config.db import db
from dataclasses import asdict, dataclass


class BelezaProduct:

    @staticmethod
    def insert_product(dataclass: dataclass, product_type):
        product_dict = asdict(dataclass)
        find_query = {'code.code': product_dict['code'][0]['code']}

        product = db[product_type].find_one(find_query)
        if not product:
            db[product_type].insert_one(asdict(dataclass))
        else:
            db[product_type].update_one(find_query,
                                        {'$push':
                                         {'price': product_dict['price'][0]}})
