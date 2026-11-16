# Mengakses data dictionary
siswa = {"nama": "Nurul", "jumlah_pensil": 8, "kota": "Subang"}

print(siswa["nama"]) # Nurul
print(siswa.get("jumlah_pensil")) # 8
print(siswa.get("hobi")) # None, tidak error karena memakai get()
