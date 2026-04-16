def main():
    plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
    ganjil, genap = ganjilgenap(plat)
    print(f"ganjil: {ganjil}")
    print(f"genap: {genap}")

def ganjilgenap(plat):
    ganjil = []
    genap = []

    for i in plat:
        pisah = i.split(" ")
        nomor = int(pisah[1])
        if ((nomor % 10) % 2) == 0:
            genap.append(i)
        else:
            ganjil.append(i)
    
    return [ganjil,genap]
        

if __name__ == "__main__":
    main()