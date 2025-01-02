# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:30:30 2022

@author: Admin
"""

import os.path
import pandas as pd

# def readAllSheets(filename):
#     if not os.path.isfile(filename):
#         return None
    
#     xls = pd.ExcelFile(filename)
#     sheets = xls.sheet_names

#     results = {}

#     for sheet in sheets:
#         results[sheet] = xls.parse(sheet)
        
#     xls.close()
    
#     return results, sheets

#Usar Funcion

    Ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/PlantillaPrueba.xlsx'
    xls = pd.ExcelFile(Ruta)
    sheets = xls.sheet_names
    
    results = {}

    for sheet in sheets:
        results[sheet] = xls.parse(sheet)
        
    results.to_csv('PRUEBA3.CSV')    
    print (results)
