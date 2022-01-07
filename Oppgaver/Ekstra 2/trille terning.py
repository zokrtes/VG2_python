import random

print("-----TRILL TALLET 6-----")

terning = random.randint(1,6)

print(terning)

if terning == 6:
    print("Hurra, Du fikk seksern!")

elif terning < 6:
    print("Prøv igjen")
	
input()

