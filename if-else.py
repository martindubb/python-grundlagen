# if-else
alter = 17.5
if (alter < 17.6):
    print("du bist nicht volljährig")
elif (alter > 18.0):
    print("du bist volljährig")
else:
    print("du bist genau 18!")


# string vergleich
farbe = "grün"
if (farbe == "grün"):
    print("die farbe ist grün")
else:
    print("die farbe ist nicht grün")


# ist X in liste enthalten?
klamotten = ["hose", "shirt", "socken", "pullover"]
kleidungsstück = "shorts"
if kleidungsstück in klamotten:
    print("JA")
else:
    print("NEIN")
