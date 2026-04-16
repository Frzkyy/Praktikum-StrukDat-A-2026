def main():
    katalog = [
        {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
        {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
        {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}
    ]
    buku = input("Masukan Keyword: ")
    ketemu = cari_buku(katalog, buku)
    if ketemu != []:
        for i in ketemu:
            print(i)

def cari_buku(katalog, keyword):
    search = []
    for i in katalog:
        if keyword.lower() in i["nama"].lower():
            search.append(i)
    if search == []:
        print("Buku tidak ditemukan")
        return []
    else:
        return search


if __name__ == "__main__":
    main()