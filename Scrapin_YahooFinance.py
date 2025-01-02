

import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr 
from datetime import datetime

 
yf.pdr_override()
#EQUITY
FECHA_HOY=(datetime.today().strftime('%Y-%m-%d'))
LISTA_EQUITYS=[['CABK.MC','IBE.MC','PHM.MC','TEF.MC','']
               ,['CAIXABANK','IBERDROLA','PHARMAMAR','TELEFONICA','REPSOL']]
TICKET='CLNX.MC'
Equity = [TICKET] #, 'TATAPOWER.NS', 'ITC.NS']
#INICIAMOS DATOS 
startdate = datetime(2022,1,22)
enddate = datetime(2023,1,22)
DataFramePrecios={}
DataFramePrecios = pdr.get_data_yahoo(Equity, start=startdate, end=enddate)
#RENOMBRAR COLUMNA PRECIO CIERRE AJUSTADO (Adj Close)
#DataFramePrecios.rename(columns={'Adj Close':'Adj_Close'})
                        
#AÑADIMOS COLUMNA LN
#DataFramePrecios.insert(6, 'LN', 1)
#DataFramePrecios['LN']=DataFramePrecios['Adj Close']/DataFramePrecios['Adj Close']  #.diff()
#PRECIO ANTERIOR
DataFramePrecios['AdjCloseAnterior']=DataFramePrecios['Adj Close'].shift(1,axis=0) #Mueve Datos hacia abajo
#VARIACION PRECIO CON LN
DataFramePrecios['lN']=np.log(DataFramePrecios['Adj Close']/DataFramePrecios['Adj Close'].shift(1,axis=0))
#RIESGO PROMEDIO
Riesgo_Promedio=DataFramePrecios['lN'].mean()

#INSERTAR RIESGO PROMEDIO EN EXCEL
DataFramePrecios['Riesgo_Promedio']=''
#DataFramePrecios.iloc[0,8]=Equity
DataFramePrecios.iloc[1,8]=Riesgo_Promedio

#CALCULO LOGARITMO NATURAL (RIESGO)
#Suma=DataFramePrecios['Adj Close'].sum()

#EXPORTAR A EXCEL
Nombre= TICKET + ' ' +FECHA_HOY + '.xlsx'

DataFramePrecios.to_excel(Nombre)

print (DataFramePrecios)
