#this file is to match the top_100_played_apps to the dataframe we sort out according to the numbers of positive reviews
import pandas as pd
import numpy as np

top = pd.read_csv('top_100_file.csv', index_col=0)
for index1, row1 in top.iterrows():
    top.loc[index1, 'current_players'] = int(row1['Current Players'].replace(',',''))
top['top_played_rank'] = top['current_players'].rank(ascending=0,method='min')
top = top.sort_values(by = ['top_played_rank'])
top_dict = dict(zip(top['Game'], top['top_played_rank']))
print(top_dict)

data3 = pd.read_csv('data2.csv', index_col=0)
for index, row in data3.iterrows():
    if row['title'] in top_dict.keys():
        data3.loc[index, 'top_played_rank'] = top_dict[row['title']]
    else:
        data3.loc[index, 'top_played_rank'] = np.nan

data3 = data3.sort_values(by = ['top_played_rank'])

data3.to_csv('data3.csv')
