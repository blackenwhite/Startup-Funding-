# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:01:12 2019

@author: LENOVO
"""

'''Due to your immense help, your friend startup successfully got seed funding
 and it is on the operational mode. Now your friend wants to expand his startup and
 he is looking for new investors for his startup. Now you again come as a saviour 
 to help your friend and want to create a list of probable new new investors.
 Before moving forward you remember your investor friend advice that finding
 the investors by analysing the investment type. Since your friend startup is
 not in early phase it is in growth stage so the best-suited investment type is
 Private Equity. Find the top 5 investors who have invested in a different number
 of startups and their investment type is Private Equity. Correct spelling of 
 investment types are - "Private Equity", "Seed Funding", "Debt Funding", and 
 "Crowd Funding". Keep an eye for any spelling mistake. You can find this by
 printing unique values from this column.There are many errors in startup names. 
 Ignore correcting all, just handle the important ones 
- Ola, Flipkart, Oyo and Paytm.'''


import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt


df=pd.read_csv("startup_funding.csv")
df.InvestorsName.fillna('',inplace=True)

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

df['InvestmentType'].dropna(inplace=True)
df['InvestmentType'].replace("SeedFunding","Seed Funding",inplace=True)
df['InvestmentType'].replace("Crowd funding","Crowd Funding",inplace=True)
df['InvestmentType'].replace("PrivateEquity","Private Equity",inplace=True)

def foo(data):
    if data=="Private Equity":
        return data
    else:
        return "Other_fundings"
    
df["my_fundings"]=df["InvestmentType"].apply(foo)

df1=df[df["my_fundings"]=="Private Equity"]

a=df1.InvestorsName.str.split(',')
a.fillna('nin',inplace=True)
d={}
for i in a:
    for j in i:
        d[j.strip()]=d.get(j.strip(),0)+1
sr=pd.Series(d)
sr['nin']=0
sr.sort_values(ascending=False,inplace=True)
for i in sr.index[:8]:
    print(i,sr[i])




