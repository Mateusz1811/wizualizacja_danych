# import random
import math
#
# A = {1 - x for x in range(1, 11)}
# B = {x**2 for x in range(1, 7)}
# C = {x for x in B if x % 2 == 0}
#
# lista1 = [random.randint(1, 100) for i in range(10)]
# nowa_lista = [x for x in lista1 if x % 2 == 0]
# print("Lista1:", lista1)
# print("Nowa_lista (tylko parzyste elementy):", nowa_lista)

# produkty = {
#     "jajka": "sztuki",
#     "bułki": "sztuki",
#     "mleko": "litry",
#     "ser": "gramy",
#     "ziemniaki": "kg",
#     "cebula": "kg"
# }
#
# produkty_sztuki = [produkt for produkt, jednostka in produkty.items() if jednostka == "sztuki"]
#
# print("Słownik produktów spożywczych:", produkty)
# print("Produkty, których wartośćią są sztuki to:", produkty_sztuki)
#
# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return True
#     else:
#         return False
#
# print(trojkat_prostokatny(3, 4, 5))
# print(trojkat_prostokatny(5,12,13))
# print(trojkat_prostokatny(3,5,7))

def pole_trapezu(a=0, b=0, h=0):
    return 0.5 * (a + b) * h

print(pole_trapezu())
print(pole_trapezu(4,6,5))
print(pole_trapezu(h=8))

def iloczyn_ciagu(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile - 1):
        a *= b
        iloczyn *= a
    return iloczyn

print(iloczyn_ciagu())
print(iloczyn_ciagu(2,3))
print(iloczyn_ciagu(2,3,5))

try:
    x = float(input("Podaj liczbę: "))
    if x < 0:
        raise ValueError("Nie da się obliczyć pierwiastka z liczby ujemnej!")
    pierwiastek = math.sqrt(x)
    print(f"Pierwiastek z liczby {x} wynosi {pierwiastek}")
except ValueError as error:
    print("Błąd:", error)

