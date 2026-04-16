def main():
    level_diskon = (
        (500000, 15), # belanja >= 500.000 -> diskon 15%
        (300000, 10), # belanja >= 300.000 -> diskon 10%
        (100000, 5),  # belanja >= 100.000 -> diskon 5%
        (0, 0) # default -> tidak ada diskon
    )

    nama = input("masukan nama: ")
    harga = int(input("Masukan total belanja: "))
    hasil = hitung_diskon(harga, level_diskon)
    print("=" * 15)
    print(f"Nama: {nama}")
    print(f"Total Belanja: Rp {harga}")
    if hasil[0] == 0:
        print("Diskon: Tidak ada diskon!")
    else:
        print(f"Diskon: {hasil[0]}%")
    print(f"Nominal diskon: Rp {hasil[1]}")
    print(f"Total Akhir: Rp {hasil[2]}")


def hitung_diskon(total_belanja, level_diskon, index=0):

    for i in level_diskon:
        if total_belanja >= i[0]:
            break
        else:
            index += 1
    
    diskon = (float(level_diskon[index][1])/100)*total_belanja
    return (level_diskon[index][1], diskon, total_belanja - diskon)


if __name__ == "__main__":
    main()