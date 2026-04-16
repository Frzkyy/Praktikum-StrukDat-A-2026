# soal 1
print("=" * 15)
print("soal 1")
print("=" * 15)

stok_barang = [15, 40, 30, 10, 25]
print(stok_barang.index(10))
stok_barang[3] = 50
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)
print(sum(stok_barang))

print("Stok Aman")if float(sum(stok_barang))/len(stok_barang) < 20 else print("Waspada")



#soal 2
print("=" * 15)
print("soal 2")
print("=" * 15)

data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for i in data_aktivitas:
    if i[1] > 80:
        print(f"{i[0]} mendapatkan predikat Gold")
    elif i[1] > 50:
        print(f"{i[0]} mendapatkan predikat Silver")
    else:
        print(f"{i[0]} mendapatkan predikat Bronze")

#soal 3
print("=" * 15)
print("soal 3")
print("=" * 15)

ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
print(f"cuman ukm coding {ukm_coding - ukm_robotik}")
print(f"Mahasiswa unik = {ukm_coding | ukm_robotik}")
print(f"Apakah Andi mengikuti ukm robotik? = {"Andi" in ukm_robotik}")

#soal 4
print("=" * 15)
print("soal 4")
print("=" * 15)

gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
for i in gudang_pc:
    if i["item"] == "Keyboard":
        i["kategori"] = "aksesoris"
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})

for i in gudang_pc:
    harga = i["harga"] * i["stok"]
    print(f"Item: {i["item"]} | Total Aset: Rp {harga}")

print(gudang_pc)