def main():
    katalog = [
        {'nama': 'Belajar Python', 'harga': 75000, 'stok': 9},
        {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
        {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}
    ]
    
    riwayatBuku = set()

    """
    temp = 1
    while temp < 4:
        try:
            nama = input("Masukan nama buku: ")
            stok = int(input("Masukan jumlah pembelian: "))
            buku = proses_transaksi(katalog, nama, stok)
            if buku:
                riwayatBuku.add(buku.title())
                temp += 1
            print()
        except ValueError:
            print(f"\n[Error] jumlah pembelian hanya bisa angka")
    """
    proses_transaksi(katalog,"struktur data", 1)
    proses_transaksi(katalog,"struktur data", 1)
    proses_transaksi(katalog,"algoritma dasaR", 4)

    print(riwayatBuku)


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