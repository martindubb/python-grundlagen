# neues auto: VOLVO! muss mit in den fuhrpark aufgenommen werden!

# datei öffnen
datei = open("fuhrpark.txt", "a+")

# datei schreiben
inhalt = "Volvo\n"
datei.write(inhalt)

inhalt = "Tesla\n"
datei.write(inhalt)

# datei schließen
datei.close()