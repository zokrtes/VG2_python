import random

print("-----FÅ 2 LIKE-----")

terning = random.randint(1,6)
terning2 = random.randint(1,6)

print(terning)
print(terning2)

if terning == terning2:
    print("Hurra! DU fikk to like!")

elif terning < 6:
    print("Prøv igjen")