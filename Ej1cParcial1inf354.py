# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:00:18 2021

@author: hp
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv (r'C:\Universidad\Septimo\354\datasetVentasJuegos.csv')

pd.options.display.max_rows = 100
print('100 juegos mas vendidos'.center(50,' '))
print(df['Name'][:100])


x_values = df['Rank']
y_values = df['Global_Sales']

plt.bar(x_values, y_values)
plt.xlim(0, 100)
plt.ylim(0, 83)
plt.title('100 juegos más vendidos')
plt.xlabel('Posición')
plt.ylabel("Juegos vendidos(en millones)")
plt.show()


plt.title('Ventas de los 100 juegos \nmás vendidos en Norte America')
plt.xlabel('Posición')
plt.ylabel("Juegos vendidos(en millones)")
y_values = df['NA_Sales']
plt.bar(x_values, y_values)
plt.xlim(0, 100)
plt.ylim(0, 45)
plt.show()

plt.title('Ventas de los 100 juegos \n en Europa')
plt.xlabel('Posición')
plt.ylabel("Juegos vendidos(en millones)")
y_values = df['EU_Sales']
plt.bar(x_values, y_values)
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.show()

plt.title('Ventas de los 100 juegos \nmás vendidos en Japón')
plt.xlabel('Posición')
plt.ylabel("Juegos vendidos(en millones)")
y_values = df['JP_Sales']
plt.bar(x_values, y_values)
plt.xlim(0, 100)
plt.ylim(0, 15)
plt.show()


plt.title('Ventas de los 100 juegos \nmás vendidos en el resto del mundo')
plt.xlabel('Posición')
plt.ylabel("Juegos vendidos(en millones)")
y_values = df['Other_Sales']
plt.bar(x_values, y_values) 
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.show()