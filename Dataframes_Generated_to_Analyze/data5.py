# this file is to extract the information from the developer column
import pandas as pd
import numpy as np
import string
data4 = pd.read_csv('data2.csv', index_col=0)

developer = []
publisher = []
release_date = []

for index, row in data4.iterrows():
    if isinstance(row['developer'], str):
        if 'Publisher' in row['developer']:
            translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
            s = row['developer'].translate(translator)
            l = s.split()
            for i1 in range(len(l)):
                if 'Publisher' in l[i1]:
                    e1 = l[i1].replace('Publisher','')
                    nl1 = l[0:i1]
                    if len(nl1) == 0 and len(e1) == 0:
                        developer.append(None)
                    if len(nl1) == 0 and len(e1) != 0:
                        developer.append(e1)
                    if len(nl1) != 0 and len(e1) == 0:
                        developer.append(' '.join(nl1))
                    if len(nl1) != 0 and len(e1) != 0:
                        developer.append(' '.join(nl1)+' '+e1)
        else:
            developer.append(None)
            publisher.append(None)
            release_date.append(np.nan)
    else:
        developer.append(None)
        publisher.append(None)
        release_date.append(np.nan)

#sort out the dataframe according to positive_review_rank
data4['developer'] = pd.Series(developer)
data4['publisher'] = pd.Series(publisher)

data4.to_csv('data5.csv')
