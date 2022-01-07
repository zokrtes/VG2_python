"""
def tekst_til_skjerm(navn):
    for teller in range(10):
        print("Hei på deg", navn)

svar = input("Tast inn navn: ")

tekst_til_skjerm(svar)
"""

def areal_sirkel(radius):
    areal = 3.14 * radius**2
    return areal

yooy = float(input("Oppgi radius: "))
print(areal_sirkel(yooy))



