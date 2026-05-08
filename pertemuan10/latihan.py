# simulasi antrian poli umum

class Node:
    # menyimpan data pasien
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


class Antrian:
    def __init__(self):
        self.head = None
        self.tail = None
        self.jumlah = 0

    # cek apakah antrian kosong
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    # menambah pasien ke antrian
    def enqueue(self, nama, keluhan):
        baru = Node(nama, keluhan)

        if self.is_empty():
            self.head = baru
            self.tail = baru
        else:
            self.tail.next = baru
            self.tail = baru

        self.jumlah = self.jumlah + 1
        print(nama, "masuk antrian")

    # menghapus pasien dari depan
    def dequeue(self):
        if self.is_empty():
            print("antrian kosong")
        else:
            keluar = self.head
            self.head = self.head.next
            self.jumlah = self.jumlah - 1

            print(keluar.nama, "dipanggil dokter")

            if self.head == None:
                self.tail = None

    # melihat pasien paling depan
    def peek(self):
        if self.is_empty():
            print("tidak ada pasien")
        else:
            print("pasien berikutnya:", self.head.nama)

    # menghitung jumlah pasien
    def size(self):
        return self.jumlah

    # mengosongkan antrian
    def clear(self):
        self.head = None
        self.tail = None
        self.jumlah = 0
        print("antrian dikosongkan")

    # menampilkan semua antrian
    def tampil(self):
        if self.is_empty():
            print("antrian kosong")
        else:
            bantu = self.head
            no = 1
            while bantu != None:
                print(no, ".", bantu.nama, "-", bantu.keluhan)
                bantu = bantu.next
                no = no + 1


rsunri = Antrian()

print("cek awal:")
print("kosong?", rsunri.is_empty())

rsunri.enqueue("BUDI", "sakit kelapa")
rsunri.enqueue("ANI", "demam pendek")
rsunri.enqueue("CITRA", "cuman tidur")

print("jumlah pasien:", rsunri.size())

rsunri.peek()
rsunri.dequeue()
rsunri.enqueue("DODI", "kepleset pisang")

print("antrian sekarang:")
rsunri.tampil()
rsunri.dequeue()

print("sisa pasien:", rsunri.size())
rsunri.clear()
print("kosong sekarang?", rsunri.is_empty())