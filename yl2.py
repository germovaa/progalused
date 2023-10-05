#Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
from math import pi

radius = float(input("Sisesta raadius: "))

area = pi * radius ** 2
print("Pindala:", area)

perimeter = 2* pi * radius
print("Ümbermõõt:", perimeter)