from product_rizki import ProductRizki

class ElectricMotorCycleRizki(ProductRizki):
    def __init__(self):
        super().__init__()

    def add_rizki(self, id_product, name, price, battery, mileage):
        sql = "INSERT INTO electric_motorcycles_rizki (id_product, name, price, battery, mileage) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (id_product, name, price, battery, mileage))
        self.conn.commit()
