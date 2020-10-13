#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:08:03 2020

@author: jnm
"""

#Viendo los temas anteriores aplicados a datos de mercado

#Usando la libreria pandas para un Dara Frame



import numpy as np
import pandas as pd
import scipy
import numpy as np
import pandas as pd
import matplotlib as mpl
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2


#Insertar datos

ric= 'DBK.DE'
file_extension
path = '/home/jnm/Documentos/Proyectos en Python/Seminario de finanzas/' + ric + '.csv'
table_raw = pd.read_csv(path)


#Datos del mercado

t = pd.DataFrame()
t['date'] = pd.to_datetime(table_raw['Date'],dayfirst=True)
t['close'] = table_raw['Close']
t['close_previous'] = table_raw['Close'].shift(1)
t['return_close'] = t['close']/t['close_previous'] - 1
t = t.dropna() #Quitar los valores nulos
t = t.reset_index(drop = True)


#Graficar series de tiempo

plt.figure()
plt.plot(t['date'],t['close'])
plt.title('Serie de tiempo de los precios' + ric)
plt.xlabel('Tiempo')
plt.ylabel('Precio')
plt.show()

#Resultados del test de Jarque-Bera

x = t['return_close'] #Resultado

x_str = 'Resultados reales' + ric #Etiqueta

x_size = len(x) #Tamaño del resultado 


#Reciclar el codigo anterior

# compute "risk metrics"
x_mean = np.mean(x)
x_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x) # excess kurtosis
x_var_95 = np.percentile(x,5)
x_cvar_95 = np.mean(x[x <= x_var_95])
jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(jb, df=2)
is_normal = (p_value > 0.05) # equivalently jb < 6


#Cociente de sharpe : Rendimiento esperado por unidad de riesgo
#Desviación estandar : Volalitilidad en el mercado

#Sharpe mayor a 2 para asegurar que nuestro intervalo de confianza 
#Al menos la media es positiva

#Sharpe anualizado

x_sharpe = x_mean / x_stdev*np.sqrt(252) #Anual donde son 252 días

# print metrics
print(x_str)
print('mean ' + str(x_mean))
print('std ' + str(x_stdev))
print('skewness ' + str(x_skew))
print('kurtosis ' + str(x_kurt))
print('VaR 95% ' + str(x_var_95))
print('CVaR 95% ' + str(x_cvar_95))
print('Jarque-Bera ' + str(jb))
print('p-value ' + str(p_value))
print('is normal ' + str(is_normal))
print('sharpe :' + str(x_sharpe))

    
# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title('Histogram ' + x_str)
plt.show()


#Clase 3 



#Mostrar medidas en las graficas 


round_digits =4

#Pendiente


