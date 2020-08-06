# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:54:03 2019

@author: LENOVO
"""

# startup funding case study question 2
'''Even after trying for so many times,
 your friend’s startup could not find the investment.
 So you decided to take this matter in your hand and try to
 find the list of investors who probably can invest in your friend’s startup. 
 Your list will increase the chance of your friend startup getting some initial
 investment by contacting these investors. Find the top 5 investors who have invested 
 maximum number of times (consider repeat investments in one company also). 
 In a startup, multiple investors might have invested.
 So consider each investor for that startup. Ignore undisclosed investors.'''





import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
df=pd.read_csv(r'startup_funding.csv')
df.InvestorsName.fillna('',inplace=True)
a=df.InvestorsName.str.split(',')
a.fillna('nin',inplace=True)
d={}
for i in a:
    for j in i:
        d[j.strip()]=d.get(j.strip(),0)+1
sr=pd.Series(d)
sr['nin']=0
sr.sort_values(ascending=False,inplace=True)
for i in sr.index[:6]:
    print(i,sr[i])


