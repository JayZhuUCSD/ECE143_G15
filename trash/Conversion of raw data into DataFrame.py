#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:55:54 2018

@author: hezi
"""

'''Convert the raw data in .jl format to a DataFrame'''
# Make the data into a list of all strings
with open('products_all.jl','r',encoding='utf8') as f:
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
# here just use three features as a demo
key_list_used=['all_ratio','platform','genres']
value_list1=[]
value_list2=[]
value_list3=[]
key1=key_list_used[0]
key2=key_list_used[1]
key3=key_list_used[2]
for i in data_list:
    # features w/o any values return None
    value_list1.append(i.get(key1))
    value_list2.append(i.get(key2))
    value_list3.append(i.get(key3))
value_list_used=[value_list1,value_list2,value_list3]
dic_used=dict(zip(key_list_used,value_list_used))

# Convert to DataFrame
import pandas as pd
df_used=pd.DataFrame(dic_used)