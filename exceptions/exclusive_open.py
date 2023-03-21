import os

try:
    # datei öffnen zum schreiben
    datei = open("text.txt", "x")
    # zu schreibenden text definieren
    text = "hallo das hier ist einfacher text"
    # text in datei schreiben
    datei.write(text)
except FileExistsError:
    eingabe = input("die datei existiert schon - soll ich die löschen [J/N]?")
    if eingabe.capitalize() == "J":
        # lösche datei
        os.remove("text.txt")
        print("datei ist gelöscht")
        # erneut anlegen!
        datei = open("text.txt", "x")
except:
    print("etwas ist schief gelaufen")
finally:
    # datei schließen
    datei.close()
    print("Datei wurde geschlossen!")
    print("das hier wird immer ausgeführt!")
