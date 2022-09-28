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
y = x**2 - 1 + rng.randn(50)
plt.scatter(x, y);
