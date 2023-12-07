import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Interfaz de usuario con Streamlit
st.title("Método de Euler - Streamlit")

# Entrada de la función en formato de cadena
Funcion = st.text_input("Ingrese la función dy/dt:", "t**2")
dy = sp.sympify(Funcion)

# Parámetros
condicion_i = st.number_input("Ingrese la condición inicial y0:", value=0.0)
tiempo_i = st.number_input("Ingrese el tiempo inicial ti:", value=0.0)
paso_i = st.number_input("Ingrese el paso de integración h:", value=0.1)
tiempo_f = st.number_input("Ingrese el tiempo final tf:", value=1.0)

# Botón para ejecutar el método de Euler
if st.button("Calcular Método de Euler"):
    # Definimos los vectores donde almacenaremos el resultado.
    t = sp.symbols('t')
    x = np.arange(tiempo_i, tiempo_f + paso_i, paso_i)
    y = np.empty_like(x)
    y[0] = condicion_i
    columnas = ['it', 't', 'yi', 'yi+1']
    tabla = pd.DataFrame(columns=columnas)

    # Calcular los valores.
    for i in range(0, len(y)-1):
        y[i+1] = y[i] + paso_i * dy.subs({t: x[i]})
        nueva_fila = pd.DataFrame(data={'it': [i+1], 't': [round(x[i], 2)], 'yi': [round(y[i], 2)], "yi+1": [round(y[i+1], 2)]})
        tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

    # Mostrar la tabla
    st.dataframe(tabla)

    # Graficar los resultados
    plt.figure()
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(x, y, marker='o', label="Método Euler")
    ax.plot(x, sp.lambdify(t, dy)(x), label="Real")
    ax.legend()
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Método de Euler vs Real')
    st.pyplot(plt)
