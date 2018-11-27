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
# We care about these keys when analyzing this part
key_list_used=['title','all_ratio','genres','specs','platform','developer']
value_list1=[]
value_list2=[]
value_list3=[]
value_list4=[]
value_list5=[]
value_list6=[]

key1=key_list_used[0]
key2=key_list_used[1]
key3=key_list_used[2]
key4=key_list_used[3]
key5=key_list_used[4]
key6=key_list_used[5]

for i in data_list:
    # features w/o any values return None
    value_list1.append(i.get(key1))
    value_list2.append(i.get(key2))
    value_list3.append(i.get(key3))
    value_list4.append(i.get(key4))
    value_list5.append(i.get(key5))
    value_list6.append(i.get(key6))

value_list_used=[value_list1,value_list2,value_list3,value_list4,value_list5,value_list6]
dic_used=dict(zip(key_list_used,value_list_used))

# Convert to DataFrame
import pandas as pd
data1=pd.DataFrame(dic_used)
data1.to_csv('data1.csv')
