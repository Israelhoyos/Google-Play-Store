# Iniciando la impotanción de librerías para su posterior utilización 
'''
Inicio del programa de proyecto final, comentado linea por linea , usando las diferentes tecnologias
usados en la carrera , optimizando los tiempos y con método ensayo-error.
Dio como resultado la aprovación del proyecto y su ejecución.

'''

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import plotly_express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

import os
import json

import base64
import time as ts
from datetime import time

#Inicio del código

st.set_page_config(page_title="Google", page_icon=":📲:")


with st.sidebar: #Crea un panel lateral en streamlit donde se puede agregar widges, sacando la información de la documentación oficial.
    st.image("img\google.jpg")

#Funcion para una animación
def load_lottieurl2(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding=load_lottieurl2("https://lottie.host/3efc5ff0-a96b-4bcd-8ff9-fdedc61a5d15/xk6pB7HcrG.json")
st_lottie(lottie_coding,height=400,key="coding2")


st.markdown("""
            ## LIMPIEZA 🗑️
            """)

code="""
#ELIMINO LAS COLUMNAS QUE NO VOY A UTILIZAR

data.drop(["App Id","Currency","Minimum Android","Developer Id",
                   "Developer Website","Developer Email","Privacy Policy",
                   "Editors Choice","Scraped Time"],axis=1,inplace=True)
"""
st.code(code,language="python") #Nos permitirá enseñar el código en Streamlir de una manera más visual

code1=("""
       #Sustituyo los valores NaN de la columna "Released" por la columna "Last Updated"
       data["Released"].fillna(data["Last Updated"],inplace=True)
       data.dropna(subset=["App Name","Installs","Minimum Installs","Size"],inplace=True)

       #Sustituyo valores de string a numéricos
       data["Rating"] = data["Rating"].astype(float)
       avg = round(data["Rating"].mean(),1)
       data["Rating"].fillna(avg,inplace=True)
       data["Rating Count"] = data["Rating Count"].astype(float)

       #Rellenar los valores faltantes con la media
       avg = round(data["Rating Count"].mean(),1)
       data["Rating Count"].fillna(avg,inplace=True)

       
       """)
st.code(code1,language="python")

st.image("img\data.png")

st.markdown("---")

state = st.checkbox("Más Código", value=False)

code3="""
#LIMPIO ALGUNOS VALORES PARA SOLO TENER 3 CATEGORIAS
#Everyone - Teens - Adult

data["Content Rating"] = data["Content Rating"].replace("Unrated","Everyone")
data["Content Rating"] = data["Content Rating"].replace("Mature 17+","Adults")
data["Content Rating"] = data["Content Rating"].replace("Adults only 18+","Adults")
data["Content Rating"] = data["Content Rating"].replace("Everyone 10+","Everyone")
data["Content Rating"].value_counts()

"""

if state:
    st.code(code3,language="python")
    st.markdown("""
Everyone    711060\n
Teen         68039\n
Adults       20796\n
Name: Content Rating, dtype: int64\n

            """)
else:
    pass

code4="""

#LOS PRECIOS ESTÁN EN DÓLARES, LOS CAMBIO A EUROS CREANDO UNA NUEVA COLUMNA
data['Price Range'] = data['Price'] * 0.93

#REAGRUPAMOS LOS DIFERENTES RANGOS DE PRECIOS EN CUATRO VALORES
data['PriceRange'] = pd.cut(data['Price Range'],bins=[0,0.19,9.99,29.99,372],labels=['Gratis','Bajo','Medio','Alto'],include_lowest=True)
dummies = pd.get_dummies(data['PriceRange'],prefix='Price')
data = data.join(dummies)
data['PriceRange'].value_counts()

"""
if state:
    st.code(code4,language="python")
    st.markdown("""
Gratis         784294\n
Bajo           14618\n
Medio         700\n
Alto            283\n
Name: PriceRange, dtype: int64\n
                
                """)
else:
    pass

code5="""
#TRANSFORMO EL RANGO DE CLASIFICACIONES PARA UNA MEJOR COMPRENSIÓN
data["Rating Type"] = "Sin Rating"
data.loc[(data["Rating Count"] > 0) & (data["Rating Count"] <= 10000.0),"Rating Type"] = "Menos de 10K"
data.loc[(data["Rating Count"] > 10000) & (data["Rating Count"] <= 500000.0),"Rating Type"] = "Entre 10K y 500K"
data.loc[(data["Rating Count"] > 500000) & (data["Rating Count"] <= 138557570.0),"Rating Type"] = "Más de 500K"
data["Rating Type"].value_counts()

"""
if state:
    st.code(code5,language="python")
    st.markdown("""
Menos de 10K        420371\n
Sin Rating          366552\n
Entre 10K y 500K     12418\n
Más de 500K            554\n
Name: Rating Type, dtype: int64\n

                """)
else:
    pass



#Funcion para una animación
def load_lottieurl3(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding=load_lottieurl3("https://lottie.host/d86cf39a-9c92-4256-90b4-312f74c15edb/ax9jsllbGp.json")
st_lottie(lottie_coding,height=350,key="coding3")
