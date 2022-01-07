import random

print("-----GANGE TABELL OVING-----")

poeng = 0

for teller in range (3):
    tall1 = random.randint(1, 10)
    tall2 = random.randint(1, 10)
    
    x = int(input(f"regn ut: {tall1} * {tall2} "))
    if x == tall1 * tall2:
        print("korrekt!")
        poeng += 1

print("du fikk ", poeng)