# funktionen mit rückgabewerten

# funktion, um zu prüfen, ob zutat in zutatenliste
# funktion gibt etwas zurück
def check_zutat(eine_zutat):
    if eine_zutat in alle_zutaten:
        return True
    else:
        return False

alle_zutaten = ["eier", "mehl", "milch", "backpulver", "apfel", "butter", "zucker"]

# ist zutat in der zutatenliste?
zutat = "eier"
ergebnis = check_zutat(zutat) # funktionsaufruf mit parameter
if ergebnis == True: 
    ergebnis_deutsch = "Ja"
else:
    ergebnis_deutsch = "Nein"
print("Ist " + zutat + " in der Liste? " + ergebnis_deutsch)

zutat = "banane"
ergebnis = check_zutat(zutat) # funktionsaufruf mit parameter
print("Ist " + zutat + " in der Liste? " + str(ergebnis))