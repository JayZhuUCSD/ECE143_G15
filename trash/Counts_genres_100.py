#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All_ratio_vs_genres for the most popualar 100

@author: Zi He (Hertz) GitID:Terahezi
"""

def convertJLtoDataFrame(fname='products_all.jl', key_list_used=['app_name','genres']):
    '''
    Convert the raw data in .jl format to a DataFrame
    
    :fname: str name of a .jl file with data (defaults to 'products_all.jl' which is our data)
    
    :key_list_used: a list of strings that are the name of features in the data 
    (Defaults to just three features 'all_ratio, platform, genres' as a demo for our analysis)
    '''
    
    assert isinstance(fname, str) and '.jl' in fname  
        
    assert isinstance(key_list_used, list)

        
    # Make the data into a list of all strings
    with open(fname,'r',encoding='utf8') as f:
        mylist = [line.rstrip('\n') for line in f]

    data_length = len(mylist)
    data_list = []

    # Convert the strings to dictionaries
    for i in mylist:
        d=json.loads(i)
        data_list.append(d)
        
    list_keys = list(data_list[0].keys())

    value_list_used = []
    key_list = []
    
    for i in key_list_used:
        key_list.append(i)
        value_list_used.append([])

    for i in data_list:
        # features w/o any values return None
        index = 0
        for key in key_list:
            value_list_used[index].append(i.get(key))
            index += 1

    # value_list_used = [value_list1,value_list2,value_list3]
    dic_used = dict(zip(key_list_used,value_list_used))

    # Convert to DataFrame
    df_used = pd.DataFrame(dic_used)
    
    # Return dataframe of the data from the .jl file
    return df_used

def generate_counts_genres_100():
    df_all_apps=convertJLtoDataFrame(fname='products_all.jl', key_list_used=['app_name','genres'])
    df_most_100=pd.read_csv('top_100_file.csv')
    list_genres_most_100=[]
    list_app_name=[]
    for i in df_most_100.Game:
        if i in list(df_all_apps.app_name):
            if df_all_apps.genres[list(df_all_apps.app_name).index(i)]!=None:
                list_genres_most_100.append(df_all_apps.genres[list(df_all_apps.app_name).index(i)])
                list_app_name.append(i)
    dic_used={'app_name':list_app_name,'genre':list_genres_most_100}
    df_genres_100_most=pd.DataFrame.from_dict(dic_used)
    df_genres_100_most.genre
    list_all_genres_100=[]

    for i in df_genres_100_most.genre:
    
    
        if type(i)==list:
            for j in i:
                print(j)
                list_all_genres_100.append(j)
        else:
            list_all_genres_100.append(None)

    from collections import Counter
    d = Counter(list_all_genres_100)
    
    list_word=[]
    list_count=[]
    
    for word, count in d.most_common(10):
        
        list_word.append(word)
        list_count.append(count)
    
    dic_wordcount={'word':list_word,'count':list_count}
    df_wordcount=pd.DataFrame.from_dict(dic_wordcount)
    return df_wordcount