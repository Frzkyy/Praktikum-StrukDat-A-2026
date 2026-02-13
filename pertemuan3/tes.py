class Animal:
    def __init__(self, nama):
        self.nama = nama

    def Speak(self,ngomong="Speeak!!"):
        print(ngomong)

class Dog(Animal):
    def __init__(self, nama):
        super().__init__(nama)
        self.nama = nama
    
    def Speak(self,ngomong="eong"):
        super().Speak(ngomong)
        print("Eong")

dogy = Dog("Anjinhhg")
print(dogy.nama)
dogy.Speak()