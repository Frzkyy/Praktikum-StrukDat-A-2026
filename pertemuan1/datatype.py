#String (str)
x = "Said Fairuz Zacky"
x = str("Said Fairuz Zacky")
print(type(x),end="\n\n")

#Integer (int)
x = 12
x = int(12)
print(type(x))

#Float
x = 3.14 
x = float(3.14)
print(f"\ntype(x)")

#Complex
x = 4j	
x = complex(4j)
print(type(x))

#List
x = ["TI-A", "TI-B", "TI-C"]	
x = list(("TI-A", "TI-B", "TI-C"))
print(type(x))

#Tuple
x = ("Aqua", "Aquavita", "Le Mineral")	
x = tuple(("Aqua", "Aquavita", "Le Mineral"))
print(type(x))

#Range
x = range(2,3)
x = range(2,3)
print(type(x))

#Dict
x = {"nama" : "Said", "umur" : 18}
x = dict(nama="Said", umur=18)
print(type(x))

#Set
x = {"Ketoprak", "Siomai", "Gergaji"}	
x = set(("Ketoprak", "Siomai", "Gergaji"))
print(type(x))

#Frozenset
x = frozenset({"Bingung", "Mau", "Tulis", "Apa"})
print(type(x))

#Boolean (bool)
x = True
x = bool(67)
print(type(x))

#Bytes
x = b"Privyet"	
x = bytes(5)


print(type(x))

#Bytearray
x = bytearray(3)
print(type(x))

#Memoryview
x = memoryview(bytes(3))
print(type(x))

#NoneType
x = None
print(type(x))