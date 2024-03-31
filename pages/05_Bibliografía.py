import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import plotly_express as px
import plotly.graph_objects as go

import numpy as np
import pandas as p
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

import os
import json
import base64
import time as ts
from datetime import time

st.set_page_config(page_title="Google", page_icon=":📲:")

with st.sidebar:
    st.image("img\google.jpg")

with st.sidebar:
    select=option_menu(
    menu_title=None,
    options=["Documentación","YouTube"],
    icons=["browser-chrome","youtube"],
    menu_icon="cast",
    default_index=0,
    )

if select == "Documentación":
    st.title("DOCUMENTACIÓN 📝")
    st.markdown("---")

#Toda la documentación de Markdown y sus opciones las he sacado de la documentación oficial que está en la biografía.    
st.markdown("""
            + **[DATASET](https://github.com/gauthamp10/Google-Playstore-Dataset)**
            + **[DATASET2](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps)**
            + **[GOOGLE](https://www.google.es/)**
            + **[MATPLOTLIB](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes)**
            + **[STACKOVERFLOW - DUDAS](https://stackoverflow.com/questions/13918835/dynamic-update-x-axis-with-date-and-time-ticks-in-chaco)**
            + **[FLATICON - LOGOS](https://www.flaticon.com/search?word=google)**
            + **[MATPLOTLIB - EJES](https://interactivechaos.com/es/manual/tutorial-de-matplotlib/marcas-de-ejes)**
            + **[BLOG](https://cesarmesa.com.co/la-historia-de-google-play-store-que-es-y-como-funciona/#:~:text=La%20historia%20de%20Google%20Play%20comienza%20en%20el%20a%C3%B1o%202008,%E2%80%9CGoogle%20Play%E2%80%9D%2C%20una%20nueva)**
            + **[ESTRUCTURA](https://www.researchgate.net/publication/366229568_ANALISIS_DATASET_GOOGLE_PLAY_STORE_MENGGUNAKAN_METODE_EXPLORATORY_DATA_ANALYSIS_EDA_Analysis_of_Google_Play_Store_Datasets_Using_the_Exploratory_Data_Analysis_EDA_Method)**
            + **[COMPROVACIÓN RESULTADOS](https://www.appbrain.com/stats)**
            + **[STREAMLIT - CHEAT](https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlit.app/)**
            + **[STREAMLIT](https://docs.streamlit.io/library/api-reference#display-charts)**
            + **[INFO - STREAMLIT](https://www.corecode.school/blog/streamlit)**
            + **[MARKDOWN](https://www.markdownguide.org/cheat-sheet/)**
            + **[KATEX - MATHS](https://katex.org/)**
            + **[BOOTSTRAP](https://icons.getbootstrap.com/)** 
            + **[FUENTE](https://fontawesome.com/start)**
            * **[EMOJIS](https://emojipedia.org/es)**
            * **[LOGO](https://www.pngfind.com/freepng/google-play-logo-png/)**
            * **[NUMPY](https://numpy.org/doc/)**
            
            """
            )
st.markdown("---")
    
if select == "YouTube":
    #st.title("")
    st.image("img\youtube.png",width=300)
    st.markdown("""
                + **[AB TEST](https://www.youtube.com/watch?v=BakFbysF6aM)**
                + **[STREAMLIT - ANIMACIÓN](https://www.youtube.com/watch?v=TXSOitGoINE)**
                + **[STREANLIT - WEB](https://www.youtube.com/watch?v=zeS2FlxF_0s)**
                + **[SIDEBAR](https://www.youtube.com/watch?v=hEPoto5xp3k)**
                + **[DATACAMP](https://www.youtube.com/@DataCamp/playlists)**
                + **[DATASCHOOL](https://www.youtube.com/@dataschool)**
                + **[SENTDEX](https://www.youtube.com/@sentdex)**
                + **[STATQUEST](https://www.youtube.com/@statquest)**
                + **[DATASCIENCE](https://www.youtube.com/@Datasciencedojo)**
                
                """
                )
    st.markdown("---")

