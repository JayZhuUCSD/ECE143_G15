def match_100_to_1000(fname1 = 'top_100_file.csv', fname2 = 'dataframe_1000.csv'):
    '''match those top played apps in recent 48 hours to the top 1000 reviewed apps'''
    assert '.csv' in fname1
    assert '.csv' in fname2
    import pandas as pd
    import numpy as np

    top = pd.read_csv(fname1, index_col=0)
    for index1, row1 in top.iterrows():
        top.loc[index1, 'Current_Players'] = int(row1['Current Players'].replace(',',''))
    top['Top_Played_Rank'] = top['Current_Players'].rank(ascending=0,method='min')
    top = top.sort_values(by = ['Top_Played_Rank'])
    top_dict = dict(zip(top['Game'], top['Top_Played_Rank']))
    print(top_dict)

    data5 = pd.read_csv(fname2, index_col=0)
    for index2, row2 in data5.iterrows():
        if row2['app_name'] in top_dict.keys():
            data5.loc[index2, 'Top_Played_Rank'] = top_dict[row2['app_name']]
        else:
            data5.loc[index2, 'Top_Played_Rank'] = None

    data5 = data5.sort_values(by = ['Top_Played_Rank'])
    return(data5)

data5 = match_100_to_1000(fname1 = 'top_100_file.csv', fname2 = 'dataframe_1000.csv')
data5.to_csv('match_100_to_1000.csv')
