# break menghentikan loop, continue melewati satu iterasi
for i in range(1, 9):
    if i == 2:
        continue # lewati angka 2
    if i == 6:
        break # hentikan loop saat i == 6
    print(i)
