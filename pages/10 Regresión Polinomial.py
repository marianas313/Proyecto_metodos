import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Regresión Polinomial')

# Crear espacio para cargar el archivo CSV
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo CSV
    data = pd.read_csv(uploaded_file)

    # Mostrar los datos del archivo cargado
    st.write("Datos del archivo cargado:")
    st.write(data)

    # Extraer los datos de x e y
    x_valores = np.array(data["X"])
    y_valores = np.array(data["Y"])

    # Pedir al usuario el grado de regresión
    grado = st.number_input("Ingrese el grado de regresión:", min_value=1, value=1)

    # Realizar la regresión polinomial
    coe = np.polyfit(x_valores, y_valores, grado)
    poli = np.poly1d(coe)

    # Crear un rango de valores para x
    x_rango = np.linspace(min(x_valores), max(x_valores), 400)

    # Calcular los valores correspondientes en y
    y_rango = poli(x_rango)

    # Graficamos los datos originales y la interpolación cúbica
    fig, ax = plt.subplots()
    ax.plot(x_valores, y_valores, 'o', label='datos')
    ax.plot(x_rango, y_rango, label=f'Regresión de grado {grado}')
    ax.set_title(f'Regresión polinomial de grado {grado}')
    ax.grid(True)
    ax.legend()


    # Mostramos la gráfica en la interfaz de Streamlit
    st.pyplot(fig)