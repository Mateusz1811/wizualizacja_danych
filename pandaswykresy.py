import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('imiona.xlsx')

urodzenia_na_rok = df.groupby("Rok")["Liczba"].sum()
plt.figure(figsize=(10, 6))
plt.plot(urodzenia_na_rok.index, urodzenia_na_rok.values, marker='o', linestyle='-', color="b")
plt.xlabel("Rok urodzenia")
plt.ylabel("Liczba urodzen")
plt.title("Liczba urodzeń dzieci w poszczególnych latach")
plt.grid(True)
plt.show()


plec = df.groupby("Rok")["Liczba"].sum()
plt.figure(figsize=(8, 6))
plt.bar(plec.index, plec.values)
plt.xlabel("Plec")
plt.ylabel("Liczba urodzen")
plt.title("Liczba urodzen chlopcow i dziewczynek")
plt.grid(axis="y")
plt.show()

urodzenia_plec = df.groupby("Rok")["Liczba"].sum()

plt.figure(figsize=(8, 6))
plt.pie(urodzenia_plec, labels=urodzenia_plec.index, autopct="%1.1f%%", colors=["skyblue", "lightcoral"])
plt.title("Procent urodzeń chłopców i dziewczynek")
plt.show()

df4 = pd.read_csv("zamowienia.csv", delimiter=";")

zamowienia = df4.groupby("Sprzedawca")["idZamowienia"].count()
plt.figure(figsize=(10, 6))
plt.bar(zamowienia.index, zamowienia.values)
plt.xlabel("Sprzedawca")
plt.ylabel("Ilość zamówień")
plt.title("Ilość złożonych zamówień przez poszczególnych sprzedawców")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.show()

