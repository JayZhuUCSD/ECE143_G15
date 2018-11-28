def final_to_1000(fname = 'dataframe_final.csv'):
    '''Convert the whole dataframe to the one containing the top1000'''
    assert '.csv' in fname

    import pandas as pd
    import numpy as np

    data4 = pd.read_csv('dataframe_final.csv', index_col=0)
    data4['Positive_Review_Rank'] = data4['Positive_Review_Rank'].fillna(16711).astype(int)
    data4 = data4.loc[data4['Positive_Review_Rank'].isin(range(1,1001))]

    data4.to_csv('dataframe_1000.csv')

final_to_1000(fname = 'dataframe_final.csv')
