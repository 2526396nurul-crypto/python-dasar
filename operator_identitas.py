# Operator identitas
a = [7, 8, 9]
b = a
c = [7, 8, 9]

print(a is b) # True (b menunjuk objek yang sama dengan a)
print(a is c) # False (c objek berbeda walau isinya sama)
print(a == c) # True (nilai isinya sama)
