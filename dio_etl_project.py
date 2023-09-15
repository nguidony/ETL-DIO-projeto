#Importar bibliotecas
import pandas as pd

#Importar dados - importar o csv contendo filmes assistidos
df = pd.read_csv(r"D:\dio curso\projeto\movies.watched.csv")
print(df)

#Transformar -selecionar apenas filmes dos anos 2000 até 2023
filmes2020 = df[df['Year'] >= 2020]
print(filmes2020)

#load
filmes2020.to_csv(r"D:\dio curso\projeto\filmes2020.csv", index= 'false')
