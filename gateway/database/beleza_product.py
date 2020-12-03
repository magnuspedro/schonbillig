from db import db
from dataclasses import asdict


class BelezaProduct:

    @staticmethod
    def insert_product(dataclass):
        product_dict = asdict(dataclass)
        product = db.find_one({'sku': product_dict['sku']})
        if not product:
            db.insert_one(asdict(dataclass))
        else:
            db.update_one({'sku': product_dict['sku']}, {
                          '$push': {'price': product_dict['price'][0]}})

        print(product)
