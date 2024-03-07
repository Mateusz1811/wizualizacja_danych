#try:
#    a = int(input())
#    b = int(input())
#     result = a / b
#    print(result)
# except ZeroDivisionError:
#     print("Error")
# import math
#
# a = [x**2 for x in range(10)]
# print(a)
# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# b = [3**y for y in range(6)]
# print(b)
# c = [x for x in a if x % 2 == 1]
# print(c)
# d = [(i, j) for i in l1 for j in l2]
# print(d)
#
# l3 = []
# for i in l1:
#     for j in l2:
#         l3.append((i,j))
# print(l3)
#
# s1 = {1:2, 2:3, 3:4}
# s2 = {v: k for k, v in s1.items()}
# print(s2)

# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 -4*a*c
#     if delta < 0:
#         print("brak pierwiastka")
#         return 0
#     elif delta == 0:
#         print("Jeden pierwiastek")
#         x = -b/2*a
#         return x
#     elif delta > 0:
#         print("dwa rozwiazania")
#         x1 = (-b - math.sqrt(delta))/(2*a))
#         x2 = (-b + math.sqrt(delta))/(2*a))
#         return x1, x2
# print(rownanie_kwadratowe(6,1,3))
# print(rownanie_kwadratowe(1,2,1))
# print(rownanie_kwadratowe(1,4,1))\

# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x2-x1))**2 + (y2-y1)**2
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2,4,5,7))
# print(dlugosc_odcinka(1,2,3,4))
# print(dlugosc_odcinka(2,3,7,8))

# plik = open('tekst,txt', 'r', encoding='utf-8')
# znaki = plik.read(10)
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
#
# print(znaki)
# print(linia)
# print(linie)

# plik = open('tekst.txt', 'a+', encoding='utf-8')
# plik.seek(0)
# znaki = plik.read(10)
# plik.write('siema')
# plik.close()
# print(znaki)

with open('tekst.txt', 'r') as plik:
    znaki = plik.readlines()

print(znaki)