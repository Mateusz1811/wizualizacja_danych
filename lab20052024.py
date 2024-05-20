import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

#bardzo prosty wykres liniowy
plt.plot([1, 2, 3, 4])
plt.ylabel('jakies liczby')
plt.show()
"""
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
plt.axis([0, 6, 0, 20])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')

plt.axis([0, 6, 0, 20])
plt.show()


t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()



x = np.linspace(0, 2, 100)
plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label='kwadratowa')
plt.plot(x, x**3, label='szescienna')

plt.xlabel('etykieta x')
plt.ylabel('etykieta y')

plt.title("prosty wykres")
plt.legend()
plt.savefig('wykres matplot.png')

plt.show()
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')


#zadania
#zad1
x = np.linspace(1, 20 ,400)
y = 1 / x

plt.plot(x, y, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(1, 20)
plt.ylim(0, 1)
plt.legend()
plt.show()

#zad2
x = np.linspace(1, 20 ,400)
y = 1 / x

plt.plot(x, y, label='f(x) = 1/x', color='green', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(1, 20)
plt.ylim(0, 1)
plt.legend()
plt.show()

#zad3
x = np.arange(0, 30, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x ,y_sin, label='sin(x)', color='blue')
plt.plot(x ,y_cos, label='cos(x)', color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykresy funkcji sin(x) oraz cos(x)")
plt.legend()
plt.grid(True)
plt.show()

#zad5
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
nazwy_kolumn = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=nazwy_kolumn)

df["diff"] = np.abs(df["sepal_length"] - df["sepal_width"])

plt.figure(figsize=(8, 6))
plt.scatter(df["sepal_length"], df["sepal_width"], c=df["diff"], cmap="viridis", s=50)
plt.colorbar(label="|sepal_length - sepal_width|")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Wykres punktowy sepal_length i sepal_width")
plt.grid(True)
plt.show()

#zad5

df = pd.ExcelFile("imiona.xlsx")
imiona = pd.read_excel(df)
plt.subplot(1,3,1)
wykres1 = imiona.groupby(['Plec']).agg({'Liczba':['sum']})
etykiety = ['K', 'M']
wartosci = list(wykres1.agg('Liczba').sum())
plt.bar(x=etykiety, height=wartosci, color=['red', 'blue'])
plt.xlabel('Plec')
plt.ylabel('Liczba')
plt.show()
plt.subplot(1,3,2)
wykres2_m=imiona[imiona['Plec']=='M'].groupby(['Rok']).agg({'Liczba': ['sum']})
wykres2_k=imiona[imiona['Plec']=='K'].groupby(['Rok']).agg({'Liczba': ['sum']})
plt.plot(wykres2_m.index.values, wykres2_m['Liczba'], 'b-', label='mezczyzni')
plt.plot(wykres2_k.index.values, wykres2_k['Liczba'], 'r-', label='kobiety')
plt.subplots_adjust(wspace=0.6)
plt.show()
###nie wiem czemu nie dziala xd
#plt.subplot(1,3,3)
#wykres3 = imiona.groupby(['Rok']).agg({'Liczba': ['sum']})
#etykiety3 = wykres3.index.values
#wartosci3 = list(wykres3['Liczba'])
#plt.bar(x=etykiety3, height=wartosci3, color='green')
#plt.xlabel('Rok')
#plt.show()
###

df = pd.read_excel("imiona.xlsx")

suma_na_rok = df.groupby("Rok")["Liczba"].sum()

plt.figure(figsize=(10, 6))
plt.bar(suma_na_rok.index, suma_na_rok.values)
plt.xlabel("Rok urodzenia")
plt.ylabel("Suma urodzeń")
plt.title("Suma urodzeń dzieci w poszczególnych latach")
plt.grid(axis="y")
plt.show()