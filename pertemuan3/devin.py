class person:
    def __init__(self, nama, jk, umur):
        self.nama = nama
        self.jk = jk
        self.umur = umur
    
class karyawan(person):
    def __init__(self, nama, jk, umur, gaji):
        super().__init__(nama, jk, umur)
        self.gaji = gaji

    def get_gaji(self):
        print(self.gaji)

class rekening(person):
    def __init__(self,norekening, pin):
        self.norekening = norekening
        self.__pin = pin
    
    def norek(self):
        print(self.norekening)

    def pin(self):
        print(self.__pin)

