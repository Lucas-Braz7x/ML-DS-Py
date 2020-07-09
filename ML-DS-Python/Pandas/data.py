import pandas as pd
import pydataset
import numpy as np
from db import DB

#Acessando o dataset
'''titanic = pydataset.data('titanic')
print(titanic.head())#Pega os elementos
print(titanic.tail())#Pega os ultimos elementos
print(titanic.describe())#Descreve a dataset
print(titanic['class'].value_counts())'''

#CARREGANDO BANCO DE DADOS
'''database = DB(filename='logs.sqlite3', dbtype='sqlite')

#print(database.tables)

#log_df = database.tables.log#não é um dataframe
log_df = database.tables.log.all()#Agora é 
#log_df = database.query('select * from log where user_id = 3')
#Pega parte da tabela

print(log_df)'''

#CARREGANDO PLANILHAS
'''
#help(pd.read_csv)
copacabana = pd.read_csv('copacabana.csv', delimiter=';')
print(copacabana['Quartos'].describe())

populacao = pd.read_excel('total-populacao-pernambuco.xls')
print(populacao.head())
print('\n')
print(copacabana.loc[copacabana['Quartos'] == 6])
print('\n')
print(copacabana['Quartos']>5)
print('\n')
#Criando novas colunas
copacabana['TOTAL'] =copacabana['AreaConstruida'] * copacabana['VAL_UNIT'] 
print(copacabana['TOTAL'].describe())'''

#DADOS CATEGORICOS
'''
titanic = pydataset.data('titanic')
#print(titanic.columns)
print('\n')
#print(titanic['class'].describe())
print(titanic['class'].nbytes)#Exibe o espaço ocupado

titanic['class'] == titanic['class'].astype('category')
#print(titanic['class'].describe())
print('\n')
print(titanic['class'].nbytes)
'''
