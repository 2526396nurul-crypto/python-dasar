# Membuat exception sendiri dengan raise
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)

try:
    cek_umur(19)
    cek_umur(-3)
except ValueError as e:
    print("Error:", e)
