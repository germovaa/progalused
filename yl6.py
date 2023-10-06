#Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni).
# (loogikatehted - logic operators)

 # Küsime kasutajalt esimese arvu sisestamist
a = int(input("Sisestage esimene arv a: "))

 # Küsime kasutajalt teise arvu sisestamist
b = int(input("Sisestage teine arv b: "))

# Küsime kasutajalt kolmanda arvu sisestamist
c = int(input("Sisestage teine arv c: "))

# Kontrollime, kasutajate poolt sisestatud arvust maksimumi

if a > b and a > c:
    print("maximum on a:", a)
elif b > c:
    print("maximum on b:" , b)
else:
    print("maximum on c:" , c)