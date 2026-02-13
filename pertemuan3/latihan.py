class Person:
    def __init__(self,nama,umur,jenisKelamin):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = jenisKelamin
    
class Karyawan(Person):
    def __init__(self, nama, umur, jenisKelamin, gaji):
        super().__init__(nama, umur, jenisKelamin)
        self._gaji = gaji

    def get_gaji(self):
        print(self._gaji)
    
    def set_gaji(self,ngaji):
        self._gaji = ngaji
        print("Gaji Berhasil Diubah")

class Rekening:
    def __init__(self,norek, pin):
        self.norek = norek
        self.__pin = pin

    def get_pin(self):
        print(self.__pin)
    
    def set_pin(self, npin):
        self.__pin = npin
        print("PIN Berhasil Diganti")

udin = Person("Udin", 12, "Laki")
print(udin.nama, udin.umur, udin.jenisKelamin)

devin = Karyawan("Devin", 18, "Perempuan", 1000000000000000)
devin.get_gaji()
devin.set_gaji(20000)
devin.get_gaji()

bca = Rekening(12345678901, 123456)
bca.get_pin()
bca.set_pin(432567)
bca.get_pin()