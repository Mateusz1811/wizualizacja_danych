import numpy as np

#zad1
mac1 = np.array([1, 2, 3])
mac2 = np.array([4, 5, 6])

wynik = np.multiply(mac1, mac2)
print("Wynik mnozenia macierzy to: ", wynik)

#zad2
mac_3x3 = np.random.rand(3, 3)
mac_4x4 = np.random.rand(4, 4)

min_rzad_3x3 = np.min(mac_3x3, axis=1)
min_kol_3x3 = np.min(mac_3x3, axis=0)

min_rzad_4x4 = np.min(mac_4x4, axis=1)
min_kol_4x4 = np.min(mac_4x4, axis=0)

print(f"Najniższe wartosci z macierzy 3x3 to:\n rząd: {min_rzad_3x3}\n kolumna: {min_kol_3x3}\n")
print(f"Najniższe wartosci z macierzy 4x4 to:\n rzad: {min_rzad_4x4}\n kolumna: {min_kol_4x4}\n")

#zad3
mac1 = np.array([1, 2, 3])
mac2 = np.array([4, 5, 6])

wynik = np.dot(mac1, mac2)
print(f"Iloczyn macierzy: {wynik}")

#zad4
mac_calkowita = np.array([1, 2 ,3], dtype=int)
mac_rzeczywista = np.array([1.5, 2.5, 3.5])

wynik = np.multiply(mac_calkowita, mac_rzeczywista)
print(f"Wynik mnożenia: {wynik}")

#zad5
macierz = np.array([[1, 2, 3],
                    [4, 5, 6]])

a = np.sin(macierz)
print(f"Sinus dla kazdej wartosci w macierzy: {a}")

#zad6
macierz = np.array([[1, 2, 3],
                    [4, 5, 6]])

b = np.cos(macierz)
print(f"Cosinus dla kazdej wartosci w macierzy: {b}")

#zad7
wynik = a + b
print(f"Wynik sumowania macierzy: {wynik}")




