#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:17:57 2018

@author: jayborkar
"""
# Data collection
import os
os.system("python tw_search.py plympics -c 100")
os.system("wc -l result.csv > lines.txt")




#   Analysis script
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm

df=pd.read_csv('./Twitter_Search/result.csv',index_col=0)

print(np.corrcoef(df.followers,df.friends)[0,1])
print(np.corrcoef(df.followers,df.retwc)[0,1])
print(np.corrcoef(df.friends,df.retwc)[0,1])


plt.scatter(np.log(df.followers), np.log(df.friends))

X=df.followers
y=df.friends
X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()

print(lr_model.summary())