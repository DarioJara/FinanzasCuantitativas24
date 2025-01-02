# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 19:01:32 2022

@author: Admin
"""

import pandas as pd
import  numpy as np

Ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/DataFramePrueba1.xlsx'

#Para una hoja
Hoja=pd.read_excel(Ruta,sheet_name='hja1')

print (Hoja)

#Varias Hojas en un diccionario de datos
VariasHojas=pd.read_excel(Ruta,sheet_name=None)

df=pd.concat(VariasHojas,ignore_index=True)

#Tipo de Columna
df.dtypes

#Operaciones Columna

df['Valor']=185*df['Valor']

#Añadir Columna con numeros secuenciales
df['Contador']=np.arange(len(df))+1

print (df)