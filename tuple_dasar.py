# Tuple: tidak bisa diubah setelah dibuat
warna = ("kuning", "ungu", "hitam")

# Akses elemen
print(warna[1]) # ungu

# Tuple tidak bisa diubah
# warna[0] = "merah" # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)
