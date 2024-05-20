import numpy as np
#zad1
a = np.arange(3, 3*15+1, 3)
print(a)

#zad2
lista = [1.5, 2.3, 4.7, 3.6, 6.7]
b = np.array(lista)
print(b)
c = a.astype(dtype='int64')
print(c)
d = np.array(lista, dtype='int32')
print(d)

#zad3
def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = i+1
    tab = a.reshape((n, n))
    return tab

#zad4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

#zad5
def diagonalna(n):
    a = np.arrange(n, 0 ,-1)
    diag = np.diag(a)
    return diag

#zad6
malina = np.array(list('malina'))
armata = np.array(list('armata'))

#zad7
def macierz(n):
    mac = np.zeros((n, n), dtype="int32")
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2*(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2 * (2 * i) for _ in range(n - i)], k=-i)
    print(mac)

#zad8
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        #nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieparzysta liczbe wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]

