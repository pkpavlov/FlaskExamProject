from models import StoreModel, UserRole

from db import db


def _check_item(item_n, item_s):
    item_name = StoreModel.query.filter_by(item_name=item_n).first()
    item_serial = StoreModel.query.filter_by(serial_number=item_s).first()
    if item_name and item_serial:
        return True
    return False


def _get_quantity_item(i):
    quantity = StoreModel.query.filter_by(item_name=i).first()

    return quantity.quantity


class StoreManager:
    @staticmethod
    def register(item):

        item = StoreModel(**item)
        item.dealer_price = item.delivery_price + (item.delivery_price * 0.3)
        item.sell_price = item.delivery_price + (item.delivery_price * 0.8)

        # check for item name and serial_number  if exists add quantity
        if _check_item(item.item_name, item.serial_number):
            q = _get_quantity_item(item.item_name)
            StoreModel.query.filter_by(
                item_name=item.item_name, serial_number=item.serial_number
            ).update({"quantity": q + item.quantity})
            db.session.commit()
        else:

            db.session.add(item)
            db.session.commit()
        return item

    @staticmethod
    def delete(item_id):
        item = StoreModel.query.filter_by(id=item_id["id"]).first()
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def buy(id, quantity):
        item = StoreModel.query.filter_by(id=id).first()
        q = item.quantity
        if q >= quantity:
            StoreModel.query.filter_by(id=id).update({"quantity": q - quantity})
            db.session.commit()
            return f"u bought {quantity} {item.item_name}"
        else:
            return "Not enouth quantity"

    @staticmethod
    def get_items():

        return StoreModel.query.all()

