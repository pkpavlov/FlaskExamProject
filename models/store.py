from db import db


class StoreModel(db.Model):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    delivery_price = db.Column(db.Integer, nullable=False)
    sell_price = db.Column(db.Float, nullable=False)
    dealer_price = db.Column(db.Float, nullable=False)



