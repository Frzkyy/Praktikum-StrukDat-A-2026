# Variabel
nama = "Budi" 
umur = 30 
pi = 3.14 
print(nama)

print(f"{nama} berumur {umur} tahun") 

# Casting
a = 20
print(a + 30, type(a))
a = str(a) #Ini castingnya
print(a, type(a))

# Penamaan variable yang benar
"""
inivariabel = "satu"
ini_variabel = "dua"
_ini_variabel = "tiga"
iniVariabel = "empat"
INIVARIABEL = "lima"
inivariabel67 = "enam"
"""

# Penamaan variable yang salah
"""
67inivariabel = "John" (angka tidak boleh ada di depan kalimat)
ini-variabel = "John" (gk boleh ada simbol selain underscore)
ini variabel = "John" (jangan ada spasi diantara kita)
"""

# jenis penamaan variable
"""
1. Camel Case
    = iniMyVariabelSaya = "John"
2. Pascal Case
    IniMyVariabelSaya = "John"
3. Snake Case
    ini_my_variabel_saya = "John"
"""
# Assign banyak variable sekaligus

siswa1, siswa2, siswa3 = 80, 70, 60


print(f"siswa1 nilainya {siswa1}")
print(f"siswa2 nilainya {siswa2}")
print(f"siswa3 nilainya {siswa3}")

# Assign banyak variable tapi satu value

rusdi = faiz = asep = 67

print(f"Mas rusdi {rusdi}")
print(f"Mas faiz {faiz}")
print(f"Mas asep {asep}\n")

# Kalau ada 2 variabel, terus satunya integer (a) satunya string (b), itu kalau di print(a + b) tidak bisa, harus pakai print(a,b)



barang = ["ubi", "singkong", "gergaji"]
x, y, z = barang

x = "Halo"
y = "Dunia"
print(x + y)
print(x,y)


print(f"\n",y)
print(z) 