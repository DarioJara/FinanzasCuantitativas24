#!/usr/bin/env python
# coding: utf-8

# In[147]:


import numpy as np 
import pandas as pd
import yfinance as yf
import datetime #FechaActual
from pandas_datareader import data as pdr


# In[167]:


yf.pdr_override()
#TATAELXSI = ['SAN.MC']


# In[184]:


Dias=10
Fecha_Actual = datetime.date.today()
Fecha_Anterior=Fecha_Actual - datetime.timedelta(days=Dias)
Cartera=['SAN.MC','^IBEX','TEF.MC','IBE.MC','FER.MC']
Tamaño_Cartera=len(Cartera)
Ruta_Exportacion='D:/2. Proyectos/3. Python/3.-Laboratorio/dataset.xlsx'
Data = pdr.get_data_yahoo(Cartera, start=Fecha_Anterior, end=Fecha_Actual)
#data = pdr.get_data_yahoo("SPY,SAN.MC,^IBEX", start=Fecha_Anterior, end=Fecha_Actual)
#data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")


# In[198]:


Df=pd.DataFrame(Data)
Df_resumido = Df.iloc[:, 0:Tamaño_Cartera]
Resultados=pd.DataFrame()
#Df_resumido = Df.iloc[:, 0:3]
#Calculo de Rentabilidades
for i in Cartera:
    Df_resumido['Variacion Intraday',i]=np.log(Df_resumido['Adj Close', i]/Df_resumido['Adj Close', i].shift(1))
    


# In[110]:


#Export to excel
writer = pd.ExcelWriter(Ruta_Exportacion, engine='xlsxwriter')
Df_resumido.to_excel(writer, sheet_name='CarteraPrecios')
writer.save()


# In[ ]:




