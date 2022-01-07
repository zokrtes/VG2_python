# variabel der bruker skal oppgi kjøpssum_inp
kjopssum_inp = input("Oppgi kjøpssum: ")
# en variabel som gjør kjopssum_inp om til interger
kjopssum = int(kjopssum_inp)
# variabel der bruker skal oppgi lappen han har
brukernspenger_inp = input("Oppgi brukerens penger: ")
# en variabel som gjør brukernspenger om til interger
brukernspenger = int(brukernspenger_inp)
# variabel som regner ut hvormange penger han skal få tilbake
vekslepenger = brukernspenger - kjopssum

# if setninger som sjekker hva bruker har betalt med
if vekslepenger >= 500:
    print("antall 500 lapper tilbake: ", vekslepenger // 500)
    vekslepenger = vekslepenger % 500

if vekslepenger >= 200:
    print("antall 200 lapper tilbake: ", vekslepenger // 200)
    vekslepenger = vekslepenger % 200

if vekslepenger >= 100:
    print("antall 100 lapper tilbake: ", vekslepenger // 100)
    vekslepenger = vekslepenger % 100

if vekslepenger >= 50:
    print("antall 50 lapper tilbake: ", vekslepenger // 50)
    vekslepenger = vekslepenger % 50

if vekslepenger >= 20:
    print("antall 20 kroner tilbake: ", vekslepenger // 20)
    vekslepenger = vekslepenger % 20

if vekslepenger >= 10:
    print("antall 10 kroner tilbake: ", vekslepenger // 10)
    vekslepenger = vekslepenger % 10

if vekslepenger >= 5:
    print("antall 5 kroner tilbake: ", vekslepenger // 5)
    vekslepenger = vekslepenger % 5

if vekslepenger >= 1:
    print("antall 1 kroner tilbake: ", vekslepenger // 1)
    vekslepenger = vekslepenger % 1

# print som sier hvor mye penger du får tilbake totalt
print("Du får tibake", brukernspenger - kjopssum)
