#try:
#    a = int(input())
#    b = int(input())
#     result = a / b
#    print(result)
# except ZeroDivisionError:
#     print("Error")

a = [x**2 for x in range(10)]
print(a)
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []
for i in l1:
    l2.append(i**2)
print(l2)
b = [3**y for y in range(6)]
print(b)
c = [x for x in a if x % 2 == 1]
print(c)
d = [(i, j) for i in l1 for j in l2]
print(d)

l3 = []
for i in l1:
    for j in l2:
        l3.append((i,j))
print(l3)

s1 = {1:2, 2:3, 3:4}
s2 = {v: k for k, v in s1.items()}
print(s2)