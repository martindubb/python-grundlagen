zahl1 = input("Bitte erste Zahl angeben: ")
zahl2 = input("Bitte zweite Zahl angeben: ")

try:
    ergebnis = int(zahl1) / int(zahl2)
except ZeroDivisionError:
    print("DURCH 0 TEILEN GEHT NICHT!")
except ValueError:
    print("BITTE EINE ZAHL EINGEBEN!")
else:
    print(ergebnis)
finally:
    print("schönen tag auch!")
