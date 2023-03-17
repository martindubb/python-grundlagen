# eine variable: speichere "banane" in der variable obst
obst = "banane"
print(obst)

o_b_s_t = "apfel"
print(o_b_s_t)

_obst_ = "kirsche"
print(_obst_)

# DAS GEHT NICHT: 
# ob-st = "ananas"

ObSt1 = "mango"
print(ObSt1)

# keyword
# int ist kein keyword!
'''
int = "AWS-23-02"
x = int(5)
print(x)

keywords, die nicht als variable benutzt werden dürfen:
for while if else def False True and ...
'''


# neuzuweisung einer variable
obst = "melone"
print(obst)
obst = "keine gurke"
print(obst)



# datentypen
a = 5 # int
b = 3.14 # float
c = "hallo" # string
d = 'hallo' # string
e = False # bool
f = ["banane", "mango"] # liste
f.append("apfel") # hinzufügen zu einer liste
print(f)
print("das hier ist das erste element: ", f[0])

g = ("banane", "mango") # tupel, unveränderlich
print("das hier ist das zweite element aus dem tupel", g[1])

h = {"banane", "mango"} # set
# i = {"banane", "banane"} # sets sind unique!

# dictionary: key-value-pais
i = {"name": "alice", "alter": 22}
print(i)
print(type(i))
# zugriff auf 'value' über 'key'
print(i["alter"])
print(i["name"])

# kommentar