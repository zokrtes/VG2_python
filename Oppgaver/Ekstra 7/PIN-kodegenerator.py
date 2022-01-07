import random

gangersiffer = int(input("Hvor lang skal PIN koden være?"))

pinkode = []

for i in range(0, gangersiffer):
    a = random.randint(0, 9)
    pinkode.append(a)

print("Her er din ", gangersiffer, " sifferede PIN")
print(pinkode)