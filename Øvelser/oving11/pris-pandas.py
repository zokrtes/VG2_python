import pandas as pd

mat = pd.read_csv("mat-pris.csv", sep = ";", encoding = "latin-1")

#print(mat)

priser = mat["Pris"]

#mat["Nypriser"] = priser * 1.2
mat["Pris"] = mat["Pris"] * 1.2
print(mat.head(3))

mat.to_csv("nymat-pris.csv", index=False)