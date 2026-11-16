# Tanpa exception handling, program langsung berhenti:
# hasil = 36 / 0 # ZeroDivisionError: division by zero

# Menangani error dengan try-except
try:
    angka = 36
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
