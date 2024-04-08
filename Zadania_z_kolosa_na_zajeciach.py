import math
import random

def zad1():
    a = 0
    for i in range(4, 10):
        a += i
        wynik = math.pow(math.e**a + math.log2(24), 1/4)
        wynik = round(wynik, 2)
    print(wynik)

zad1()

def zad2(ile, n):
    if ile < n:
        return None
    lista = []
    for i in range(ile):
        lista.extend([random.randint(1,20)] * n)
    return lista

print(zad2(10,3))

def zad4():
    try:
        r = float(input("Podaj promien kola: "))
        if r <= 0:
            raise ValueError("Promien musi byc liczba dodatnia. ")
        a = math.pi * r ** 2
        return a
    except ValueError as e:
        print("Wystąpił błąd: ", e)
        return None
wynik = zad4()
if wynik is not None:
    print("Pole koła wynosi: ", wynik)




