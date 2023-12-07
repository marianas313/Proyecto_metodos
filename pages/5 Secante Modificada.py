import streamlit as st
import pandas as pd
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.numbers import NaN

# Inicializar variables
x = sp.symbols('x')

# Función de Secante Modificada
def secante_modificada(y1, x0, delta, tole, ite):
    x = sp.symbols('x')

    y = sp.sympify(y1)
    deltaX = delta
    xi = x0

    columnas = ['Iteración', 'xi', 'xi+1', 'fxi+deltaX', 'fxi', 'xi+delta', 'er(%)']
    tabla = pd.DataFrame(columns=columnas)

    tol = tole
    er = tol + 1
    it = 1

    r = np.linspace(-1, 5, 100)

    fig, ax = plt.subplots()

    ax.plot(r, [y.subs({x: x_i}) for x_i in r], color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min([y.subs({x: xi}) for xi in r]) - 0.1, ymax=max([y.subs({x: xi}) for xi in r]) + 0.1, color='k')
    ax.hlines(y=0, xmin=min(r) - 0.1, xmax=max(r) + 0.1, color='k')
    ax.grid()

    # Placeholder para la gráfica en Streamlit
    fig_placeholder = st.pyplot(fig)

    # Placeholder para la tabla en Streamlit
    table_placeholder = st.empty()

    while er > tol and er!=NaN:
        fxi_1 = round(y.subs({x: xi}), 4)
        fxi = round(y.subs({x: xi + deltaX}), 4)

        ax.clear()
        ax.plot(r, [y.subs({x: x_i}) for x_i in r], color='blue', label=f"${sp.latex(y)}$")
        ax.vlines(x=0, ymin=min([y.subs({x: xi}) for xi in r]) - 0.1, ymax=max([y.subs({x: xi}) for xi in r]) + 0.1, color='k')
        ax.hlines(y=0, xmin=min(r) - 0.1, xmax=max(r) + 0.1, color='k')
        ax.grid()
        xx=round( xi+deltaX, 4)
        xi_2 = round(xi - ((fxi_1 * deltaX) / (fxi - fxi_1)), 4)

        ax.plot([xi], [fxi_1], color='red', marker='o', label=f'$(x_{it-1},f(x_{it-1}))= ({xi},{fxi_1})')
        ax.plot([xi + deltaX], [fxi], color='red', marker='x', label=f'$(x_{it},f(x_{it}))= ({xi + deltaX},{fxi})')
        ax.plot([xi_2], [0], color='red', marker='o', label=f'$(x_{it+1},0) = ({xi_2},0)$')

        ax.set_title(label=f"${sp.latex(y)}$")
        ax.legend()

        # Actualizar el placeholder en Streamlit para la gráfica
        fig_placeholder.pyplot(fig)

        # Actualizar el placeholder en Streamlit para la tabla
        nueva_fila = {'Iteración': it, 'xi': xi, 'xi+1': xi + deltaX, 'fxi+deltaX': fxi, 'fxi': fxi_1,
                      'xi+delta': xi + deltaX, 'er(%)': round(er, 4)}
        nueva_fila = pd.DataFrame([nueva_fila])
        tabla = pd.concat([tabla, nueva_fila], ignore_index=True)
        table_placeholder.table(tabla)

        er = np.abs((xi_2 - xi) / xi_2) * 100
        it += 1
        xi=xi+deltaX
        xi = xi_2

    st.write(f"El error final es: {er}")
    st.write(f"La raíz está en: {xi}")

# Interfaz de usuario con Streamlit
st.title("Método de Secante Modificada")

# Ingresar la función, punto inicial, delta, tolerancia y número de iteraciones
Funcion_secante = st.text_input("Ingrese la función con la que desea trabajar:", '-x+2.71**(-x)')
punto_inicial_secante = st.number_input("Ingrese el punto inicial (xi):", value=0)
delta_secante = st.number_input("Ingrese el valor de delta:", value=0.1)
tolerancia_secante = st.number_input("Ingrese el valor de la tolerancia:", value=0.001)
iteraciones_secante = st.number_input("Ingrese el número máximo de iteraciones:", value=6)

# Ejecutar el método de Secante Modificada al presionar un botón
if st.button("Calcular Secante Modificada"):
    secante_modificada(Funcion_secante, punto_inicial_secante, delta_secante, tolerancia_secante, iteraciones_secante)