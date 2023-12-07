import streamlit as st
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

st.title("Método de Splines Cubicos")

# Subir archivo CSV
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

# Verificar si se cargó un archivo CSV
if uploaded_file is not None:
    # Leer datos desde el archivo CSV
    data = pd.read_csv(uploaded_file)

    # Obtener las columnas X e Y
    x_valores = data["X"].values
    y_valores = data["Y"].values

    # Esta función nos permite reducir el código y optimizarlo
    # pues nos permite calcular los splines cúbicos
    cs = CubicSpline(x_valores, y_valores)

    # Creamos un rango de valores para x
    x_rango = np.linspace(min(x_valores), max(x_valores), 400)

    # Nos permite calcular los valores correspondientes en y
    y_rango = cs(x_rango)

    # Imprimimos los polinomios
    for i, coef in enumerate(cs.c):
        if i == len(cs.c) - 1:
            st.write(f"Para el intervalo [{x_valores[i]}, {x_valores[i+1]}]:")
            st.write(f"S(x) = {coef[0]:.4f} + {coef[1]:.4f}(x - {x_valores[i]:.4f}) + {coef[2]:.4f}(x - {x_valores[i]:.4f})^2")
            st.write()
        else:
            st.write(f"Para el intervalo [{x_valores[i]}, {x_valores[i+1]}]:")
            st.write(f"S(x) = {coef[0]:.4f} + {coef[1]:.4f}(x - {x_valores[i]:.4f}) + {coef[2]:.4f}(x - {x_valores[i]:.4f})^2 + {coef[3]:.4f}(x - {x_valores[i]:.4f})^3")
            st.write()

    # Graficamos los datos originales y la interpolación cúbica
    fig, ax = plt.subplots()
    ax.plot(x_valores, y_valores, 'o', label='datos')
    ax.plot(x_rango, y_rango, label='Interpolación')
    ax.set_title('Interpolación cúbica con splines')
    ax.grid(True)
    ax.legend()

    # Mostramos la gráfica en la interfaz de Streamlit
    st.pyplot(fig)