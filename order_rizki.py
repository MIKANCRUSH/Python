from database import connect
from prettytable import PrettyTable

class OrderRizki:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()

    def add_rizki(self, id_order, customer, product, date):
        sql = "INSERT INTO orders_rizki (id_order, customer, product, date) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (id_order, customer, product, date))
        self.conn.commit()

    def delete_rizki(self, id_order):
        sql = "DELETE FROM orders_rizki WHERE id_order = %s"
        self.cursor.execute(sql, (id_order,))
        self.conn.commit()

    def listorder_rizki(self):
        sql = "SELECT id_order, customer, product, date FROM orders_rizki"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        if rows:
            table = PrettyTable()
            table.field_names = ["ID Order", "Nama Customer", "Nama Produk", "Tanggal"]

            for row in rows:
                table.add_row(row)

            print(table)
        else:
            print("Tidak ada order yang tersedia.")

    def detailorder_rizki(self, id_order):
        sql = "SELECT id_order, customer, product, date FROM orders_rizki WHERE id_order = %s"
        self.cursor.execute(sql, (id_order,))
        rows = self.cursor.fetchall()

        if rows:
            table = PrettyTable()
            table.field_names = ["ID Order", "Nama Customer", "Nama Produk", "Tanggal"]

            for row in rows:
                table.add_row(row)

            print(table)
        else:
            print(f"Order dengan ID {id_order} tidak ditemukan.")

    def updateorder_rizki(self, id_order, new_date):
        sql = "UPDATE orders_rizki SET date = %s WHERE id_order = %s"
        self.cursor.execute(sql, (new_date, id_order))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Order dengan ID {id_order} berhasil diperbarui ke tanggal {new_date}.")
        else:
            print(f"Order dengan ID {id_order} tidak ditemukan.")
