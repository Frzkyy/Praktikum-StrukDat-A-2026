#Boolean (bool) bisa True atau False
a = True
a = False

print(67 > 69) #False
print(1==1) #True
print(2*2 == 2**2) #True


print((pow(pow(2,5),0)) == (int(3.14 + 6.86) % 9)) #True

print(bool("string isinya")) # Parameter ada isinya, makanya True
print(bool("")) # karena kosong makanya False

x = 7
if x % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

x = "a"
d = None
print(bool(x)) #True karena ada isi
print(bool(d)) #False karena tidak ada isi