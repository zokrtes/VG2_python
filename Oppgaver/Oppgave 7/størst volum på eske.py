# definer en funksjon ved navn beregnvolum
def beregnvolum(hoyde):
# inni funksjonenen skal det ligge en formel, som er volum = lengde * bredde * hoyde, deretter returner volum
    volum = hoyde * (29.7 - 2 * hoyde) * (21 - 2 * hoyde)
    return volum

# lag en variabel med input som float datatype, der brukeren skal skrive inn høyden på sidene på arket deres.
hoydeinp = float(input("Oppgi høyde på papir boksen: "))

# kall funksjon i en print med høyde inputen inni parentesene
print("Volum: ", beregnvolum(hoydeinp),"cm")

#lag variabel med 0 som verdi. lag liste uten noen verdi.
hoydetest = 0
testeliste = []

# for løkke som regner ut volum formelen 10 ganger og putter den i en liste
for teller in range (10):
    hoydetest += 1
    volum2 = hoydetest * (29.7 - 2 * hoydetest) * (21 - 2 * hoydetest)
    testeliste.append(volum2)
print(testeliste)