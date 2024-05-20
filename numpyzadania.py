import pandas as pd
import numpy as np
#zad1
imiona = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(imiona, header=0)
print(df)
#zad2
print(df[df['Liczba'] > 1000])
print(df[df['Imie'] == "MATEUSZ"])
#print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
urodzone_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
suma_urodzen = urodzone_2000_2005['Liczba'].sum()
print(f"Suma dzieci urodzonych w latach 2000-2005 wynosi:{suma_urodzen}")
suma_dzieci = df.agg({'Liczba':'sum'})
print(f"Suma urodzonych dzieci w calym danym okresie wynsosi:{suma_dzieci}")
print(df.groupby(['Plec']).agg({'Liczba':'sum'}))
