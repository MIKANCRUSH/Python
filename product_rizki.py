from database import connect

class ProductRizki:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()
    
    def show_rizki(self):
        # Menampilkan data dari tabel product_rizki
        print("\n=== Produk dari Tabel product_rizki ===")
        sql = "SELECT * FROM product_rizki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

        # Menampilkan data dari tabel motorcycles_rizki
        print("\n=== Produk dari Tabel motorcycles_rizki ===")
        sql = "SELECT * FROM motorcycles_rizki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

        # Menampilkan data dari tabel electric_motorcycles_rizki
        print("\n=== Produk dari Tabel electric_motorcycles_rizki ===")
        sql = "SELECT * FROM electric_motorcycles_rizki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)
