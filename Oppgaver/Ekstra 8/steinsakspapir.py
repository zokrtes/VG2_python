# import random
import random
# en valglist med stein saks papir som elementene
valglist = ["stein", "saks", "papir"]
# en variabel som teller runder
runder = 0
# en poeng variabel
poeng = 0
cpu_poeng = 0

ikke_ferdig = True

print("--------------------STEIN, SAKS, PAPIR--------------------")

# while løkke som kjører til den er stoppet
while ikke_ferdig:
    # en variabel med str input()
    bruker_inp = input("stein, saks eller papir: ").lower()
    # variabel som har random.choice(valglist) som verdi
    cp_inp = random.choice(valglist)
    # if setning som sjekker om inputen din er riktig
    # elif setning som sjekker om brukeren har samme verdi
    if bruker_inp == cp_inp:
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("Det ble likt, ingen poeng trukket eller gitt.")
    # elif setning som sjekker om brukeren har gitt en verdi som er bedre enn cpu'ens valg
    elif bruker_inp == "stein" and cp_inp == "saks":
        # print du vant og gi poeng variabelen -1, og +1 runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("Bruker fikk +1 poeng")
        poeng += 1
        runder +=1
    # elif setning som sjekker om brukeren har gitt en verdi som er dårligere enn cpu'ens valg
    elif bruker_inp == "saks" and cp_inp == "stein":
        # print du vant og gi poeng variabelen +1,  og minus runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("CPU fikk +1 poeng")
        cpu_poeng +=1
        runder +=1
    # elif setning som sjekker om brukeren har gitt en verdi som er bedre enn cpu'ens valg
    elif bruker_inp == "papir" and cp_inp == "stein":
        # print du vant og gi poeng variabelen -1, og +1 runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("Bruker fikk +1 poeng")
        poeng += 1
        runder +=1
    # elif setning som sjekker om brukeren har gitt en verdi som er dårligere enn cpu'ens valg
    elif bruker_inp == "stein" and cp_inp == "papir":
        # print du vant og gi poeng variabelen -1, og +1 runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("CPU fikk +1 poeng")
        cpu_poeng +=1
        runder +=1
    # elif setning som sjekker om brukeren har gitt en verdi som er bedre enn cpu'ens valg
    elif bruker_inp == "saks" and cp_inp == "papir":
        # print du vant og gi poeng variabelen -1, og +1 runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("Bruker fikk +1 poeng")
        poeng += 1
        runder +=1
    # elif setning som sjekker om brukeren har gitt en verdi som er dårligere enn cpu'ens valg
    elif bruker_inp == "papir" and cp_inp == "saks":
        # print du vant og gi poeng variabelen -1, og +1 runde variabelen
        print("Bruker valgte: ", bruker_inp, "\n" "CPU valgte: ", cp_inp)
        print("CPU fikk +1 poeng")
        cpu_poeng +=1
        runder +=1
    # else setning som bryter while løkken 
    else:
        print("Feil: Du må skrive inn enten, stein, saks eller papir")
    if poeng >= 3:
        ikke_ferdig = False
    elif cpu_poeng >= 3:
        ikke_ferdig = False
    

print("-------RESULTAT-------")
if poeng >= 3:
    print("DU VANT SPILLET")
elif cpu_poeng >= 3:
    print("CPU VANT SPILLET")
print()
print("Dine Poeng: ", poeng)
print("CPU poeng: ", cpu_poeng)
print()