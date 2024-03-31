#TRABAJO FINAL DE BOOTCAMP : GOOGLE PLAY STORE

#SÁBADO 29 DE JULIO 2023

#REALIZADO POR : ISRAEL HOYOS CATOTA



#CARGAR LIBRERÍAS

#El cargo de librería siemrpe es necesario para poder procesar los diferentes módulos que nos vamos a encontrar\\
#Se tiene que explorar las diferentes métricas que se nos presentan en los diferentes problemas a resolver.
#Aquí se tiene una muestra de las librerías que serán necesarias llamar y sus funciones.
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

#Cambia el nombre y añade un icono a el índice de la página
st.set_page_config(page_title="Google", page_icon=":📲:")

#Funcion para una animación 
# (ESTE CÓDIGO DE ANIMACIÓN LO HE SACADO DE UN VIDEO DE YOUTUBE, QUE ESTÁ PUESTO EN MI BIBLIOGRAFIA)
def load_lottieurl2(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#Todas las extensiones de las animaciones con inicio HTTTPS , salen de la página oficial LOTTIESFILES, añadida en la Bibliografía
lottie_coding=load_lottieurl2("https://lottie.host/b657434f-c931-4376-9de6-0f7a4c3f8eac/WEmm9d5Khh.json")
st_lottie(lottie_coding,height=300,key="coding2")





#Funcion para una animación
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding=load_lottieurl("https://lottie.host/feb97bb7-e26f-4d51-99f4-4fdb99742a37/HM1ICvmYUR.json")
imagen = Image.open("img\google.jpg")

with st.container():
    st.subheader("Trabajo Final :wave:")
    st.markdown("""
                **Google Play Store** es una plataforma de distribución digital de aplicaciones, juegos, música, libros y películas desarrollada por Google. Fue lanzada el 22 de octubre de 2008 bajo el nombre de Android Market, como una tienda de aplicaciones exclusiva para dispositivos Android.
En 2012, Google decidió cambiar el nombre de Android Market a ***Google Play Store***, con el objetivo de unificar todas las tiendas digitales de Google bajo una sola marca. Ahora ofrecía no solo aplicaciones, sino también música, libros y películas.

Con el tiempo, ***Google Play Store*** se ha convertido en la tienda de aplicaciones más grande y popular del mundo, con millones de aplicaciones disponibles para descargar en dispositivos Android. Además, ofrece una amplia gama de contenido multimedia.
Google Play Store también ha implementado medidas de seguridad para proteger a los usuarios de aplicaciones maliciosas. Cada aplicación pasa por un proceso de revisión antes de ser publicada en la tienda, y Google utiliza sistemas de detección de malware para identificar y eliminar aplicaciones sospechosas.

En resumen, la historia de ***Google Play Store*** es la historia de una tienda digital que ha crecido y evolucionado junto con el sistema operativo Android, convirtiéndose en una plataforma integral para la distribución de aplicaciones y contenido multimedia.
                """
                )
    st.write("[Más Información >>>](https://cesarmesa.com.co/la-historia-de-google-play-store-que-es-y-como-funciona/#:~:text=La%20historia%20de%20Google%20Play%20comienza%20en%20el%20a%C3%B1o%202008,%E2%80%9CGoogle%20Play%E2%80%9D%2C%20una%20nueva)")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Mi objetivo")
        st.write("""
                 **1. Identificar patrones y tendencias:** Para comprender mejor un fenómeno o tomar decisiones informadas.

                **2. Realizar predicciones y pronósticos:** Para la planificación y toma de decisiones estratégicas.

                **3. Identificar relaciones:** Para comprender las causas y efectos de un fenómeno.

                **4. Tomar decisiones efectivas:** La información y evidencia objetiva puede ayudar a tomar mejores decisiones basadas en los datos.

                **5. Representación gráfica:** La representación gráfica es más esficaz y visualmente se entiende mejor.
                 """)
    

    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")
        
st.markdown("---")

with st.sidebar:
    select=option_menu(
    menu_title=None,
    options=["Play Store","Android","Google"],
    icons=["google-play","android2","google"], #El nombre de los iconos salen predefinidos en la página GETBOOTSTRAP, añadido en la bibliografía
    menu_icon="cast",
    default_index=0,
    )

if select == "Android":
    st.title("ANDROID")
    print("")
    print("")
    with st.container():
        left,right= st.columns(2)
        with left:
            st.image("img\Android.png",width=200)

        with right:
            #Todas las modificaciones dentro de un Markdown están sacadas de la documentación oficial, añadido en la bibliografía
            st.markdown("""
- **1. Sistema operativo de código abierto.** 
                        
- **2. Compatibilidad.**

- **3. Actualizaciones.**

- **4. Integración con servicios de Google.**

- **5. Integración con servicios en la nube.**

                        """
                        )


if select == "Google":
    
    st.markdown("")
    st.image("img\google1.png",width=300)
    st.markdown("")
    st.markdown("""
### ***¿Qué es Google?***

Google es una empresa que se dedica principalmente a servicios y productos relacionados con Internet,
motores de búsqueda, publicidad en línea, servicios en la nube, software y hardware.
Además, Google es conocido por su motor de búsqueda homónimo, que es uno de los más utilizados en todo el mundo.

                
### ***Algunas características de Google:***

**1. Motor de búsqueda:** Google es conocido principalmente por su motor de búsqueda, que es uno de los más utilizados y populares en todo el mundo.

**2. Innovación:** Google se destaca por su constante innovación en el campo de la tecnología y sencillez.

**3. Énfasis en la usabilidad:** Google se esfuerza por ofrecer productos y servicios que sean fáciles de usar y accesibles para todos los usuarios. ***Diseño minimalista*** y enfoque en la experiencia del usuario son características distintivas de la marca.

**4. Compromiso con la información:** La empresa se esfuerza por proporcionar resultados de búsqueda imparciales y relevantes, y también ha implementado iniciativas para combatir la desinformación en línea.

**5. Diversificación de productos:** Google ha diversificado su cartera de productos y servicios, expandiéndose a áreas como publicidad en línea, dispositivos móviles, inteligencia artificial, realidad virtual, entre otros.

En resumen, Google se caracteriza por su liderazgo en el campo de la tecnología, su enfoque en la innovación y la usabilidad, su cultura empresarial única y su compromiso con la información y la accesibilidad en línea.


        
                
                """)

with st.sidebar:
    st.image("img\google.jpg")




#Funcion para una animación
def load_lottieurl1(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding=load_lottieurl1("https://lottie.host/9cc851b8-8943-449d-a80a-4a114a9dc43f/9H9ksfnTcH.json")
st_lottie(lottie_coding,height=300,key="coding1")








































