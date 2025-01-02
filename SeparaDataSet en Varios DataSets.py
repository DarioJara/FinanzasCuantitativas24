# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:01:59 2023

@author: Admin
"""
import pandas as pd

Ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/Prueba2.xlsx'

# Cargar el dataset original en un dataframe de Pandas
#df = pd.read_csv("dataset.csv")

df = pd.read_excel(Ruta)

# Dividir el dataframe en varios dataframes en base a una columna específica
grouped = df.groupby("TICKET")

# Crear un archivo de Excel
writer = pd.ExcelWriter("D:/2. Proyectos/3. Python/3.-Laboratorio/dataset_separado.xlsx", engine='openpyxl')

# Escribir cada grupo en una hoja diferente
for name, group in grouped:
    group.to_excel(writer, sheet_name=name, index=False)

# Guardar el archivo de Excel
writer.save()