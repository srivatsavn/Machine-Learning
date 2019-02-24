# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:55:05 2018

@author: Administrator
"""

import pandas as pd
import numpy as np

x = np.array([95,85,80,70,60])
y = np.array([85,95,70,65,70])

x_mean = np.mean(x)
y_mean = np.mean(y)

b1 = sum((x-x_mean)*(y-y_mean))/(sum((x-x_mean)**2))
b1

b0 = y_mean-b1*x_mean
b0

y_pred = b1*x + b0 ## Regression Line
y_pred

y=y.reshape(-1,1)  ## To reshape to column vector
y_pred=y_pred.reshape(-1,1)  ## Previously shape of y was [5,]
out = np.concatenate((y, y_pred), axis = 1)
out

res = float(sum(y_pred-y))
sq_err=float(sum((y-y_pred)**2))
mse = np.mean((y-y_pred)**2)
rmse = np.sqrt(np.mean((y-y_pred)**2))

print("The Residue is:", res)
print("The Squared Error is:", sq_err)
print("Mean Squared Error is:", mse)
print("The Root Mean Squared Error is:", rmse)

r_sqr =1 - sum((y-y_pred)**2)/sum((y-y_mean)**2)
r_sqr

n = len(x)
p=1
r_adj = 1 - ((1-r_sqr**2)*(n-1))/(n-p-1)
r_adj

