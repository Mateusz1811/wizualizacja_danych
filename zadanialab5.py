import numpy as np
"""
a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)
a = np.array(['a', 'b', 'c', 1, 2, 3])
print(a)
print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

print(a.ndim)

m = np.array((np.arange(2), np.arange(2)))
print(m)
print(m.shape)

m = np.array([[2, 1, 3],
              [5, 4, 8]])
print(m)

zera = np.zeros((5, 5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2, 2))
print(pusta)
poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

macierz = np.array([[1,2], [3,4]])
print(macierz)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczzby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczzby_lin)

z = np.indices((5,3))
print(z)
print(z.shape)
print(z[0, 2, 1])

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)

z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'abcdef'
zn1 = np.frombuffer(znaki, dtype='S1')
print(zn1)
zn2 = np.frombuffer(znaki, dtype='S2')
print(zn2)

znaki = 'abcdef'
zn3 = np.array(list(znaki))
zn4 = np.array(list(znaki), dtype='S1')
zn5 = np.array(list(b'abcdef'))
zn6 = np.fromiter(znaki, dtype='S1')
zn7 = np.fromiter(znaki, dtype='U1')
print(zn3)
print(zn4)
print(zn5)
print(zn6)
print(zn7)

mat = np.ones((2, 2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)
mat_1 = np.array([[4, 5], [6, 3]])
print(mat*mat_1)
print(mat/mat_1)

a = np.dot(mat, mat_1)
print(a)
b = mat.dot(mat_1)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[2:5])

mat = np.arange(25)

mat = mat.reshape((5, 5))

print(mat[1:])
print(mat[:,1])
print(mat[:, -1:])
print(mat[2:6, 1:3])
print(mat[:, range(2, 6, 2)])
print('')

x = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

a = np.loadtxt('tekst.txt', dtype=int)
print(a)
print(a.shape)
for i in range(a.shape[0]):
    lista = []
    for j in range(a.shape[1]):
        lista.append(a[j][i])
    print(max(lista))
"""
a = np.arange(3 ,3*16, 3)
print(a)

lista_float = [1.5, 2.7, 3.8, 4.2, 5.1]
tablica_float = np.array(lista_float)
tablica_int64 = tablica_float.astype(np.int64)
print(lista_float)
print(tablica_int64)

def zad3(n):
    tablica = np.arange(1, n*n+1).reshape(n, n)
    return tablica

n = 4
wynik = zad3(n)
print(wynik)

def zad4(podstawa, ilosc_poteg):
    potegi = np.logspace(base=podstawa, start=1, stop=ilosc_poteg, num=ilosc_poteg, dtype='int32')
    return potegi

print(zad4(2, 4))

def zad5(dlugosc):
    wektor = np.arange(dlugosc, 0, -1)
    macierz = np.diag(wektor)
    return macierz

print(zad5(5))

def zad6(macierz):
    n, m = macierz.shape
    print("Slowa w kolumnach: ")
    for j in range(m):
        slowo = ''
        for i in range(n):
            slowo += macierz[i][j]
        print(slowo)
    print("\nSlowa w wierszach: ")
    for i in range(n):
        slowo = ''
        for j in range(m):
            slowo += macierz[i][j]
        print(slowo)
    print("\nSlowo po ukosie:")
    slowo = ''
    for i in range(min(n, m)):
        slowo += macierz[i][i]
    print(slowo)

    print("\nSlowo po ukosie (od prawej do lewej): ")
    slowo = ''
    for i in range(min(n, m)):
        slowo += macierz[i][m - i -1]
    print(slowo)