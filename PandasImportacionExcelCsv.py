
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:26:51 2022

@author: Admin

Ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/TELEFONICA.csv'
mydataset = pd.read_csv('D:/2. Proyectos/3. Python/3.-Laboratorio/TELEFONICA.csv')


"""

import pandas as pd
mydataset=pd.read_csv('TELEFONICA.csv')
"""print (mydataset)"""
"""print(mydataset['Adj Close'])"""
"""print(mydataset.sort_values('Date', ascending=False))"""
"""print(mydataset.loc[0:3]) """
#print (mydataset['Adj Close']>3.5)
#print(mydataset[(mydataset['Adj Close'] > 2) & (mydataset['Date'] > '2022-01-25')])
#print(mydataset[(mydataset['Adj Close'] > 3.2) & (mydataset['Date'] > '2022-01-25'),['Date','Adj Close']])
#Vector1=mydataset['Date','Open']
#print (Vector1)
#print(Vector1[Vector1>'2022-12-01'])
mydataset.insert(6, 'column2', -15)

mydataset.loc[:,'Nuevo2']=mydataset['Open']*2

mydataset.to_csv('PRUEBA.CSV')
mydataset.to_csv('PRUEBA2.CSV', sep=';')
#print(mydataset)
