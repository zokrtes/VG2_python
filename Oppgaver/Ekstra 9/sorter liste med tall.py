t = [16,87,5,79,41,4,39,104,6,99,13,66,10]

print("t = ", t)

def sortertall():
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                t[i], t[j] = t[j], t[i]

sortertall()

print("t = ", t)