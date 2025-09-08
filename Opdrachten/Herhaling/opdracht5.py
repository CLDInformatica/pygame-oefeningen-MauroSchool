# Gegeven is een functie met 2 argumenten:
#   - getal1
#   - getal2

# Return de grootste van deze 2 getallen.
# Voer de functie daarna uit met verschillende waarden en print de uitkomst

def grootste(getal1, getal2):
    if getal1 > getal2:
        print(getal1) 
    elif getal1 < getal2:
        print(getal2)
    else:
        print(f"{getal1} en {getal2} zijn even groot")

getal1 = int(input("geef een getal"))
getal2 = int(input("geef een 2e getal"))
print(grootste(getal1, getal2))