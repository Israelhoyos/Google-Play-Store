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


st.image("img\ML.png", width=800)
st.markdown("---")
st.markdown("""
**Es una rama de la inteligencia artificial, para mi se basa en algoritmos que pueden aprender de los datos sin depender de la programación basada en reglas.**

            """)
st.code("""
#MODELO KNN

# Dividir los datos en características (X) y etiquetas (y)
X = df2.drop('App Name', axis=1)
y = df2['Installs']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador KNN
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo
knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo: {:.2f}%".format(accuracy * 100))       
        """)
st.markdown("Precisión del modelo: 91.87%")
st.markdown("---")

st.code("""
#MODELO SVM

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
# Cargar el conjunto de datos de ejemplo
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Crear un clasificador SVM
clf = svm.SVC(kernel='linear')

# Entrenar el clasificador utilizando el conjunto de entrenamiento
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = clf.score(X_test, y_test)
print("Precisión del modelo:", accuracy)      
        """)
st.markdown("Precisión del modelo: 0.9777777777777777")
st.markdown("---")

st.code("""
#Random Forest


# Dividir los datos en características (X) y etiquetas (y)
X = df2.drop('App Name', axis=1)
y = df2['Installs']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo: {:.2f}%".format(accuracy * 100))     
        """)
st.markdown("Precisión del modelo: 100.00%")

st.markdown("")
st.markdown("")
st.markdown("""Es un algoritmo de aprendizaje supervisado, puede usarse
en problemas de regresión y clasificación, este modelo se basa
en la combinación de múltiples árboles de decisión independientes
para tomar decisiones finales.""")
st.markdown("")
st.image("img\MachineL.png")
st.markdown("")
st.markdown("""
+ Mi objetivo principal era localizar el modelo más eficaz para poder llevar a cabo un entrenamiento de los datos.
+ Tiene una mayor efectividad a la hora de manejar gran flujo de datos.
            """)

