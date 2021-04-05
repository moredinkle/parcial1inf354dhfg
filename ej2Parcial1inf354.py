# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:40:30 2021

@author: hp
"""
import pandas as pd 
from sklearn import preprocessing
import numpy
df= pd.read_csv(r'C:\Universidad\Septimo\354\datasetVentasJuegos.csv', skiprows=0, low_memory=False)
pd.set_option('max_columns', None)
numpy.set_printoptions(precision=4, suppress=True)
df= df.dropna(thresh=len(df.index)/2,axis=1)
x = df.iloc[:,6:11].values
y = df.iloc[:, 10].values
print('Datos iniciales:')
print(x[0:10,:])
print('\nSe imprimen las 10 primeras filas de cada ejercicio\n'
      '\nEstandarización o eliminación de medias y escalado de varianza')
scaler = preprocessing.StandardScaler().fit(x)

x_scaled = scaler.transform(x)
print('\nDatos escalados:\n',
      x_scaled[0:10,:],
      '\n\nMedias:',x_scaled.mean(axis=0),
      '\nDesviación estandar:',x_scaled.std(axis=0))



print("\nEscalar datos a un rango(0,100):\n")
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 100))
X_train_minmax = min_max_scaler.fit_transform(x)

print(X_train_minmax[0:10,:])


print("\nNormalizar los datos:\n")
escalador = preprocessing.Normalizer().fit(x)
normalizedX = escalador.transform(x)
print(normalizedX[0:10,:])
'''
Acá la ultima columna es ventas globales, la suma
del resto de columnas, por eso la suma de las columnas 
no da 1, pero la suma de las 4 primeras da la ultima columna
'''
