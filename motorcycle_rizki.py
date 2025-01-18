from product_rizki import ProductRizki

class MotorCycleRizki(ProductRizki):
    def __init__(self):
        super().__init__()

    def add_rizki(self, id_product, name, price, cylinder, tank_capacity):
        sql = "INSERT INTO product_rizki (id_product, name, price, cylinder, tank_capacity) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (id_product, name, price, cylinder, tank_capacity))
        self.conn.commit()
