from konverter import convert
from tabulate import tabulate
from kurs import kurs_table


def inputMataUang(ke):
    validasi = ["EUR", "IDR", "SGD", "USD", "JPY"]
    while True:
        uang = input(f"{ke} (IDR/USD/EUR/SGD/JPY): ")
        if uang in validasi:
            return uang
        else:
            print("[ERROR] Mata uang tidak ada (EUR/IDR/SGD/USD/JPY)")

def printUang(cr, uang):
    nilai = f"{uang:,.2f}"
    nilai = nilai.replace(",","]").replace(".",",").replace("]",".")
    match cr:
        case "EUR":
            print(f"€{nilai}")
        case "IDR":
            print(f"RP {nilai}")
        case "USD":
            print(f"${nilai}")
        case "JPY":
            print(f"¥{nilai}")
        case "SGD":
            print(f"${nilai}")
            
print(tabulate(kurs_table(), headers="keys", tablefmt="outline"))

cr1 = inputMataUang("Dari")
cr2 = inputMataUang("Ke")

while True:
    try:
        uangg = float(input("Jumlah: "))
    except ValueError:
        print("[ERROR] Hanya Bisa Angka")
    else:
        break

printUang(cr2, convert(uangg,cr1,cr2))
