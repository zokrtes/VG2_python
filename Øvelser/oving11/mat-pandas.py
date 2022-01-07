import pandas as pd

# hent in CSV-fil
mat = pd.read_csv("mat-innhold.csv", sep = ";", encoding = "latin-1")

#vis innhold i dataframe
#print(mat.head(3))
#print(mat.tail(3))
#print(mat.columns)

#se spesifike kolloner
print(mat["Matvare"][100:105])