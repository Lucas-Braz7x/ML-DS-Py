import pandas as pd
import pydataset
import numpy as np
#from db import DB
from db import DemoDB

#TRABALHANDO COM DADOS INCOMPLETOS
'''dados = {
    'nome': ['João', 'Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
    'sexo': ['M', 'F', 'M', np.nan, 'M', 'M', np.nan],
    'idade': [14, 13, np.nan, np.nan, 15, 13, 14],
    'nota': [4, 10, 7, np.nan, 8, 9, 7]
}
df = pd.DataFrame(dados)
print(df)
print('\n')
print(df.dropna())#Elimina a linha que não tem nenhum dado
print('\n')
print(df.dropna(thresh=3))#Elimina as linhas que tem até 3 NAN
print('\n')
df['series'] = np.nan #Cria uma nova coluna
print(df.dropna(how='all')) #Elimina todas as linhas que tenham algum NAN
print('\n')
print(df.dropna(how='all', axis=1)) #Elimina a coluna que tenha todos dados NAN
print('\n')
df['series'].fillna(8, inplace=True)
print(df)
df['series'] = np.nan
'''

""" df = pd.read_csv('results.csv')

#print(df.head())
print('\n')
print(df.groupby('candidate').aggregate({'votes':[min, np.mean, max]}))
print('\n')
#print(df[df['votes'] == 590502])
#A linha superior é igua df.loc[df['votes'] == 590502]
#print(df.groupby('candidate').aggregate({'fraction_votes':[min, np.mean, max]}))
print('\n')
#print(df[(df['fraction_votes'] == 1) & (df['candidate'] == 'Hillary Clinton')])
def fraction_votes_filter(x):
    return x['votes'].sum()>10000000

print(df.groupby('state').filter(fraction_votes_filter))
print('\n')

print(df[df['state_abbreviation'] == 'AL']['votes'].sum())
print('\n')
print(df.groupby(['state_abbreviation', 'candidate'])['votes'].sum()) """

#OPERAÇÕES NO BD

database = DemoDB()

album = database.tables.Album.all()
#print(album)
artist = database.tables.Artist.all()
print('\n')
#print(artist)

album_artist = pd.merge(artist, album, on='ArtistId')
print('\n')
#print(album_artist.head())

album.rename(columns={'ArtistId':'Artist_Id'}, inplace=True)
artist_album = pd.merge(album, artist, left_on='Artist_Id',right_on = 'ArtistId').drop('Artist_Id', axis=1)
#print(artist_album.head())

aluno1 = pd.DataFrame(
    {
        'nome':['Maria', 'Sofia'],
        'nota':[8, 9],
    }
)
aluno2 = pd.DataFrame(
    {
        'nome':['João', 'Pedro', 'Maria'],
        'cod':[1, 2, 3],
    }
)

alunos = pd.merge(aluno1, aluno2, how='outer')
print(alunos)

