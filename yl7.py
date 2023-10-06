#Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)

#Sisesta arv a

a = int(input("Sisestage täisarv: "))

if a % 2:
    print(a, "on paaritu arv:")
else:
    print(a, "on paaris arv:")
        
