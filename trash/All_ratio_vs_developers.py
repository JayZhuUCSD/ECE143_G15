#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All_ratio vs developer

@author: Zi He (Hertz) GitID:Terahezi
"""
def convertJLtoDataFrame(fname='products_all.jl', key_list_used=['all_ratio','developer','genres']):
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

def parseRatioAndReviews(df):
    '''
    return a DataFrame with gaming apps which have an all_ratio
    '''
    

    df_with_all_ratio=df[df.all_ratio.str.contains('positive')]
    
    assert isinstance(df_with_all_ratio, pd.DataFrame)

    return df_with_all_ratio

def parseRatio_NreviewsAndDeveloper(df_with_all_ratio,fname='df_wordcount_100_most.csv'):
    '''return a DataFrame containing all_ratio 
    and developer only for the top 10'''
    
    assert isinstance(df_with_all_ratio, pd.DataFrame)
    
    list_all_ratio=[]
    list_N_reviews=[]
    
    for i in df_with_all_ratio.all_ratio:
        list_all_ratio.append(i.split()[0])
        list_N_reviews.append(i.split()[3])
    
    list_all_Developer=[]
    
    for i in df_with_all_ratio.developer:
        if type(i)==str:
            index1=i.find('Publisher')
            index2=i.find('Release')
            if index1!=-1:
                list_all_Developer.append(i[:index1])
                
            elif index2!=-1:
                list_all_Developer.append(i[:index2])
        else:
            list_all_Developer.append(None)
            
    dic_all_ratio_developer={'all_ratio':list_all_ratio,'developer':list_all_Developer}
    dic_Nreviews_developer={'#Reviews':list_N_reviews,'developer':list_all_Developer}
    df_all_ratio_developer=pd.DataFrame(dic_all_ratio_developer)
    df_Nreviews_developer=pd.DataFrame(dic_Nreviews_developer)
    return df_all_ratio_developer

import pandas as pd
import json
from IPython.display import display, HTML
from collections import Counter

def main():
    df_used = convertJLtoDataFrame()
    
    # Assert that a pandas DataFrame was returned
    assert isinstance(df_used, pd.DataFrame)
    
    print('DataFrame of data parsed from products_all.csv')
    df_used.to_csv('products_developer_counts.csv')
    display(df_used)
    
    df_with_all_ratio= parseRatioAndReviews(df_used)
    
    df_all_ratio_developer= parseRatio_NreviewsAndDeveloper(df_with_all_ratio)
    df_all_ratio_developer.to_csv('df_all_ratio_vs_developer.csv')
    
    display(df_all_ratio_developer)
