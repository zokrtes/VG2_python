barnpris = 80
ungpris = 100
voksen = 120

antall_pers = int(input("Hovr mange skal på kino?"))

aldsjk = str(input("Er det flere enn en aldersgruppe? J/N ")).lower()

if aldsjk == "j":
    print("ja")
    ant_barn = int(input("antall barn(2-12 år)?"))

elif aldsjk == "n":
    print("nei")