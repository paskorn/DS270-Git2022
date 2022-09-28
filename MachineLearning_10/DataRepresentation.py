# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:59:15 2022

@author: paskorn.c
"""
import seaborn as sns
iris = sns.load_dataset('iris')
print(iris.head())



X_iris = iris.drop('species', axis=1)
print(X_iris.shape)

y_iris = iris['species']
print(y_iris.shape)

sns.set()
sns.pairplot(iris, hue='species', height=1.5);