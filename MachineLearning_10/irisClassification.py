# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 02:08:40 2022

@author: paskorn.c
"""
#--------------- Data Import
import seaborn as sns
iris = sns.load_dataset('iris')

X_iris = iris.drop('species', axis=1)
#X_iris.shape() <- (150, 4)

y_iris = iris['species']
#y_iris.shape() <- (150,)

sns.set()
sns.pairplot(iris, hue='species', height=1.5);

#---------------- Cross Validation

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
random_state=1)

#---------------- Machine Learning API
from sklearn.naive_bayes import GaussianNB  # 1. choose model class
model = GaussianNB()                        # 2. instantiate model
model.fit(Xtrain, ytrain)                   # 3. fit model to data
y_model = model.predict(Xtest)              # 4. predict on new data

#---------------- Check Accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest, y_model))