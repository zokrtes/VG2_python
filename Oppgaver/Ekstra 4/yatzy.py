import random


def func():
    antall_runder = 0
    while True:
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        terning3 = random.randint(1,6)
        terning4 = random.randint(1,6)
        terning5 = random.randint(1,6)
        print(antall_runder, terning1, terning2, terning3, terning4, terning5)
        antall_runder += 1
        if terning1 == terning2 == terning3 == terning4 == terning5:
            print("yay", antall_runder)
            break

print("-----FÅ YATZY!-----")

start = input("Trykk hvilken som helst knapp for å starte")

func()

print("f2")