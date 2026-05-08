class HashTable:
    def __init__(self):
        self.panjang_bucket = 10
        self.bucket = [[] for _ in range(self.panjang_bucket)]

    def hitung_index(self, kode):
        jumlah_unicode = 0
        for karakter in kode:
            jumlah_unicode += ord(karakter)
        index = jumlah_unicode % self.panjang_bucket
        return index

    def insert(self, kode, judul):
        index = self.hitung_index(kode)

        for i in range(len(self.bucket[index])):
            if self.bucket[index][i][0] == kode:
                self.bucket[index][i][1] = judul
                print(f"Buku dengan kode {kode} diupdate menjadi '{judul}'")
                return

        self.bucket[index].append([kode, judul])
        print(f"Buku '{judul}' dengan kode {kode} berhasil ditambahkan (index: {index})")

    def search(self, kode):
        index = self.hitung_index(kode)

        for data in self.bucket[index]:
            if data[0] == kode:
                print(f"Buku ditemukan! Kode: {kode} | Judul: {data[1]}")
                return data[1]

        print("Buku tidak ditemukan")
        return None

    def delete(self, kode):
        index = self.hitung_index(kode)

        for i in range(len(self.bucket[index])):
            if self.bucket[index][i][0] == kode:
                judul = self.bucket[index][i][1]
                self.bucket[index].pop(i)
                print(f"Buku '{judul}' dengan kode {kode} berhasil dihapus")
                return

        print(f"Buku dengan kode {kode} tidak ditemukan, gagal dihapus")

    def display(self):
        print("\n===== ISI HASH TABLE =====")
        ada_data = False
        for i in range(self.panjang_bucket):
            if len(self.bucket[i]) > 0:
                ada_data = True
                print(f"Index {i}: ", end="")
                for j in range(len(self.bucket[i])):
                    print(f"[{self.bucket[i][j][0]} : {self.bucket[i][j][1]}]", end="")
                    if j < len(self.bucket[i]) - 1:
                        print(" -> ", end="")  # tanda chaining kalau ada collision
                print()
        if not ada_data:
            print("Hash table masih kosong")
        print("==========================\n")



ht = HashTable()

print(">>> INSERT DATA AWAL <<<")
ht.insert("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK333", "Debat Sengit Calon Jenazah VS Malaikat Maut")
ht.insert("BK444", "How To Make an Atomic Bomb")
ht.insert("BK555", "Sawit in a Nutshell")  
ht.insert("BK666", "Matematika Diskrit")  
ht.insert("BK777", "Atomic Habits")  

print("\n>>> DISPLAY HASH TABLE <<<")
ht.display()

print(">>> INSERT TAMBAHAN <<<")
ht.insert("BK045", "Mein Kampf")
ht.insert("BK111", "Bumi Manusia")  # ini harusnya update karena BK111 sudah ada

print("\n>>> DISPLAY SETELAH INSERT TAMBAHAN <<<")
ht.display()

print(">>> SEARCH <<<")
ht.search("BK222")       
ht.search("BK999")       

print("\n>>> DELETE <<<")
ht.delete("BK333")       # hapus Debat Maut Calon Jenazah VS Malaikat Maut


print("\n>>> DISPLAY SETELAH DELETE <<<")
ht.display()