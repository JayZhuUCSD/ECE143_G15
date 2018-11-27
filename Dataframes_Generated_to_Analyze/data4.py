import pandas as pd
import numpy as np

data4 = pd.read_csv('data2.csv', index_col=0)
data4['positive_review_rank'] = data4['positive_review_rank'].fillna(0).astype(int)
data4 = data4.loc[data4['positive_review_rank'].isin(range(1,1000))]

data4.to_csv('data4.csv')
