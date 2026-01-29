# String
print("ini string")

a = "Ini juga string"
print(a)

# Multiline string
print("""
ini juga string
bisa multiline """)

a = """
variabel ini
bisa multiline juga
"""
print(a)

# Karena string itu array, maka
a = "Sawit"
b = a[0]
print(f"{b} adalah index 0 dari variabel a yang berisi {a} dan panjangnya {len(a)}")

for huruf in a:
    print(huruf, end="-")
print("\n")

# Slicing string
b = "Bingung mau tulis apa"
print(b[2:7]) # x:y berarti mulai di x dan berhenti di sebelum y
print(b[2:])
print(b[:-3])

# Modify string
c = " Wleeo WlEEoO       "
print(c.strip()) # Menghilangkan whitespace
print(c.upper()) # Bikin semuanya huruf besar
print(c.lower()) # Bikin semuanya huruf kecil
print(c.title()) # Bikin jadi seperti judul, huruf besar di awal setiap kalimat
print(c.replace("e", "+")) # Ganti huruf e jadi +

# Split
text = "I came,I saw,I conquered"
a,b,c = text.split(",") # Memisahkan text tadi jadi 3 varaibel, dengan tanda pemisahnya ","
print(a, b, c)

# String Concatenation
a = "Python"
b = "V.3.13.11"
print(a + " " + b)

print("Ini \"bapak\" budi")