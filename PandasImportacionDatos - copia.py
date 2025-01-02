# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:26:51 2022

@author: Admin
"""

import pandas as pd

Ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/TELEFONICA.csv'

File = pd.ExcelFile(Ruta)

Hoja=(File.sheet_names)

#df=File.parse(‘inicial’)

DataSet=File.parse('Datos')

#Imprimir Datos
print(DataSet)


