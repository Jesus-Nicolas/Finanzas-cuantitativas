# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:59:17 2020

@author: Meva
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

'''
Goal: create a normality test e.g. Jarque-Bera

step 1: generate vector of iid random variables
step 2: visualise histogram of random variables
step 3: define what is the p-value
step 4: perform a Jarque-Bera test
step 5: a normal distribution can fail its normality test

To run the while loop of the normality test until it fails:
* Uncomment lines 31-33 and 82-84
* Indent lines 35-80 (select them and press Tab)

'''
### playing with Borel-Cantelli: P[all tests are normal = True] = 0
# is_normal = True
# counter = 0
# while is_normal and counter < 50:
    
# generate random variable
x_size = 10**6
degrees_freedom = 2
type_random_variable = 'chi-squared' # normal exponential student chi-squared

if type_random_variable == 'normal':
    x = np.random.standard_normal(size=x_size)
    x_str = type_random_variable
elif type_random_variable == 'exponential':
    x = np.random.standard_exponential(size=x_size)
    x_str = type_random_variable
elif type_random_variable == 'student':
    x = np.random.standard_t(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'
elif type_random_variable == 'chi-squared':
    x = np.random.chisquare(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'

# compute "risk metrics"
x_mean = np.mean(x)
x_std = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x) # excess kurtosis
x_var_95 = np.percentile(x,5)
x_cvar_95 = np.mean(x[x <= x_var_95])
jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(jb, df=2)
is_normal = (p_value > 0.05) # equivalently jb < 6

# print metrics
print(x_str)
print('mean ' + str(x_mean))
print('std dev ' + str(x_std))
print('skewness ' + str(x_skew))
print('kurtosis ' + str(x_kurt))
print('VaR 95% ' + str(x_var_95))
print('CVaR 95% ' + str(x_cvar_95))
print('Jarque-Bera ' + str(jb))
print('p-value ' + str(p_value))
print('is normal ' + str(is_normal))
    
# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title('Histogram ' + x_str)
plt.show()
    
    # counter +=1
    # print('counter ' + str(counter))
    # print('-----')


























