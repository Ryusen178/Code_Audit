# aplikasi kasir sederhana (versi clean code)

DISCOUNT_THRESHOLD = 100000
DISCOUNT_RATE = 0.1


def hitung_total(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total):
    if total > DISCOUNT_THRESHOLD:
        return total * DISCOUNT_RATE
    return 0


def input_data():
    nama_barang = input("Masukkan nama barang: ")
    
    try:
        harga = int(input("Masukkan harga: "))
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Input harus berupa angka!")
        return None

    return nama_barang, harga, jumlah


def tampilkan_hasil(nama_barang, total, diskon, total_bayar):
    print("\n=== STRUK PEMBELIAN ===")
    print(f"Barang       : {nama_barang}")
    print(f"Total        : {total}")
    print(f"Diskon       : {diskon}")
    print(f"Total Bayar  : {total_bayar}")


def main():
    print("=== KASIR SEDERHANA ===")
    
    data = input_data()
    if data is None:
        return

    nama_barang, harga, jumlah = data

    total = hitung_total(harga, jumlah)
    diskon = hitung_diskon(total)
    total_bayar = total - diskon

    tampilkan_hasil(nama_barang, total, diskon, total_bayar)


if __name__ == "__main__":
    main()