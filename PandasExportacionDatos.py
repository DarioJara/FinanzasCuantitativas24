# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:01:01 2022

@author: Admin
"""

#ARCHIVO PARA IMPORTAR DATOS DE YAHOO FINANCE 365

import pandas as pd
from urllib.request import Request, urlopen

Ruta='https://es.finance.yahoo.com/quote/TEF.MC/history?p=TEF.MC'
#DataFrame=pd.read_html('https://es.finance.yahoo.com/quote/TEF.MC/history?p=TEF.MC')
req=Request(Ruta, headers={'User-Agent': 'Mozilla/5.0'})  
html = urlopen(req)
print(html)


    






