# liste med 4 CPUfarger
cpFarge = ["gr", "bl", "ro", "li"]

# liste Brukerfarger
inpFarge = []

#tabell
poeng = 0
runderkjort = 0
rFarger = 0
rPlassert = 0

power = True

print("fasit: ", cpFarge)

# while løkke som kjører til til spillet er ferdig
while power == True:
    inpStr = str(input("tast inn 4 farger separert med kommaer: ")).lower()
    inpFarge = inpStr.split(",")
    print("Du tastet inn: ", inpFarge)

    if inpFarge[0] == cpFarge[0]:
        rPlassert += 1
        print("riktige plassert: ", rPlassert)
    if inpFarge[1] == cpFarge[1]:
        rPlassert += 1
        print("riktige plassert: ", rPlassert)
    if inpFarge[0] == cpFarge[0]:
        rPlassert += 1
        print("riktige plassert: ", rPlassert)
    if inpFarge[0] == cpFarge[0]:
        rPlassert += 1
        print("riktige plassert: ", rPlassert)
# input der du gjetter CPUfarger
# input der du gjetter CPUposisjoner
# splitter farge gjettet ditt
# splitter posisjon gjettet ditt