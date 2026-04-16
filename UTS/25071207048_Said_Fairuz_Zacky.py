pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina","usia": 20, "kategori": "Fiksi","kembali": True},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains","kembali": True},
{"id": "M003", "nama": "Siti","usia": 19, "kategori": "Fiksi","kembali": True},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum","kembali": True},
{"id": "M005", "nama": "Yuni","usia": 18, "kategori": "Sains","kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum","kembali": False},
{"id": "M007", "nama": "Rudi", "usia": 23, "kategori": "Hukum","kembali": False},
{"id": "M008", "nama": "Rusdi", "usia": 23, "kategori": "Sains","kembali": False}
]

print("=" * 30)
print("Masuk Soal 1")
print("=" * 30)
# ===================
#       Soal 1
# ===================

def tampilkan_pengunjung(riwayat):
    print()
    print("=" * 13, "DATA PENGUNJUNG PERPUSTAKAAN", "=" * 13)
    print(f"No | ID      | Nama     | Usia     | Kategori     | Status Kembali")
    print("---+---------+----------+----------+--------------+----------------")

    no = 1
    for i in riwayat:
        if i["kembali"]:
            print(f"{no}  | {i["id"]}    | {i["nama"].strip()}   | {i["usia"]}       | {i["kategori"]}        | Sudah Kembali ")
        else:
            print(f"{no}  | {i["id"]}    | {i["nama"].strip()}     | {i["usia"]}       | {i["kategori"]}        | Belum Kembali ")
        no += 1
    
    print()

def filter_belum_kembali(riwayat):
    print("=" * 13, "PENGUNJUNG BELUM KEMBALI", "=" * 13)
    belum = []
    for i in riwayat:
        if not i["kembali"]:
            belum.append(i["nama"])
    belum.sort()
    no = 1
    for i in belum:
        print(f"{no}. {i}")
        no += 1
    print(f"Total belum kembali: {len(belum)} pengunjung")

tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(pengunjung_hari_ini)


print("=" * 30)
print("Masuk Soal 2")
print("=" * 30)
print()
# ===================
#       Soal 2
# ===================
def info_perpustakaan():
    return ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321")

info = info_perpustakaan()
print(f"Nama: {info[0]}")
print(f"Alamat: {info[1]}")
print(f"Telp: {info[2]}")


def rekap_kategori(riwayat):
    unik = []
    for i in riwayat:
        unik.append(i["kategori"])
    unik = set(unik)
    total = {}

    for i in unik:
        jumlah = 0
        for j in riwayat:
            if j["kategori"] == i:
                jumlah += 1
        total[i] = jumlah

    print(f"Kategori Buku Unik: {unik}")
    print(f"Jumlah Kategori: {len(unik)}")
    print()
    print("Rekap per kategori: ")
    for i in total:
        print(f"{i} : {total[i]} pengunjung")
    
    print("Kategori terbanyak: ", end="")

    maks = list(total.values())
    maks = maks[0]
    for i in total:
        if total[i] > maks:
            maks = total[i]

    for i in total:
        if total[i] == maks:
            print(i, end=", ")
    
    print(f"({maks} Pengunjung)")

rekap_kategori(pengunjung_hari_ini)

print("=" * 30)
print("Masuk Soal 3")
print("=" * 30)
print()
# ===================
#       Soal 3
# ===================

class Pengunjung:
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
    
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f"ID : {self.__id}")
        print(f"Nama : {self.__nama}")
        print(f"Kategori : {self.__kategori}")


class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani Segera! **")

b = []
a = PengunjungPrioritas("M2212", "Rsuidi", "Fiksi", "Mendesak")
b.append(a)
a.tampilkan_info()

print()
print(f"Total Pengunjung Terdaftar: {len(b)}")

print("=" * 30)
print("Masuk Soal 4")
print("=" * 30)
print()
# ===================
#       Soal 4
# ===================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self, head):
        self.head = head

    def tambah(self, data):
        currentNode = self.head
        while currentNode and currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = Node(data)
    
    def hapus_berdasarkan_id(self, id):
        if self.head.data["id"] == id:
            return self.head.next
        currentNode = self.head
        while currentNode.next.data["id"] and currentNode.next.data["id"] != id:
            currentNode = currentNode.next
        if currentNode.next is None:
            return self.head
        currentNode.next = currentNode.next.next
        return self.head  

    def tampilkan(self):
        currentNode = self.head
        print("=" * 10, "ANTRIAN PEMINJAMAN", "=" * 10  )
        no = 1
        while currentNode:
            print(f"[{no}] {currentNode.data["id"]} - {currentNode.data["nama"]} | {currentNode.data["kategori"]}")

            no += 1
            currentNode = currentNode.next
        print()

    def hitung(self):
        currentNode = self.head
        no = 0
        while currentNode:
            currentNode = currentNode.next
            no += 1
        print(f"Total Antrian: {no}")
        print()

    def cari(self, nama):
        currentNode = self.head
        no = 1
        ada = False
        print(f"Mencari {nama}...")
        while currentNode:
            if currentNode.data["nama"] == nama:
                print(f"Ditemukan: {currentNode.data["id"]} - {currentNode.data["nama"]} ada di posisi ke-{no}")
                ada = True
            no += 1
            currentNode = currentNode.next
        if not ada:
            print("Nama tidak ditemukan!")
        print()
    
    def panggil_berikutnya(self):
        currentNode = self.head
        print()
        print("Memanggil Pengunjung Berikutnya... ")
        print(f"Silahkan Masuk: {currentNode.data["nama"]} ({currentNode.data["id"]}) - {currentNode.data["kategori"]}")
        self.head = currentNode.next
        print()

    def tampilkan(self):
        currentNode = self.head
        print("=" * 10, "ANTRIAN PEMINJAMAN", "=" * 10  )
        no = 1
        while currentNode:
            print(f"[{no}] {currentNode.data["id"]} - {currentNode.data["nama"]} | {currentNode.data["kategori"]}")

            no += 1
            currentNode = currentNode.next
        print()

def tes_node(head):
    currentNode = head
    while currentNode:
        print(currentNode.data["nama"], end=" -> ")
        currentNode = currentNode.next
    print("null")


p1 = Node({"id": "M001", "nama": "Rina","usia": 20, "kategori": "Fiksi","kembali": True})
p2 = Node({"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains","kembali": True})
p1.next = p2
p3 = Node({"id": "M003", "nama": "Siti","usia": 19, "kategori": "Fiksi","kembali": True})
p2.next = p3
p4 = Node({"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum","kembali": True})
p3.next = p4
p5 = Node({"id": "M005", "nama": "Yuni","usia": 18, "kategori": "Sains","kembali": False})
p4.next = p5
p6 = Node({"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum","kembali": False})
p5.next = p6
p7 = Node({"id": "M007", "nama": "Rudi", "usia": 23, "kategori": "Hukum","kembali": False})
p6.next = p7
p8 = Node({"id": "M008", "nama": "Rusdi", "usia": 23, "kategori": "Sains","kembali": False})
p7.next = p8

antrian = AntrianPeminjaman(p1)
antrian.tambah({"id": "M009", "nama": "Rina","kategori": "Fiksi"})
antrian.tambah({"id": "M010", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M011", "nama": "Siti","kategori": "Fiksi"})
antrian.tambah({"id": "M012", "nama": "Taufik", "kategori": "Hukum"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.cari("Rina")
antrian.cari("ada")
antrian.hitung()
antrian.hapus_berdasarkan_id("M009")
antrian.tampilkan()



    
    


