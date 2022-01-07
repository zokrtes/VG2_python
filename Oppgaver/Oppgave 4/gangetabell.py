# variabel med int og input type, "Velg tall mellom 1-10"
gangetabell = int(input("Gangetabell du vil regne ut: "))

print("Her er ", gangetabell, " gangen")
print("-------------------------------")

# for løkke med teller variabel som in range start verdi på 1 og slutt verdi på 11
for teller in range(1, 11):
    # print som ganger teller med gangetabell inputen din
    print(teller*gangetabell)