import random

# en liten jukse metode (for å ungå logikk), lager unike tall uten å måtte kode så mye
lottoliste = [random.sample(range(1, 35), 7)]
lottoliste.sort()

def lottotest():
    antall_runder = 0
    while (1):
        lottoliste = [random.randrange(1, 35, 1) for i in range(7)]
        print(antall_runder, lottoliste)
        antall_runder += 1
        if tall1 == lottoliste[0] and tall2 == lottoliste[1] and tall3 == lottoliste[2] and tall4 == lottoliste[3] and tall5 == lottoliste[4] and tall6 == lottoliste[5] and tall7 == lottoliste[6]:
            print("Det tok antall runder:", antall_runder)
            break


print(lottoliste)
print("-----LOTTO SPILL-----")
print("Først må du skrive inn 7 tall som du tror kommer til å vinne")

tall1 = int(input("tast inn ditt 1 tall: "))
tall2 = int(input("tast inn ditt 2 tall: "))
tall3 = int(input("tast inn ditt 3 tall: "))
tall4 = int(input("tast inn ditt 4 tall: "))
tall5 = int(input("tast inn ditt 5 tall: "))
tall6 = int(input("tast inn ditt 6 tall: "))
tall7 = int(input("tast inn ditt 7 tall: "))

print("dine tall: ", tall1, tall2, tall3, tall4, tall5, tall6, tall7)
lottotest()


