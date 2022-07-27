#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:44:33 2022

@author: life
"""
##import Libraries required
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
#DATA
data=pd.read_csv('advertising.xls')
##print the head
print(data.head())
##find whether there is any null data
print(data.isnull().sum())
###shape of data
print(data.shape)
##describe the data
print(data.describe())
###plot to find the co relation
sns.heatmap(data.corr(),cmap="YlGnBu" ,annot=True)
###X
X=data['TV'].tolist()
Y=data['Sales'].tolist()
##mean
def meanlist(l):
    return(sum(l)/len(l))
##covariance
def cov(X,X_mean,Y,Y_mean):
     arr=np.array(X)
     arr_1=np.array(Y)
     return(np.sum((arr-X_mean)*(arr_1-Y_mean)))
##variance
def var(X,X_mean):
    arr=np.array(X)
    return (np.sum((arr-X_mean)**2))
    
def coefficient(X,Y):
    X_mean=meanlist(X)
    Y_mean=meanlist(Y)
    m=cov(X,X_mean,Y,Y_mean)/var(X,X_mean)
    c=Y_mean-X_mean*m
    return(m,c)
    
###Linearregression
def Linearregression(X_train,Y_train,X_test,Y_test):
    prediction=[]
    m,c=coefficient(X_train,Y_train)
    for i in X_test:
        y=m*i+c
        prediction.append(y)
    mse = mean_squared_error(prediction, Y_test)
    r2 = r2_score(prediction, Y_test)
    print("The R2 score of the model is: ", r2)
    print(mse)    
    return(prediction)    
    
Linearregression(X[:140],Y[:140],X[:60],Y[:60])

