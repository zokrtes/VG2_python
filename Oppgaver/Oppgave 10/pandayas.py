import pandas as pd

mat = pd.read_csv("mat-pris.csv", sep = ";", encoding="latin-1")

print("---kollenneoverskrifter---")
print(mat.columns)

print("---Første fire radene---")
print(mat.head(4))

print("---Siste fire radene---")
print(mat.tail(4))

print("---alle rader med Kategori lik «Melk»---")
print(mat.loc[mat.Kategori == "Melk"])

print("---rad med ID lik 222---")
print(mat.loc[mat.ID == 222])

print("---Endre 'Sau' til 'Fe' for ID lik 221 ---")
mat.loc[mat.ID == 221, "Kategori"] = "Fe"
print(mat.loc[mat.ID == 221])

print("---Endre Pris på ID lik 222 til kr 100---")
mat.loc[mat.ID == 222, "Pris"] = 100
print(mat.loc[mat.ID == 222])

print("---Øk Pris med 50% på alle varer med Kategori lik 'Fe'---")
mat.loc[mat.Kategori == "Fe", "Pris"] = mat.loc[mat.Kategori == "Fe", "Pris"] * 1.5
print(mat.loc[mat.Kategori == "Fe"])

print("---Skriver ut den endrede matoversikten til filen 'ny-mat-pris.csv'---")
mat.to_csv("ny-mat-pris.csv", index=False)
print("---Utskrift Ferdig---")
