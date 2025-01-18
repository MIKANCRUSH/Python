from database import connect
from prettytable import PrettyTable  # Import PrettyTable

class CustomerRizki:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()

    def add_rizki(self, cus_id, cus_name):
        sql = "INSERT INTO customers_rizki (cus_id, cus_name) VALUES (%s, %s)"
        self.cursor.execute(sql, (cus_id, cus_name))
        self.conn.commit()

    def update_rizki(self, cus_id, cus_name):
        sql = "UPDATE customers_rizki SET cus_name = %s WHERE cus_id = %s"
        self.cursor.execute(sql, (cus_name, cus_id))
        self.conn.commit()

    def delete_rizki(self, cus_id):
        sql = "DELETE FROM customers_rizki WHERE cus_id = %s"
        self.cursor.execute(sql, (cus_id,))
        self.conn.commit()

    def show_rizki(self):
        sql = "SELECT * FROM customers_rizki"
        self.cursor.execute(sql)

        # Membuat objek tabel
        table = PrettyTable()
        table.field_names = ["ID Customer", "Nama Customer"]

        # Menambahkan baris data ke dalam tabel
        for row in self.cursor.fetchall():
            table.add_row(row)

        # Menampilkan tabel
        print(table)
