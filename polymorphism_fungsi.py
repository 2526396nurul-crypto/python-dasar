# Polymorphism dengan fungsi
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())

# Fungsi bawaan len() juga polymorphism
print(len("Nurul")) # string
print(len([11, 22, 33, 44, 55, 66])) # list
print(len({"a": 1, "b": 2, "c": 3})) # dictionary
