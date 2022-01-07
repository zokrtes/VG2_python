import pandas as pd

print("running", pd.__version__, "of pandas")

grades = pd.read_csv("grades.csv", sep = ",", encoding="utf-8")

print(grades.tail(3))