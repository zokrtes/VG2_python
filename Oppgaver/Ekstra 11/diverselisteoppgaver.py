import numpy

print("oppg1--------------------------")
#1
tall = [1, 4, 6, 16, 12, 15, 10, 21, 28, 30, 45, 64, 44, 55, 23, 53, 10, 89, 96, 44]

print("oppg2--------------------------")
#2
print(tall[0])

print("oppg3--------------------------")
#3
print(tall[-1])

print("oppg4--------------------------")
#4
summet=0
for count in range (len(tall)):
    summet += tall[count]
print(summet)
print("oppg5--------------------------")
#5
x = summet/len(tall)
print(x)

print("oppg6--------------------------")
#6
tall.sort()
print(tall)
m = tall[-1] + tall[-2] + tall[-3]
print(m/3)

print("oppg7--------------------------")
#7
print(tall[15] + tall[16] / 2)

print("oppg8--------------------------")
#8
def gangtall():
    for count in range (0, 20):
        print(tall[count]*3)
gangtall()

print("oppg9--------------------------")
#9
ordliste = []
for count in range (0, 3):
    item = input("Skriv inn liste element: ")
    ordliste.append(item)

print(ordliste)

nyliste = []

for count in range (0, len(ordliste)):
    nyliste.append(len(ordliste[count]))

print(nyliste)
