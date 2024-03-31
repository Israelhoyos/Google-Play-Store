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


with st.container():
    left,right=st.columns(2)
    with left:
        st.header("POWER BI📊")
        st.write("""
***Power BI*** es una herramienta de análisis de datos y visualización que permite transformar datos brutos en información significativa y visualmente atractiva.
Sirve para ayudar a las organizaciones y usuarios a analizar, visualizar y compartir datos de manera efectiva. Uno de sus mayores atractivos es precisamente
que es interactivos sus resultados.               
                 """)
    
    with right:
        st.image("img\powerbi.png",width=500)

st.markdown("---")
st.markdown("")
st.markdown("")



st.markdown("**DATOS ALTERNATIVOS**")
st.markdown("\n")
st.markdown("")
#Exporto Mi PowerBI , usando la documentación necesaria extraida de la bibliografia
power_bi_iframe_code='<iframe title="final" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=4eac72b6-071d-4bc6-a842-4706952f4645&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" frameborder="0" allowFullScreen="true"></iframe>'
st.markdown("""<center>{}</center>""".format(power_bi_iframe_code),unsafe_allow_html=True)





