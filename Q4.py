# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:17:02 2019

@author: LENOVO
"""
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
    if data=="Crowd Funding" or data=="Seed Funding":
        return data
    else:
        return "Other_fundings"

df["my_fundings"]=df["InvestmentType"].apply(foo)
df1=df[df["my_fundings"]!="Other_fundings"]




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