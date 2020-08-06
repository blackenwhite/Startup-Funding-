# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:00:10 2019

@author: LENOVO
"""
'''After re-analysing the dataset you found out that some investors have invested
 in the same startup at different number of funding rounds. So before finalising 
 the previous list, you want to improvise it by finding the top 5 investors who have
 invested in different number of startups. This list will be more helpful than your 
 previous list in finding the investment for your friend startup. Find the top 5 
 investors who have invested maximum number of times in different companies. 
 That means, if one investor has invested multiple times in one startup, count one for 
 that company. There are many errors in startup names.
 Ignore correcting all, just handle the important ones - Ola, Flipkart, Oyo and Paytm.'''
 
 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv("startup_funding.csv")
df['Date'].replace('12/05.2015','12/05/2015',inplace = True)
df['Date'].replace('13/04.2015','13/04/2015',inplace = True)
df['Date'].replace('15/01.2015','15/01/2015',inplace = True)
df['Date'].replace('22/01//2015','22/01/2015',inplace = True)

df['CityLocation'].dropna(inplace=True)
df['StartupName'].dropna(inplace=True)

# taking care of  the names of the big startups
df['StartupName'].replace('Olacabs','Ola',inplace=True)
df['StartupName'].replace('Ola Cabs','Ola',inplace=True)
df['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)
df['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)
df['StartupName'].replace('Oyo Rooms','Oyo',inplace=True)
df['StartupName'].replace('Oyorooms','Oyo',inplace=True)
df['StartupName'].replace('OyoRooms','Oyo',inplace=True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)

df.InvestorsName.fillna('',inplace=True)
companies={}
for i in range(len(df)):
    com=df['StartupName'][i]
    if com not in companies:
        investors=[]
        lst=list(df['InvestorsName'][i].strip().split(','))
        for i in lst:
            i=i.strip()
            investors.append(i)
        companies[com]=investors
    else:
        lst=list(df['InvestorsName'][i].strip().split(','))
        for i in lst:
            i=i.strip()
            investors.append(i)
        companies[com]+=investors
        
dic={}
for i in companies:
    for j in companies[i]:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1

dic=pd.Series(dic)
dic['nin']=0
dic.sort_values(ascending=False,inplace=True)

for i in dic.index[:6]:
    print(i,dic[i])
    




