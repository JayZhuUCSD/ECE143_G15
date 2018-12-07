def jl_to_df(fname = 'products_all.jl'):
    '''Convert the raw data in .jl format to a DataFrame'''
    assert '.jl' in fname
    # Make the data into a list of all strings
    with open(fname, 'r', encoding='utf8') as f:
        mylist=[line.rstrip('\n') for line in f]
    data_length=len(mylist)
    data_list=[]

    # Convert the strings to dictionaries
    import json
    for i in mylist:
        d=json.loads(i)
        data_list.append(d)
    list_keys=list(data_list[0].keys())

    # The key_listed_used can vary for different tasks
    # We care about these keys when analyzing this part
    key_list_used=['app_name','title','id','url','all_ratio','genres','specs','platform','developer']
    value_list1=[]
    value_list2=[]
    value_list3=[]
    value_list4=[]
    value_list5=[]
    value_list6=[]
    value_list7=[]
    value_list8=[]
    value_list9=[]

    key1=key_list_used[0]
    key2=key_list_used[1]
    key3=key_list_used[2]
    key4=key_list_used[3]
    key5=key_list_used[4]
    key6=key_list_used[5]
    key7=key_list_used[6]
    key8=key_list_used[7]
    key9=key_list_used[8]

    for i in data_list:
        # features w/o any values return None
        value_list1.append(i.get(key1))
        value_list2.append(i.get(key2))
        value_list3.append(i.get(key3))
        value_list4.append(i.get(key4))
        value_list5.append(i.get(key5))
        value_list6.append(i.get(key6))
        value_list7.append(i.get(key7))
        value_list8.append(i.get(key8))
        value_list9.append(i.get(key9))

    value_list_used=[value_list1,value_list2,value_list3,value_list4,value_list5,value_list6,value_list7,value_list8,value_list9]
    dic_used=dict(zip(key_list_used,value_list_used))

    # Convert to DataFrame
    import pandas as pd
    data1=pd.DataFrame(dic_used)
    return(data1)


def df_preprocessing(data1):
    ''' Extract informations from the developer column'''
    import pandas as pd
    assert isinstance(data1, pd.DataFrame)
    import numpy as np
    import string
    data2 = data1

    developer = []
    publisher = []
    release_date = []

    for index, row in data2.iterrows():
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
                                data2.loc[index,'Developer'] = None
                            if len(nl1) == 0 and len(e1) != 0:
                                data2.loc[index,'Developer'] = e1
                            if len(nl1) != 0 and len(e1) == 0:
                                data2.loc[index,'Developer'] = ' '.join(nl1)
                            if len(nl1) != 0 and len(e1) != 0:
                                data2.loc[index,'Developer'] = ' '.join(nl1)+' '+e1

                            if len(nl2) == 0 and len(e2) == 0:
                                data2.loc[index,'Publisher'] = None
                            if len(nl2) == 0 and len(e2) != 0:
                                data2.loc[index,'Publisher'] = e2
                            if len(nl2) != 0 and len(e2) == 0:
                                data2.loc[index,'Publisher'] = ' '.join(nl2)
                            if len(nl2) != 0 and len(e2) != 0:
                                data2.loc[index,'Publisher'] = ' '.join(nl2)+' '+e2

                            if len(nl3) != 0:
                                data2.loc[index,'Release_Date'] = ' '.join(nl3)
                            if len(nl3) == 0:
                                data2.loc[index,'Release_Date'] = None


            else:
                data2.loc[index,'Developer'] = None
                data2.loc[index,'Publisher'] = None
                data2.loc[index,'Release_Date'] = None
        else:
            data2.loc[index,'Developer'] = None
            data2.loc[index,'Publisher'] = None
            data2.loc[index,'Release_Date'] = None
    return(data2)


def df_processing(data2):
    ''' this file is to generate the Positive_Review_Rank feature
    on the basis of which the new dataframe is created'''
    import pandas as pd
    assert isinstance(data1, pd.DataFrame)
    import numpy as np
    data3 = data2

    # generate the positive_review feauture
    for index, row in data3.iterrows():
        if 'positive' in row['all_ratio']:
            for i in row['all_ratio'].split():
                if i.isdigit():
                    all_review = int(i)
                if '%' in i:
                    for j in i.split('%'):
                        if j.isdigit():
                            all_ratio = int(j)
                if ',' in i:
                    all_review = int(i.replace(',', ''))
            data3.loc[index,'Positive_Review'] = round(all_review*all_ratio/100)
        else:
            data3.loc[index,'Positive_Review'] = None

    #sort out the dataframe according to positive_review_rank
    data3['Positive_Review_Rank'] = data3['Positive_Review'].rank(ascending=0,method='min')
    data3 = data3.sort_values(by = ['Positive_Review_Rank'])
    return(data3)

data1 = jl_to_df(fname = 'products_all.jl')
data2 = df_preprocessing(data1)
data3 = df_processing(data2)
data3.to_csv('dataframe_final.csv')
