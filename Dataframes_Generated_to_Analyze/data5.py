# this file is to extract the information from the developer column
import pandas as pd
import numpy as np
import string
data5 = pd.read_csv('data2.csv', index_col=0)

developer = []
publisher = []
release_date = []

for index, row in data5.iterrows():
    if isinstance(row['developer'], str):
        if 'Publisher' in row['developer']:
            translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
            s = row['developer'].translate(translator)
            l = s.split()
            for i1 in range(len(l)):
                for i2 in range(len(l)):

                    if 'Publisher' in l[i1] and 'Release' in l[i2]:
                        e1 = l[i1].replace('Publisher','')
                        nl1 = l[0:i1]
                        e2 = l[i2].replace('Release','')
                        nl2 = l[i1+1:i2]
                        nl3 = l[i2+2:]

                        if len(nl1) == 0 and len(e1) == 0:
                            data5.loc[index,'Developer'] = None
                        if len(nl1) == 0 and len(e1) != 0:
                            data5.loc[index,'Developer'] = e1
                        if len(nl1) != 0 and len(e1) == 0:
                            data5.loc[index,'Developer'] = ' '.join(nl1)
                        if len(nl1) != 0 and len(e1) != 0:
                            data5.loc[index,'Developer'] = ' '.join(nl1)+' '+e1

                        if len(nl2) == 0 and len(e2) == 0:
                            data5.loc[index,'Publisher'] = None
                        if len(nl2) == 0 and len(e2) != 0:
                            data5.loc[index,'Publisher'] = e2
                        if len(nl2) != 0 and len(e2) == 0:
                            data5.loc[index,'Publisher'] = ' '.join(nl2)
                        if len(nl2) != 0 and len(e2) != 0:
                            data5.loc[index,'Publisher'] = ' '.join(nl2)+' '+e2

                        if len(nl3) != 0:
                            data5.loc[index,'Release_Date'] = ' '.join(nl3)
                        if len(nl3) == 0:
                            data5.loc[index,'Release_Date'] = None


        else:
            data5.loc[index,'Developer'] = None
            data5.loc[index,'Publisher'] = None
            data5.loc[index,'Release_Date'] = None
    else:
        data5.loc[index,'Developer'] = None
        data5.loc[index,'Publisher'] = None
        data5.loc[index,'Release_Date'] = None

data5.to_csv('data5.csv')
