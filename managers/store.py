from models import StoreModel

from db import db


class StoreManager:
    @staticmethod
    def register(item):

        item = StoreModel(**item)
        item.dealer_price = item.delivery_price + (item.delivery_price * 0.3)
        item.sell_price = item.delivery_price + (item.delivery_price * 0.8)

        # check for item name and serial number if exists add quantity

        db.session.add(item)
        db.session.commit()
        return item
