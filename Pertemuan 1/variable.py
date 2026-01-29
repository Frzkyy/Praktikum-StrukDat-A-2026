# Variabel
nama = "Budi" #String (str)
umur = 30 #Integer (int)
pi = 3.14 #float

print(f"{nama} berumur {umur} tahun") 

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

a = 20
print(a + 30, type(a))
a = str(a)
print(a, type(a))

# Penamaan variable yang benar
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""

# Penamaan variable yang salah
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# jenis penamaan variable
"""
1. Camel Case
    = myVariableName = "John"
2. Pascal Case
    MyVariableName = "John"
3. Snake Case
    my_variable_name = "John"
"""
# Assign banyak variable sekaligus
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign banyak variable tapi satu value
x = y = z = "Orange"
print(x)
print(y)
print(z)