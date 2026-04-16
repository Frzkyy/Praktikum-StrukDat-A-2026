def main():
    gudang = []
    temp = 1
    while temp < 4:
        nama = input(f"Masukan nama buku ke-{temp}: ")
        harga = input(f"Masukan harga buku ke-{temp}: ")
        stok = input(f"Masukan stok buku ke-{temp}: ")
        
        bukuBaru = tambah_buku(nama, harga, stok)
        if bukuBaru:
            gudang.append(bukuBaru)
            temp += 1
        print()
    
    for i in gudang:
        print(i)
    




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



if __name__ == "__main__":
    main()