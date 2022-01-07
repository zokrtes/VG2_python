print("---------FERIEPENGE KALKULATOR-----------")

navn = input("Navn: ")
arslonn = float(input("For i fjors årslønn: "))
alder = int(input("Alder: "))

print("--------------------")


if alder < 1:
    print("Ugyldig alder, prøv igjen, Husk tallen kan kun være hele og ikke mindre enn")
elif alder >= 60:
    feriepenger = 0.125 * arslonn
    print("Dine feriepenger: ", feriepenger, "kr")
elif alder < 60:
    feriepenger = 0.102 * arslonn
    print("Dine feriepenger: ", feriepenger, "kr")
