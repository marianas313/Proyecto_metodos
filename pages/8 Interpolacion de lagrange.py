import streamlit as st
import pandas as pd
import numpy as np
from sympy import symbols, lambdify, simplify
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Interpolación de Lagrange')

# Crear espacio para subir el archivo CSV
uploaded_file = st.file_uploader("Subir archivo CSV", type=["csv"])

# Verificar si se ha subido un archivo
if uploaded_file is not None:
    # Leer el archivo CSV
    data = pd.read_csv(uploaded_file)
    df = pd.DataFrame(data)

    x_values = np.array(df["X"])
    y_values = np.array(df["Y"])

    x = symbols('x')
    Px = 0  # Inicializamos el polinomio interpolante

    for i in range(len(x_values)):
        Li = 1
        for j in range(len(x_values)):
            if i != j:
                Li *= (x - x_values[j]) / (x_values[i] - x_values[j])
        Px += y_values[i] * Li

    # Simplificamos el polinomio
    Px_simpli = simplify(Px)

    # Creamos una función numérica a partir del polinomio simplificado
    Px_lambda = lambdify(x, Px_simpli, "numpy")

    # Crear un rango de valores para x
    x_range = np.linspace(min(x_values), max(x_values), 400)

    # Calcular los valores correspondientes en y
    y_range = Px_lambda(x_range)

    # Graficar los datos originales y el polinomio interpolado
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, 'ro', label='Datos')
    ax.plot(x_range, y_range, label='Interpolación de Lagrange')
    ax.set_title('Interpolación de Lagrange')
    ax.grid(True)
    ax.legend()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

