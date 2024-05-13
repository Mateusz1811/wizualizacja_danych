import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df1 = pd.ExcelFile('imiona.xlsx')
    imiona = pd.read_excel(df1)
    print(imiona)

    #zad1
    imiona1 = imiona.groupby(['Rok']).agg({'Liczba': ['sum']})
    imiona1.plot(kind='line', title='Liczba urodzonych dzieci')
    plt.show()

    #zad2
    imiona2 = imiona.groupby(['Płeć']).agg({'Liczba': ['sum']})
    imiona2.plot(kind='bar')
    plt.show()


main()