#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:39:31 2020

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



#Funciones 

def cargar_serie_tiempo(ric,file_extension):
    
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

return x, x_str