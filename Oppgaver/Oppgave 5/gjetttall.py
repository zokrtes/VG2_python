# importer random
import random

# tittel på program skrives til skjerm
print("gjett tallet som skrives")

# string input der bruker kan taste inn hva de tror tallet kommer til å bli
input_str = input("gjett ett tall fra 1-10: ")

# gjør input string om til interger
tall = int(input_str)

# variabel som får en random interger verdi
tilfeldig = random.randint(1,10)

# variabel med data type interger, som teller antall ganger bruker har gjettet
forsokbrukt = 0

# en whileløkke som kjøres når randomverdi ikke er lik inputen
while tilfeldig != tall:

    # if setning som sjekker om random variabelen er lavere en inputen int variabelen
    if tilfeldig > tall:
        print("Feil, tallet er for lavt")
        input_str = input("gjett ett tall fra 1-10: ")
        tall = int(input_str)
        forsokbrukt += 1

    # elif setning som sjekker om random er høyere enn input
    elif tilfeldig < tall:
        print("Feil, tallet er for høyt")
        input_str = input("gjett ett tall fra 1-10: ")
        tall = int(input_str)
        forsokbrukt += 1

# else setning som kun skrives ut når brukeren fikk riktig. Skriver også ut hvor mange
else:
    forsokbrukt += 1
    print("Du vant!")
    print("Tallet var: ", tilfeldig)
    print("Forsøk brukt: ", forsokbrukt)