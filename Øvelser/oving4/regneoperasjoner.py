#   lag to variabler for tall
tall1_txt = input("Oppgi første verdi: ")
operator = input("Operator for verdi: ")
tall2_txt = input("Oppgi andre verdi: ")

#henter string valuen til tall1_txt og tall2_txt og gjør den om til en float value
tall1 = float(tall1_txt)
tall2 = float(tall2_txt)

#   lag if setninger for de forskjellige operatorene.
if operator == "*":
    print(tall1 * tall2)
elif operator == "-":
    print(tall1 - tall2)
elif operator == "+":
    print(tall1 + tall2)
elif operator == "/":
    print(tall1 / tall2)
else:
    print("Nå har du kødda det til")