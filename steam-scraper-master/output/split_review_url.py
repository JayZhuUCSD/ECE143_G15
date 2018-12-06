# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:14:02 2018
Extrac all the reviews' urls from raw data file and 
@author: Fangzhou Ai
"""
true=1
false=0
fname='products_all.jl'
f=open(fname,'r',encoding="utf8")


g1=open('re_url1','w')
g2=open('re_url2','w')
g3=open('re_url3','w')
g4=open('re_url4','w')
g5=open('re_url5','w')
g6=open('re_url6','w')
g7=open('re_url7','w')
g8=open('re_url8','w')
g9=open('re_url9','w')
g0=open('re_url0','w')
i=0
for line in f:
    exec('temp=%s'%line)
    try:
       assert int(str(temp['all_view']).replace(',',''))>0 #check if it has comments
    except AssertionError:
       continue
    try:
       assert temp['reviews_url'] #extract url
    except KeyError:
        continue
    a=temp['reviews_url']+'\n'
    exec('g%d.write(a)'%i)

    i=i+1
    i=i%10     

f.close()
g0.close()
g1.close()
g2.close()
g3.close()
g4.close()
g5.close()
g6.close()
g6.close()
g7.close()
g8.close()
g9.close()

print('done')
