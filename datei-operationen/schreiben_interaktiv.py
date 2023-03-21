# datei öffnen
datei = open("fuhrpark.txt", "a+")

# benutzereingabe lesen
eingabe = input("Welches Auto soll hinzugefügt werden (Leerzeichen getrennt)? ")
einzelne_autos = eingabe.split(" ")

# datei schreiben
for i in einzelne_autos:
    datei.write(i + "\n")

# datei schließen
datei.close()