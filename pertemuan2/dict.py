mahasiswa = {
    "M001" : {
        "nama" : "Rina",
        "prodi" : "Informatika",
        "ipk" : 3.6
    },
    "M002" : {
        "nama" : "Doni",
        "prodi" : "Sistem Informasi",
        "ipk" : 3.25
    },
    "M003" : {
        "nama" : "Lina",
        "prodi" : "Informatika",
        "ipk" : 3.8
    }
}

infor = []
ipk_infor = []

for i in mahasiswa:
    if mahasiswa[i]["prodi"] == "Informatika" and mahasiswa[i]["ipk"] >= 3.5:
        infor.append(mahasiswa[i]["nama"])
print(infor)

rataan = 0.0
for i in mahasiswa:
    rataan += mahasiswa[i]["ipk"]

rataan = rataan / len(mahasiswa)
print(rataan)


mahasiswa.update({"M004":{"nama":"Said", "prodi":"Informatika", "ipk":4}})
print(mahasiswa)