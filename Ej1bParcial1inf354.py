"""
Created on Mon Mar 29 16:08:07 2021

@author: hp
"""

#b)

import pandas as pd 
import numpy as np

df = pd.read_csv (r'C:\Universidad\Septimo\354\datasetVentasJuegos.csv')
pd.set_option('max_columns', None)
#Los resultados se expressan en millones, por eso los multiplico
mventasna=round(df["NA_Sales"].mean()*1000000,2)
mventaseu=round(df["EU_Sales"].mean()*1000000,2)
mventasjp=round(df["JP_Sales"].mean()*1000000,2)
mventasot=round(df["Other_Sales"].mean()*1000000,2)
mventasgl=round(df["Global_Sales"].mean()*1000000,2)

print("Medias\n"
      "Ventas Norte America: ", mventasna, "\n" 
      "Ventas Europa: ", mventaseu, "\n" 
      "Ventas Japon: ", mventasjp, "\n" 
      "Ventas Resto del mundo: ", mventasot, "\n" 
      "Ventas Globales: ", mventasgl, "\n" )


modanom = df["Name"].mode()
modaaño = df["Year"].mode() 
modaplat = df["Platform"].mode()
modagen = df["Genre"].mode() 
modapub = df["Publisher"].mode()
modana = round(df["NA_Sales"].mode()*1000000,2)
modaeu = round(df["EU_Sales"].mode()*1000000,2)
modajp = round(df["JP_Sales"].mode()*1000000,2)
modaot = round(df["Other_Sales"].mode()*1000000,2)
modagl = round(df["Global_Sales"].mode()*1000000,2)

print("Modas\n"
      "Nombre: ", modanom[0], "\n"
      "Año: ", modaaño[0], "\n"
      "Plataforma: ", modaplat[0], "\n"
      "Genero: ", modagen[0], "\n"
      "Publisher(Editora): ", modapub[0], "\n"
      "Ventas Norte America: ", modana[0], "\n" 
      "Ventas Europa: ", modaeu[0], "\n" 
      "Ventas Japon: ", modajp[0], "\n" 
      "Ventas Resto del mundo: ", modaot[0], "\n" 
      "Ventas Globales: ", modagl[0], "\n" )



print("Desviación estándar\n"
      "Ventas Norte America: ", round(df["NA_Sales"].std(),4), "\n" 
      "Ventas Europa: ",round(df["EU_Sales"].std(),4), "\n" 
      "Ventas Japon: ", round(df["JP_Sales"].std(),4), "\n" 
      "Ventas Resto del mundo: ", round(df["Other_Sales"].std(),4), "\n" 
      "Ventas Globales: ", round(df["Global_Sales"].std(),4), "\n" 
      )











