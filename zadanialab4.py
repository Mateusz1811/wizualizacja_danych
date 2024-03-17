import math
import random

#zad1

# a = math.pow(math.exp(4) - math.log2(34), 1/3)
# a = round(a, 2)
# b = math.pow(math.log(20) + math.cos(45) + math.e, 1/3)
# b = round(b, 2)
# c = math.pow(math.log(20, 3) + math.sin(45) * (5/8), 1/4)
# c = round(c, 2)
# d = math.log(23, 3) + math.pow(math.sin(34) + 5, 1/3)
# d = round(d, 2)
# e = math.pow(math.log2(32) + math.pi + math.sin(56), 1/4)
# e = round(e, 2)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#zad2

def wierza(n):
    if n < 10 | n < 1:
        print("zla wartosc n")
    else:
        for i in range(1, n+1):
            for j in range(0, i):
                print('A', end='')
            print()
wierza(2)

def piramida(n):
    if n < 10 | n < 1:
        print("zla wartosc")
    else:
        a = 2*n
        for i in range(n):
            for j in range(a):
                if j == a/2:
                    print("A", end='')
                elif (j >= a/2 - i) & (j < a/2):
                    print("A", end='')
                elif (j > a/2) & (j <= a/2 + i):
                    print("A", end='')
                else:
                    print(" ", end='')
            print('')
piramida(10)

#zad5
def wektor_nxn(n):
    wektor = []
    for i in range(0, n):
        lista = [random.randint(0, 20) for _ in range(n)]
        wektor.append(lista)
    print(wektor)
    for j in wektor:
        print(j, sum(j))

wektor_nxn(5)