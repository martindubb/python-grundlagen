# funktionen mit parameter

# funktion, um zu prüfen, ob zutat in zutatenliste
# variable 'zutat' ist hier verfügbar!
def check_zutat(eine_zutat):
    if eine_zutat in alle_zutaten:
        print("JA " + eine_zutat + " ist dabei")
    else:
        print("NEIN " + eine_zutat + " ist nicht dabei")

alle_zutaten =["eier", "mehl", "milch", "backpulver", "apfel", "butter", "zucker"]

# ist zutat in der zutatenliste?
check_zutat("eier") # funktionsaufruf mit parameter
check_zutat(alle_zutaten[2]) # funktionsaufruf mit parameter
check_zutat("banane") # funktionsaufruf mit parameter

# wenn man die liste überschreibt im späteren verlauf?
alle_zutaten = ["pizzateig", "tomatensoße", "käse"]
check_zutat("eier") # funktionsaufruf mit parameter
check_zutat(alle_zutaten[2]) # funktionsaufruf mit parameter

# parameter sind hier zwingend erforderlich!
# ohne parameter kommt ein fehler:
# check_zutat()