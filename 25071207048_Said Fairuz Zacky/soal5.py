def main():
    katalog = [
        {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
        {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
        {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}
    ]

    log_transaksi = {}
    while True:
        try:
            print("=" * 15)
            print("1. Tambah Buku")
            print("2. Tampilkan Semua buku")
            print("3. Beli Buku")
            print("4. Laporan Penjualan")
            print("5. Keluar")
            print()

            ip = int(input("Masukan Opsi: "))
            match ip:
                case 1:
                    namae = input(f"Masukan nama buku : ")
                    hargae = input(f"Masukan harga buku : ")
                    stoke = input(f"Masukan stok buku : ")
        
                    bukuBaru = tambah_buku(namae, hargae, stoke)
                    if bukuBaru:
                        katalog.append(bukuBaru)
                    print()
                
                case 2:
                    tampilkan_buku(katalog)

                case 3:
                    try:
                        namaa = input("Masukan nama buku: ")
                        stoka = int(input("Masukan jumlah pembelian: "))
                        buku = proses_transaksi(katalog, namaa, stoka)
                        try:
                            log_transaksi[namaa] += stoka
                        except KeyError:
                            log_transaksi[namaa] = stoka
                        
                    except ValueError:
                        print(f"\n[Error] jumlah pembelian hanya bisa angka")

                case 4:
                    print(log_transaksi)

                case 5:
                    break
        except ValueError:
            print("[Error] masukan hanya angka ")

def tampilkan_buku(katalog):
    for i in katalog:
        print("=" * 15)
        print(f"Nama: {i["nama"]}")
        print(f"Harga: {i["harga"]}")
        print(f"Stok: {i["stok"]}")
        print("=" * 15)
    
def tambah_buku(nama, harga, stok):
    try:
        harga = float(harga)
        stok = int(stok)
    except ValueError:
        print("[Error] Stok dan Harga harus berupa angka")
        return None

    if harga <= 0:
        print("[Error] Harga harus lebih dari 0")
        return None

    if stok < 0:
        print("[Error] Stok tidak boleh negatif")
        return None
    
    return {"nama":nama, "harga":harga, "stok":stok}

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    bukuTersedia = False
    idx = 0
    for i in katalog:
        if nama_buku.lower() == i["nama"].lower():
            bukuTersedia = True
            idxBuku = idx
            break
        else:
            idx += 1

    if bukuTersedia:
        if katalog[idxBuku]["stok"] >= jumlah_beli:
            total = jumlah_beli * katalog[idxBuku]["harga"]
            katalog[idxBuku]["stok"] -= jumlah_beli
            print(f"Total: {total}, Sisa Stok: {katalog[idxBuku]["stok"]}")
            return nama_buku
        else:
            print(f"\n[Error] Stok Buku tidak cukup")
            return None
    else:
        print(f"\n[Error] Buku tidak ditemukan")
        return None



if __name__ == "__main__":
    main()