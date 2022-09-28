# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:59:13 2022

@author: paskorn.c
"""

# Create DATA to Play with
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);

#Machine Learning API in SKlearn

#------------- 1 Select Model
from sklearn.linear_model import LinearRegression

#------------- 2 Choose Hyper Parameter
model = LinearRegression(fit_intercept=True)
print(model)


#------------- 3 Arrange DATA
X = x[:, np.newaxis] # X Features

#------------- 4 Fit the Model
model.fit(X, y)
print(model.coef_)
print(model.intercept_)

#------------- 5 Test with new Data
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.plot(xfit, yfit, color='red');
print(model.predict ([[10]]) )