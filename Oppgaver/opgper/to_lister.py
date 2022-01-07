import datetime

# bt_hp er en liste med holdeplasser på en bussrute fra Gulset til Porsgrunn
bt_hp = ["Gulsetsenteret","Ravnåsen","Myren","Skien Landmannstorget","Rådhusplassen","Bøle","Borgestad","Porsgrunn Kammerherreløkka"]

# bt_t er en liste som viser tiden i minutter det tar fra Gulsetsenteret og til aktuell holdeplass.
# Denne listen viser at det tar 6 minutter til Ravnåsen, 11 minutter til Myren, osv.
bt_t = [0,6,11,16,17,21,25,35]

print("Ny bussrute fra Gulset (M1)\n")

time = int(input("oppgi start i timer: "))
minutter = int(input("oppgi start i minutter: "))
dt = datetime.datetime(2021, 1, 1, 1, 1)
newdatetime = dt.replace(hour=time, minute=minutter)

print(newdatetime)

for i in range(0, 8):
    print(bt_hp[i], newdatetime.hour, newdatetime.minute + bt_t[i])


# vet dette ikke er riktig, prøvde så godt jeg kunne (hadde jeg bare hatt litt mer tid)

