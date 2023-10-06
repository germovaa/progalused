#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni).
# (muutuja - variable, tingimus - condition, if-lause - if statement)

 # Küsime kasutajalt esimese arvu sisestamist
a = float(input("Sisestage esimene arv a: "))

 # Küsime kasutajalt teise arvu sisestamist
b = float(input("Sisestage teine arv b: "))

 # Kontrollime, kumb arv on väiksem
if a < b:
    minimum = a
else:
    minimum = b

# Väljastame leitud miinimumi
print("Miinimum on:", minimum)
