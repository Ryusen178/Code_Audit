# aplikasi kasir sederhana

def h(a, b):
    return a * b

def d(t):
    if t > 100000:
        return t * 0.1
    else:
        return 0

def x():
    print("=== KASIR SEDERHANA ===")
    n = input("Masukkan nama barang: ")
    p = int(input("Masukkan harga: "))
    j = int(input("Masukkan jumlah: "))
    
    total = h(p, j)
    diskon = d(total)
    bayar = total - diskon

    print("Barang:", n)
    print("Total:", total)
    print("Diskon:", diskon)
    print("Bayar:", bayar)

x()