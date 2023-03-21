# datei öffnen
datei = open("fuhrpark.txt", "r")

# inhalt aus datei lesen
inhalt = datei.read()
datei.close()
# inhalt zu liste umkonvertieren
alle_zeilen = inhalt.split()
# liste sortieren
alle_zeilen.sort()

# neue datei öffnen
datei_sortiert = open("fuhrpark_sortiert.txt", "w")

# sortierten inhalt in datei schreiben
for i in alle_zeilen:
    datei_sortiert.write(i + "\n")

# neue datei schließen
datei_sortiert.close()

# ausgabe der sortierten liste
for i in alle_zeilen:
    print(i)