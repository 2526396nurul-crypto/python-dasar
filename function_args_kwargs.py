# *args dan **kwargs
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(5, 10, 15, 20) # Bisa input banyak angka

def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Nurul", sekolah="SMKN 2 Subang", kota="Subang")
