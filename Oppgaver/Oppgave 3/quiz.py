#   Lag varaibel med interger datatype kalt poeng
poeng = 0

#   skriv til skjerm: Du har nå startet quizen
print("ERIKS QUIZ")

#navn variabel med string input
navn = input("Ditt navn: ")
#   skriv til skjerm: Hvem eier huset her?

print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hva heter læreren min")
print("a) Sturle b) Max c) Ole")
#   Lag variabel kalt svar
#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "a":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   skriv til skjerm: (spørsmål her)?
print("----------------")
print("Hvem er kongen av Norge den dag idag?")
print("a) statensvegvesen b) moren din c) Harald")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "c":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   skriv til skjerm: (spørsmål her)?
print("----------------")
print("Hva heter han som lagde quizen?")
print("a) Erik b) Geir c) Elias")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "a":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hvor mange bor det i norge?")
print("a) 5,6 mil b) 6 miln c) 4,6 mil")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "a":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hvilke program ble brukt til å skrive denne koden?")
print("a) paint b) notepad c) Visual studio code")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "c":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")
    
#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hva heter bussterminalen i skien")
print("a) landsemtorget b) 6 miln c) 4,6 mil")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "a":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hvordan staves GOOGLE")
print("a) Goggle b) Google c) Giggle")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "b":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Når endte den kalde krigen")
print("a) 1991 b) 1990 c) 1989")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "a":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hvem stemte mot rusreformen i Norge 2021")
print("a) FRP b) AP c) SP")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "b":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#   lag if setning som sjekker om svar er riktig
print("----------------")
#   skriv til skjerm: (spørsmål her)?
print("Hvor lang tid tar det før bomben sprenger i CSGO")
print("a) 42 sek b) 40 sek c) 45 sek")

#   bruker taster inn svar
svar = input("ditt svar: ").lower()

#   lag if setning som sjekker om svar er riktig
if svar == "b":
    poeng += 1
    print("----------------")
    print("Riktig!")
#lag else setning som sier at du er feil hvis du svarte feil
else:
    poeng -= 1
    print("----------------")
    print("Feil!")

#if setning som sier at hvis poeng summen din er under 0 så blir poeng summen din 0
if poeng < 0:
    poeng = 0


#print setning som sier at quizen er over og viser poen sumen deres
print("----------------")
print("QUIZEN ER OVER")
print("----------------")
print("Din poeng sum: ", poeng)

#if setninger som bestemer hvor smart du er og gir en kommentar basert på poeng sum?
if poeng > 10:
    print(navn, " Du er en gud")

if poeng > 9:
    print(navn, " IQ på 160")

if poeng > 6:
    print(navn, " IQ på 100")

if poeng > 3:
    print(navn, " Du er nesten et vasshue")

else:
    print(navn, " Du er en dass!")

input("trykk hva som helst for å avslutte.")