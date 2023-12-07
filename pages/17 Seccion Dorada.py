import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def busqueda_seccion_dorada(func, xl, xu, tol):
    x = sp.symbols('x')
    f = func
    R = (np.sqrt(5) - 1) / 2

    error = tol + 1
    it = 1
    x0 = (xl + xu) / 2

    columnas = ['xl', 'xu', 'x1', 'x2', 'f(x1)', 'f(x2)', 'x0', 'error(%)']
    tabla = pd.DataFrame(columns=columnas)

    while error > tol:
        d = R * (xu - xl)
        x1 = xl + d
        x2 = xu - d

        fx1 = round(f.subs({x: x1}), 4)
        fx2 = round(f.subs({x: x2}), 4)

        error = (1 - R) * np.abs((xu - xl) / x0) * 100

        if fx1 > fx2:
            xl, x2, x0, x1 = x2, x1, x1, xl + d
        elif fx1 < fx2:
            xu, x1, x0, x2 = x1, x2, x2, xu - d

        data = {'xl': [xl], 'xu': [xu], 'x1': [x1], 'x2': [x2], 'f(x1)': [fx1], 'f(x2)': [fx2], 'x0': [x0], 'error(%)': [round(error, 2)]}
        tabla = pd.concat([tabla, pd.DataFrame(data=data)], ignore_index=True)

        it += 1

    return tabla

def plot_seccion_dorada(func, tabla_resultados):
    x_vals = np.linspace(tabla_resultados['xl'].min(), tabla_resultados['xu'].max(), 100)
    y_vals = [float(func.subs('x', val)) for val in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='Función')
    ax.scatter(tabla_resultados['x1'], tabla_resultados['f(x1)'], color='red', label='Puntos evaluados (x1)')
    ax.scatter(tabla_resultados['x2'], tabla_resultados['f(x2)'], color='green', label='Puntos evaluados (x2)')

    ax.set_title("$2 \\sin(x) - \\frac{x^2}{10}$")
    ax.vlines(x=tabla_resultados['x0'], ymin=0, ymax=tabla_resultados['f(x1)'], color='orange', linestyle='--')
    ax.vlines(x=tabla_resultados['x1'], ymin=0, ymax=tabla_resultados['f(x1)'], color='r', linestyle='--', label="$x_1$")
    ax.vlines(x=tabla_resultados['x2'], ymin=0, ymax=tabla_resultados['f(x2)'], color='purple', linestyle='--', label="$x_2$")
    
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    st.pyplot(fig)

st.title("Método de la Sección Dorada")

expr_str = st.text_input("Ingrese la función en términos de x:")
x = sp.symbols('x')
f = sp.sympify(expr_str)

# Valores iniciales y tolerancia
xl_inicial = st.number_input("Ingrese el valor de xl:")
xu_inicial = st.number_input("Ingrese el valor de xu:")
tolerancia = st.number_input("Ingrese la tolerancia:")

resultados = busqueda_seccion_dorada(f, xl_inicial, xu_inicial, tolerancia)
st.write("Resultados:")
st.dataframe(resultados)

plot_seccion_dorada(f, resultados)
