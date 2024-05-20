import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#print(ts)
#ts.plot()
#plt.show()

#data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        #'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        #'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        #'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#df = pd.DataFrame(data)
#print(df)
#grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
#print(grupa)
#grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld',
          # legend=True, title='Populacja z podzialem na kontynenty')
#wykres = grupa.plot.bar()
#wykres.set_ylabel('Kontynent')
#wykres.tick_params(axis='x', labelrotation=0)
#wykres.legend()
#wykres.set_title('Populacja z podzialem na kontynenty')
#plt.xticks(rotation=0)
#plt.savefig('wykres.png')
#plt.show()

#df = pd.read_csv('dane.csv', header=0, sep=";",
              #   decimal=".")
#print(df)
#grupa = (df.groupby(['Imię i nazwisko']).
        # agg({'Wartość zamówienia':["sum"]}))
#grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
          # fontsize=20, figsize=(6,6),colors=['red', 'green'])
#wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%',
                        #fontsize=20, figsize=(6,6))

#plt.legend(loc="lower right")
#plt.title('Suma zamówienia dla sprzedawcy')
#plt.show

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

df = pd.DataFrame(ts, columns=['wartości'])
print(df)

df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()