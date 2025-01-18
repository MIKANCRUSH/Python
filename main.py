from customer_rizki import CustomerRizki
from product_rizki import ProductRizki
from motorcycle_rizki import MotorCycleRizki
from electric_motorcycle_rizki import ElectricMotorCycleRizki
from order_rizki import OrderRizki
from prettytable import PrettyTable  # Import PrettyTable

def kelola_customer():
    customer = CustomerRizki()
    while True:
        print("\n=== Kelola Customer ===")
        print("1. Tambah Customer")
        print("2. Update Customer")
        print("3. Hapus Customer")
        print("4. Lihat Semua Customer")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                cus_id = int(input("Masukkan ID Customer: "))
                cus_name = input("Masukkan Nama Customer: ")
                customer.add_rizki(cus_id, cus_name)
                print("Customer berhasil ditambahkan!")
            elif pilihan == "2":
                cus_id = int(input("Masukkan ID Customer yang akan diupdate: "))
                cus_name = input("Masukkan Nama Baru: ")
                customer.update_rizki(cus_id, cus_name)
                print("Customer berhasil diupdate!")
            elif pilihan == "3":
                cus_id = int(input("Masukkan ID Customer yang akan dihapus: "))
                customer.delete_rizki(cus_id)
                print("Customer berhasil dihapus!")
            elif pilihan == "4":
                customer.show_rizki()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka untuk ID!")

def kelola_produk():
    product = ProductRizki()
    while True:
        print("\n=== Kelola Produk ===")
        print("1. Lihat Semua Produk")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            product.show_rizki()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

def kelola_order():
    order = OrderRizki()
    while True:
        print("\n=== Kelola Order ===")
        print("1. Tambah Order")
        print("2. Update Order")
        print("3. Hapus Order")
        print("4. Lihat Semua Order")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                order_id = int(input("Masukkan ID Order: "))
                order_date = input("Masukkan Tanggal Order (YYYY-MM-DD): ")
                customer_id = int(input("Masukkan ID Customer: "))
                product_name = input("Masukkan Nama Produk: ")
                order.add_rizki(order_id, customer_id, product_name, order_date)
                print("Order berhasil ditambahkan!")
            elif pilihan == "2":
                order_id = int(input("Masukkan ID Order yang akan diupdate: "))
                order_date = input("Masukkan Tanggal Baru (YYYY-MM-DD): ")
                order.updateorder_rizki(order_id, order_date)
                print("Order berhasil diupdate!")
            elif pilihan == "3":
                order_id = int(input("Masukkan ID Order yang akan dihapus: "))
                order.delete_rizki(order_id)
                print("Order berhasil dihapus!")
            elif pilihan == "4":
                order.listorder_rizki()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka untuk ID!")

def main():
    while True:
        print("\n=== Menu Program Rizki ===")
        print("1. Kelola Customer")
        print("2. Kelola Produk")
        print("3. Kelola Order")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kelola_customer()
        elif pilihan == "2":
            kelola_produk()
        elif pilihan == "3":
            kelola_order()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
