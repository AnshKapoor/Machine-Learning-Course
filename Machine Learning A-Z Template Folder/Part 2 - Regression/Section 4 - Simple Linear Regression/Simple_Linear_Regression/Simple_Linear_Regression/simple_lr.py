#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:28:38 2018

@author: ansh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values



from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(X_train,Y_train)
Y_pred = regressor.predict(X_test)

#plotting the data and visualising it
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train))
plt.title('Salary vs Experience')
plt.xlabel('Experience(years)')
plt.ylabel('Salary')
plt.show()
#plotting test results
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,regressor.predict(X_train))
plt.title('Salary vs Experience')
plt.xlabel('Experience(years)')
plt.ylabel('Salary')
plt.show()