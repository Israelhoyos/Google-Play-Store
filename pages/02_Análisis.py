#Importacion de los modulos necesarios

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
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import re
import csv
import base64
import time as ts
from datetime import time

#Inicio del código

st.set_page_config(page_title="Google", page_icon=":📲:")

with st.sidebar:
    st.image("img\google.jpg")

#LEEMOS EL DATASET MODIFICADO PARA PODER UTILIZARLO
data1=pd.read_csv(r"data\data1.csv")



with st.container(): #Crea un contenedor visual que se puede incluir otros elementos
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("ANÁLIS EXPLORATORIO 📈")
        st.write("""
Mi objetivo principal del análisis exploratorio es obtener una comprensión inicial de los datos 
antes de realizar análisis más avanzados. Me ayuda a identificar patrones,
tendencias y relaciones en los datos, lo que puede ser útil para tomar decisiones 
informadas y diseñar estrategias de análisis más detalladas.
                 """)
    

    with right_column:
        st.image("img\Analytics.png")

#Creamos nuevas pestañas con este código, que se cargará automáticamente
tab1,tab2,tab3,tab4 = st.tabs(["PREGUNTAS","ANÁLISIS","DESCARGAS","EXTRA"])


with tab1:
    col1,col2=st.columns(2)
    with col1:
        st.markdown("""
**CUANTAS APLICACIONES ESTÁN DISPONIBLES?**                
                """)
        apps=data1["Type"].value_counts()
        apps.plot.bar(figsize=(10,8))
        for i, v in enumerate(apps):
            plt.text(i,v,str(v),ha="center",va="bottom")
    
        st.bar_chart(apps)

        st.markdown("""
**LAS APLICACIONES TIENE MUCHAS CALIFICACIONES?**                
                """)
        rating=data1["Rating"].value_counts()
        rating.plot.bar(figsize=(10,8))
        for i, v in enumerate(rating):
            plt.text(i,v,str(v),ha="center",va="bottom")    
        st.bar_chart(rating)


        st.markdown("""
**TODAS LAS APLICACIONES TIENEN CLASIFICACIÓN?**                
                """)
        type=data1["Rating Type"].value_counts()
        type.plot.bar(figsize=(10,8))
        for i, v in enumerate(type):
            plt.text(i,v,str(v),ha="center",va="bottom")
    
        st.bar_chart(type)








    with col2:
        st.markdown("""
**LAS APPS DE PAGO SON COSTOSAS?**                 
                    """)
        price=data1["PriceRange"].value_counts()
        price.plot.bar(figsize=(10,8))
        
        for j,y in enumerate(price):
            plt.text(j,y,str(y),ha="center",va="bottom")
        st.bar_chart(price)

        st.markdown("""
**QUE CATEGORÍA TIENE MAYOR NÚMERO DE APLICACIONES?**                  
                    """)
        category=data1["Category"].value_counts()
        category.plot.bar(figsize=(10,8))
        for j,y in enumerate(category):
            plt.text(j,y,str(y),ha="center",va="bottom")
        st.bar_chart(category)


        st.markdown("""
**APPS SUPERIORES A 9,99€?**                  
                    """)
        bajo=data1["Price_Bajo"].value_counts()
        bajo.plot.bar(figsize=(10,8))
        for j,y in enumerate(bajo):
            plt.text(j,y,str(y),ha="center",va="bottom")
        st.bar_chart(bajo)



with tab2:
    st.title('Análisis')

    option = st.selectbox('**Que análisis deseas ver?**',('Social', 'Económico', 'Rating'))
    st.write("")
    st.write("")
    if option == ('Social'):
        st.image("img/clasificacion.png", width=800)
        st.markdown("---")
        st.image("img/apps_gratis.png", width=800)
        st.markdown("---")
        st.image("img/apps_pago.png", width=800)
        
        
    if option == ('Económico'):
        st.image("img/gratis_pago.png",width=800)
        st.markdown("---")
        st.image("img/gratis_pago1.png",width=800)
        st.markdown("---")
        st.image("img/porcentaje.png",width=500)



    if option == ('Rating'):
        st.image("img/rating_precio.png",width=800)
        st.markdown("---")
        st.image("img/rating_categoria.png",width=800)
        st.markdown("---")
        st.image("img/rating_categoria1.png",width=800)




with tab3:
    option = st.radio('**Que descarga quieres ver?**',("General","Más Descargadas"))

    if option == ("General"):
        st.image("img/descargas.png", width=800)
        
    if option == ("Más Descargadas"):
        st.image("img/descargas1.png", width=800)




with tab4:
    st.markdown("""
### La aplicación más costosa
**MESH Connect - 372€**         
                """)
    st.image("img\QR.png")
    st.markdown("---")


    st.markdown("""
### CORRELACIÓN
                """)
    st.image("img\corr.png")
    




























        