nilai = [75,80,65,90,85]
nilai.append(95)
nilai.remove(min(nilai))
nilai.sort()
print(max(nilai), min(nilai), len(nilai))

jumlah = 0
for i in nilai:
    jumlah += int(i)

mean = float(jumlah) / len(nilai)
print(mean)


dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1], dosen[2])
for i in dosen:
    print(i, end= " ")
print("")
# Mengubah tuple dosen[4] = 14 Error (TypeError)
# kelebihan tuple dibandingkan list adalah tuple bersifat imutable, yaitu tidak dapat diubah, sehingga data yang tidak boleh diubah dapat dimasukan kedalam tuple