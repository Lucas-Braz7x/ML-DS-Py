import pandas as pd
import pydataset
import numpy as np
from db import DB

#SERIE TEMPORAL
""" database = DB(filename = 'logs.sqlite3', dbtype = 'sqlite')
log_df = database.tables.log.all()
#print(log_df.head())

#Convertendo a coluna date de string-DATA 
log_df['date'] = pd.to_datetime(log_df['date'], format='%Y-%m-%d %H:%M:%S.%f')
#print(log_df['date'].dtypes)

#Filtros 
log_df.set_index(['date'], inplace=True)
print(log_df['2017-01-03 10:47'])
print(log_df['2017-01-03 10:47' : '2017-01-03 10:51']) """

#PIVOT TABLES

results = pd.read_csv('results.csv')
#print(results['candidate'].unique())

pivot = pd.pivot_table(
    results, index=['state', 'party', 'candidate'], values=['votes'],
    aggfunc={'votes':np.sum}
)
#print(pivot)

results['rank'] = results.groupby(['county', 'party'])['votes'].rank(ascending=False)
results
#print(results[results['county'] == 'Los Angeles'])
results_groupby = results.groupby(['state', 'party', 'candidate']).sum()
del results_groupby['fips']
del results_groupby['fraction_votes']
results_groupby.reset_index(inplace=True)
print('\n')
print(results_groupby.head())




