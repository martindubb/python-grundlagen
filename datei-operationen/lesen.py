# datei oeffnen
datei = open("fuhrpark.txt", "r")

# kompletten inhalt der datei in eine variable lesen
inhalt = datei.read()
# einzelne zeilen in liste schreiben
inhalt = inhalt.split()

# über liste iterieren und inhalt zeilenweise ausgeben
laenge = len(inhalt)
for i in range(laenge):
    print(i+1, inhalt[i])

# datei schließen
datei.close()