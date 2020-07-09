import pandas as pd
import numpy as np
from pydataset import data

#CRIANDO SÉRIES
''' a = pd.Series([1,4,5,7,10,6])
print(a)
print('media = %f' % a.mean())
print('mediana = %f' % a.median())
print(a.duplicated())'''

#DATAFRAME (MATRIZES)
'''
df = pd.DataFrame(
    [['Lucas', 3], ['Gui', 5], ['Doug', 1]], columns = ['repository', 'stars']
)
print(df)
print(df.shape)
print('\n')
print(df['stars'])#Printa a coluna
print(df['stars'].mean())#media
print('\n')
print(df.iloc[1])#Retorna linha específica
print(df.iloc[1]['stars'])#Retorna elemento em específico
'''
#CRIANDO ID
'''df = pd.DataFrame(
    [['Lucas', 3], ['Gui', 5], ['Doug', 1]], columns = ['repository', 'stars']
)
print(df.ix[:1])
print(df.iloc[:1])
df.index = pd.Index([1,2,3])
print('\n')
print(df)'''

#Pydataset (Banco de dados)
#print(data())
print('sucesso')