#LISTER

#Lag en liste
listebab = ["Svein", "Tore", "Ove"]

#skriv ut en liste
print(listebab)

#kontroller at det er en liste
print(type(listebab))

#hvor mange elementer inneholder en liste 
print(len(listebab))

#lag en tom liste
tom_liste = []

#legg til elementer i listen
tom_liste.append("Montana")
tom_liste.append("Hanna")
listebab.append("Tore")
print(tom_liste)
print(listebab)

#les et element i listebab
print(listebab[0])

#skriv ut fra et element til ett annet, teller fra 0:2 0 til 1
print(listebab[0:2])

#skriv ut siste element i listen
print(listebab[-1])
#skriv ut nest siste element i listen
print(listebab[-2])

listebab[3] = "Ole"

print(listebab)

#slett liste, sletter første elementet den finner, bruk loop for å slette til den ikke finner flere ved samme verdi
listebab.remove("Tore")
print(listebab)

navn = "Erik"
print(navn[1])

#for løkke
for i in range (0, len(listebab)):
    print(listebab[i])