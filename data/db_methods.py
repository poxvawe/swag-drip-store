import sqlite3
import base64


class Thing(object):
    def __init__(self, id, name, price, quantity, seller_id, image):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.seller_id = seller_id
        self.image = image

    @classmethod
    def get_all(cls, max=20):
        cursor = db_connect()
        QUERY = """
                  SELECT id,
                         name,
                         price,
                         quantity,
                         seller_id,
                         image
                   FROM products
                   WHERE seller_id = 1
                   LIMIT ?;
               """

        cursor.execute(QUERY, (max,))
        products_list = cursor.fetchall()
        clothes = [Thing(*row) for row in products_list]
        return clothes

    def get_image_base64(self):
        return base64.b64encode(self.image).decode('utf-8')


def db_connect():
    conn = sqlite3.connect("./db/store.db")
    cursor = conn.cursor()
    return cursor
