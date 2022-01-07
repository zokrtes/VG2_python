#   lag to variabler for kari og henrik som er deklarert med input
kari_alder = input("Kari sin alder: ")
henrik_alder = input("henrik sin alder: ")

#   if setning som sier: hvis kari sin interger verdi er større en henrik så printer den "kari er eldst"
if int(kari_alder) > int(henrik_alder):
    print("Kari er eldst")
#   elif som sier hvis kari sin interger verdi er mindre enn henrik så print henrik er eldst
elif int(kari_alder) < int(henrik_alder):
    print("Henrik er eldst")
#   else som sier begge er like gammle
else:
    print("begge er like gammle")
#   
#
#
#
#
#
#