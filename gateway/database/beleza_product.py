from config.db import db
from dataclasses import asdict


class BelezaProduct:

    @staticmethod
    def insert_product(dataclass):
        product_dict = asdict(dataclass)
        find_query = {'code.code': product_dict['code'][0]['code']}

        product = db.shampoo.find_one(find_query)
        if not product:
            db.shampoo.insert_one(asdict(dataclass))
        else:
            db.shampoo.update_one(find_query,
                                  {'$push':
                                   {'price': product_dict['price'][0]}})
