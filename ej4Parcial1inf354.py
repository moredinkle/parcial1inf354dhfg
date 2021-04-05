# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:22:43 2021

@author: hp
"""
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import model_selection

df = pd.read_csv (r'C:\Universidad\Septimo\354\datasetVentasJuegos.csv')
pd.set_option('max_columns', None)
df= df.dropna(thresh=len(df.index)/2,axis=1)
x = df.iloc[:,:].values

for i in range(0,len(x)):
    x[i,5]=str(x[i,5])
    x[i,10]=int(round(x[i,10]))

encoderx= LabelEncoder()
x[:,2]=encoderx.fit_transform(x[:,2])
x[:,3]=encoderx.fit_transform(x[:,3])
x[:,4]=encoderx.fit_transform(x[:,4])
x[:,5]=encoderx.fit_transform(x[:,5])


y = x[:,10]
y=y.astype('int')

clasificador = tree.DecisionTreeClassifier(criterion='entropy')
clasificador.fit(x[:,2:6], y)
prediccion=clasificador.predict([[26,297,6,359],[11,276,4,359]])
print(prediccion)


X_train, X_test, y_train, y_test = model_selection.train_test_split(x[:,2:6], y, test_size=0.0002)


clasificador.fit(X_train, y_train)
prediccion = clasificador.predict(X_test)
print(prediccion)
print(y_test)
print(confusion_matrix(y_test, prediccion))
print(classification_report(y_test, prediccion))






