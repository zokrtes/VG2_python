import random


lengde = int(input("Tast inn lengde på passordet ditt: "))
passord = []

for count in range (0, lengde):
    passord.append(chr(random.randint(48, 127)))

passordcopy = ''.join(map(str, passord))

print(passordcopy)

