# funktionen

# funnktion, um zu prüfen, ob zutat in zutatenliste
def check_zutat(zutat):
    if zutat in alle_zutaten:
        print("JA " + zutat + " ist dabei")
    else:
        print("NEIN " + zutat + " ist nicht dabei")

alle_zutaten =["eier", "mehl", "milch", "backpulver", "apfel", "butter", "zucker"]

# ist x in der zutatenliste?
zutat = "eier"
check_zutat(zutat) # funktionsaufruf

zutat = "mehl"
check_zutat(zutat) # funktionsaufruf

zutat = "banane"
check_zutat(zutat) # funktionsaufruf
