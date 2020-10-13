#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:16:56 2020

@author: jnm
"""

import numpy as np
import pandas as pd
import scipy
import numpy as np
import pandas as pd
import matplotlib as mpl
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

'''
Crear un test de normalidad Jarque Bera
'''

'''
Paso 1:: Generar variables aleatorias

Paso 2: Visualizar el histograma


Paso 3: Test
'''

#Generar la variable aleaotoria

x_size = 10**6
degrees_freedom = 2
type_random_variable = 'student' # normal exponential student

if type_random_variable == 'normal':
    x = np.random.standard_normal(size=x_size)
    x_str = type_random_variable
elif type_random_variable == 'exponential':
    x = np.random.standard_exponential(size=x_size)
    x_str = type_random_variable
elif type_random_variable == 'student':
    x = np.random.standard_t(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'


# compute "risk metrics"
x_mean = np.mean(x)
x_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x) # excess kurtosis

# print metrics
print(x_str)
print('mean ' + str(x_mean))
print('std ' + str(x_stdev))
print('skewness ' + str(x_skew))
print('kurtosis ' + str(x_kurt))


# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title('Histogram ' + x_str)
plt.show()


#Valor en riesgo 

x_var95 = np.percentile(x,5)

print('VaR 95% ' + str(x_var95))


#Jarque-Bera

x_jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)

print('Jarque-Bera' + str(x_jb))


#p-value

p_value = 1-chi2.cdf(x_jb,df = degrees_freedom)


#Criterio de normalidad

is_normal = (p_value >0.005) #Equivalente a jb<6

print('Normalidad: ' + str(is_normal))