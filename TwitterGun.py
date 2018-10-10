#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:05:13 2018

@author: jayborkar
"""
#   Analysis script
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm

df=pd.read_csv('results_gunS.csv',index_col=0)
#df1=df[df.followers < 16000000]
#df2=df[df.friends < 250000]

print("Correlation of Followers and Friends=",np.corrcoef(df.followers,df.friends)[0,1])
print("Correlation of Followers and Polarity=",np.corrcoef(df.followers,df.polarity)[0,1])
print("Correlation of Followers and subjectivity=",np.corrcoef(df.followers,df.subjectivity)[0,1])
print("Correlation of Friends and Polarity=",np.corrcoef(df.friends,df.polarity)[0,1])
print("Correlation of Friends and subjectivity=",np.corrcoef(df.friends,df.subjectivity)[0,1])
print("Correlation of Friends and retweets=",np.corrcoef(df.friends,df.retwc)[0,1])
print("Correlation of Followers and retweets=",np.corrcoef(df.followers,df.retwc)[0,1])

#df=df[df.followers < 3500000]
#df=df[df.friends < 250000]

#Using followers & retweets

X=df.followers
y=df.retwc

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.followers.min(), X.followers.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(1)

plt.subplot(211)

plt.scatter( df1.followers,df1.retwc)

plt.subplot(212)
plt.scatter(X.followers, y) # Plot the raw data plt.xlabel("Friends")
plt.ylabel("retwc")
plt.xlabel("Followers")
plt.plot(X_prime[:, 1], y_hat, 'red') # Add the regression line, colored in red


#Using followers & subjectivity

X=df.followers
y=df.subjectivity

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.followers.min(), X.followers.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(2)

plt.subplot(211)

plt.scatter( df.followers,df.subjectivity)

plt.subplot(212)
plt.scatter(X.followers, y) # Plot the raw data plt.xlabel("Friends")
plt.ylabel("subjectivity")
plt.xlabel("Followers")
plt.plot(X_prime[:, 1], y_hat, 'red')

#Using followers & polarity

X=df.followers
y=df.polarity

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.followers.min(), X.followers.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(3)

plt.subplot(211)

plt.scatter( df.followers,df.retwc)

plt.subplot(212)
plt.scatter(X.followers, y) # Plot the raw data plt.xlabel("Friends")
plt.ylabel("polarity")
plt.xlabel("Followers")
plt.plot(X_prime[:, 1], y_hat, 'red') # Add the regression line, colored in red


#Using Polarity & friends
y = df.polarity
X= df.friends
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.friends.min(), X.friends.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(4)

plt.subplot(211)

plt.scatter(df.friends, df.polarity)

plt.subplot(212)
plt.scatter(X.friends, y) # Plot the raw data plt.xlabel("Friends")
plt.xlabel("Friends")
plt.ylabel("polarity")
plt.plot(X_prime[:, 1], y_hat, 'red') # Add the regression line, colored in red


#Using friends & retweets

X=df.friends
y=df.retwc

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.friends.min(), X.friends.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(5)

plt.subplot(211)

plt.scatter( df.friends,df.retwc)

plt.subplot(212)
plt.scatter(X.friends, y) # Plot the raw data plt.xlabel("Friends")
plt.ylabel("retwc")
plt.xlabel("Friends")
plt.plot(X_prime[:, 1], y_hat, 'red')


#Using subjectivity & friends
y = df.polarity
X= df.friends
X=sm.add_constant(X)

X=sm.add_constant(X)

lr_model=sm.OLS(y,X).fit()
print(lr_model.summary())
print(lr_model.params)

X_prime = np.linspace(X.friends.min(), X.friends.max(), 100)
X_prime = sm.add_constant(X_prime)
y_hat = lr_model.predict(X_prime)

plt.figure(6)

plt.subplot(211)

plt.scatter(df.friends, df.subjectivity)

plt.subplot(212)
plt.scatter(X.friends, y) # Plot the raw data plt.xlabel("Friends")
plt.xlabel("Friends")
plt.ylabel("subjectivity")
plt.plot(X_prime[:, 1], y_hat, 'red') # Add the regression line, colored in red

