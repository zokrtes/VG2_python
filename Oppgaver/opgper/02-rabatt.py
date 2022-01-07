# definer en ny funksjon som beregner ny pris med en bestemt rabattsats
def prisOgRabatt():
    # inndata for pris
    pris = float(input("Pris på gjenstand: "))
    # inndata for rabatt prosent
    rabatt = float(input("Rabatt prosent: "))

    # if setninger som sjekker om den er over 100% eller mindre en 1%
    if rabatt <= 0 or rabatt >= 101:
        print("ugyldig, velg en prosent fra 0-100 ")
    else:
        # under else: formel for å regne ut ny pris
        nypris = pris - pris * rabatt/100
        print("Nypris", nypris, "Kr") 

#kjør funksjonen
prisOgRabatt()


