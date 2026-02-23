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

def simbol(cr, nilai):
    match cr:
        case "EUR":
            return(f"€{nilai}")
        case "IDR":
            return(f"RP {nilai}")
        case "USD":
            return(f"${nilai}")
        case "JPY":
            return(f"¥{nilai}")
        case "SGD":
            return(f"${nilai}")


def printUang(crA, uangA, crB, uangB):
    nilaiA = f"{uangA:,.2f}"
    nilaiA = nilaiA.replace(",","]").replace(".",",").replace("]",".")
    nilaiB = f"{uangB:,.2f}"
    nilaiB = nilaiB.replace(",","]").replace(".",",").replace("]",".")
    print(f"{simbol(crA, nilaiA)} = {simbol(crB, nilaiB)}")

print(tabulate(kurs_table(), headers="keys", tablefmt="outline"), end="\n\n")

cr1 = inputMataUang("Dari")
cr2 = inputMataUang("Ke")

while True:
    try:
        uangg = float(input("Jumlah: "))
    except ValueError:
        print("[ERROR] Hanya Bisa Angka")
    else:
        break
print()
printUang(cr1, uangg, cr2, convert(uangg,cr1,cr2))
