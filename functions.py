# funktionen

# funktion, um zu prüfen, ob zutat in zutatenliste
# variable 'zutat' ist hier verfügbar!
def check_zutat():
    if zutat in alle_zutaten:
        print("JA " + zutat + " ist dabei")
    else:
        print("NEIN " + zutat + " ist nicht dabei")

alle_zutaten =["eier", "mehl", "milch", "backpulver", "apfel", "butter", "zucker"]

# ist zutat in der zutatenliste?
zutat = "eier"
check_zutat() # funktionsaufruf

zutat = "mehl"
check_zutat() # funktionsaufruf

zutat = "banane"
check_zutat() # funktionsaufruf
