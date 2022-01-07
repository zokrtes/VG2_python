# variabel med int og input type, "Velg gangetabell mellom 1-10: "
gangetabell = int(input("Velg gangetabell mellom 1-10: "))

#lag en tom liste
listetabell = []

if gangetabell >= 11:
    print("Jeg sa spesefikt at du skulle velge ett tall mellom 1-10, det betyr altså ikke over 10")
elif gangetabell == 0:
    print("Er du dum elle? kan ikke gange med null")
elif gangetabell <= 0:
    print("Ikke noen minus tall heller, igjen velge ett tall mellom 1-10!")
else:
    # for løkke med teller variabel som in range start verdi på 1 og slutt verdi på 11
    for i in range(1, 11):
        # liste med append method som ganger teller med gangetabell inputen
        listetabell.append(i*gangetabell)
    #print ut liste
    print("----------", gangetabell, "gangen ----------")
    print(listetabell)
    print("------------------------------")

