# this file is to generate the positive_review_rank feature on the basis of which the new dataframe is created
import pandas as pd
import numpy as np
data2 = pd.read_csv('data1.csv', index_col = 0)

# generate the positive_review feauture
positive_review = []
for index, row in data2.iterrows():
    if 'positive' in row['all_ratio']:
        for i in row['all_ratio'].split():
            if i.isdigit():
                all_review = int(i)
            if '%' in i:
                for j in i.split('%'):
                    if j.isdigit():
                        all_ratio = int(j)
        positive_review.append(round(all_review*all_ratio/100))
    else:
        positive_review.append(np.nan)

#sort out the dataframe according to positive_review_rank
data2['positive_review'] = positive_review
data2['positive_review_rank'] = data2['positive_review'].rank(ascending=0,method='min')
data2 = data2.sort_values(by = ['positive_review_rank'])

data2.to_csv('data2.csv')
