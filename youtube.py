#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:48:07 2018

@author: jayborkar
"""

#   Analysis script
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm

df=pd.read_csv('youtube_results_imm.csv',index_col=0)

print("Correlation of viewcount and likes=",np.corrcoef(df.viewCount,df.likeCount)[0,1])
print("Correlation of viewcount and dislikes=",np.corrcoef(df.viewCount,df.dislikeCount)[0,1])
print("Correlation of viewcount and comments=",np.corrcoef(df.viewCount,df.commentCount)[0,1])
print("Correlation of likes and dislikes=",np.corrcoef(df.likeCount,df.dislikeCount)[0,1])
print("Correlation of likes and comments=",np.corrcoef(df.likeCount,df.commentCount)[0,1])
print("Correlation of dislikes and comments=",np.corrcoef(df.dislikeCount,df.commentCount)[0,1])

#Using viewcount & likes
y = df.likeCount
X= df.viewCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.viewCount.min(), X.viewCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(1)

plt.subplot(211)

plt.scatter(df.viewCount, df.likeCount)

plt.subplot(212)
plt.scatter(X.viewCount, y) 
plt.xlabel("viewCount")
plt.ylabel("Likes")
plt.plot(X_prime[:, 1], y_hat, 'red') 


#Using viewcount & dislikes
y = df.dislikeCount
X= df.viewCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.viewCount.min(), X.viewCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(2)

plt.subplot(211)

plt.scatter(df.viewCount, df.dislikeCount)

plt.subplot(212)
plt.scatter(X.viewCount, y) 
plt.xlabel("viewCount")
plt.ylabel("Dislikes")
plt.plot(X_prime[:, 1], y_hat, 'red') 

#Using viewcount & comments
y = df.commentCount
X= df.viewCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.viewCount.min(), X.viewCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(3)

plt.subplot(211)

plt.scatter(df.viewCount, df.commentCount)

plt.subplot(212)
plt.scatter(X.viewCount, y) 
plt.xlabel("viewCount")
plt.ylabel("commentCount")
plt.plot(X_prime[:, 1], y_hat, 'red') 


#Using likes & dislikes
y = df.dislikeCount
X= df.likeCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.likeCount.min(), X.likeCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(4)

plt.subplot(211)

plt.scatter(df.likeCount, df.dislikeCount)

plt.subplot(212)
plt.scatter(X.likeCount, y) 
plt.xlabel("Likes")
plt.ylabel("Dislikes")
plt.plot(X_prime[:, 1], y_hat, 'red')

#Using like & comments
y = df.commentCount
X= df.likeCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.likeCount.min(), X.likeCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(5)

plt.subplot(211)

plt.scatter( df.likeCount, df.commentCount)

plt.subplot(212)
plt.scatter(X.likeCount, y) 
plt.xlabel("ikeCount")
plt.ylabel("commentCount")
plt.plot(X_prime[:, 1], y_hat, 'red')

#Using dislike & comments
y = df.commentCount
X= df.dislikeCount
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.dislikeCount.min(), X.dislikeCount.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(6)

plt.subplot(211)

plt.scatter( df.dislikeCount, df.commentCount)

plt.subplot(212)
plt.scatter(X.dislikeCount, y) 
plt.xlabel("dislikeCount")
plt.ylabel("commentCount")
plt.plot(X_prime[:, 1], y_hat, 'red')