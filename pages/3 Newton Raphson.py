import streamlit as st
import pandas as pd
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Función de Newton-Raphson
def newton_raphson(y1, xii, tole):
    x = sp.symbols('x')

    y = sp.sympify(y1)
    xi = xii

    columnas = ['Iteración', 'xi', 'Xi+1', 'f(xi)', "f'(Xi)", 'er(%)']
    tabla = pd.DataFrame(columns=columnas)

    tol = tole
    er = tol + 1
    it = 1

    r = np.linspace(xi - 1.5, xi + 10, 100)

    fig, ax = plt.subplots()
    fx = [y.subs({x:x_i}) for x_i in r]

    ax.plot(r,fx,color='blue',label=f"${sp.latex(y)}$")

    ax.vlines(x=0, ymin=min([y.subs({x: xi}) for xi in r]) - 0.1, ymax=max([y.subs({x: xi}) for xi in r]) + 0.1, color='k')
    ax.hlines(y=0, xmin=min(r) - 0.1, xmax=max(r) + 0.1, color='k')
    ax.grid()

    # Placeholder para la gráfica en Streamlit
    fig_placeholder = st.pyplot(fig)

    # Placeholder para la tabla en Streamlit
    table_placeholder = st.empty()

    while er > tol:
        fxi = round(y.subs({x: xi}), 4)

        ax.clear()
        ax.plot(r, [y.subs({x: x_i}) for x_i in r], color='blue', label=f"${sp.latex(y)}$")
        ax.vlines(x=0, ymin=min([y.subs({x: xi}) for xi in r]) - 0.1, ymax=max([y.subs({x: xi}) for xi in r]) + 0.1, color='k')
        ax.hlines(y=0, xmin=min(r) - 0.1, xmax=max(r) + 0.1, color='k')
        ax.grid()

        dy = y.diff()
        dfxi = round(dy.subs({x: xi}), 4)
        xs = round(xi - ((fxi) / (dfxi)), 4)

        ax.plot([xi], [fxi], color='red', marker='o', label=f'$(x_{it},f(x_{it}))= ({xi},{fxi})$')
        ax.plot([xs], [0], color='red', marker='x', label=f'$(x_{it+1},0) = ({xs},0)$')
        ax.plot(r, [dy.subs({x: xi})*(x_i - xi) + fxi for x_i in r], color='purple', linestyle='--', label=f"${sp.latex(dy)}$")

        ax.set_title(label=f"${sp.latex(y)}$")
        ax.legend()

        # Actualizar el placeholder en Streamlit para la gráfica
        fig_placeholder.pyplot(fig)

        # Actualizar el placeholder en Streamlit para la tabla
        nueva_fila = {'Iteración': it, 'xi': xi, 'Xi+1': xs, 'f(xi)': fxi, "f'(Xi)": dfxi, 'er(%)': round(er, 4)}
        nueva_fila = pd.DataFrame([nueva_fila])
        tabla = pd.concat([tabla, nueva_fila], ignore_index=True)
        table_placeholder.table(tabla)

        er = np.abs((xs - xi) / xs) * 100
        it += 1
        xi = xs


    st.success(f"El error final es: {er}")
    st.success(f"La raíz está en: {xs}")

# Interfaz de usuario con Streamlit
st.title("Método de Newton-Raphson")

# Ingresar la función, límite inicial y tolerancia
Funcion = st.text_input("Ingrese la función con la que desea trabajar:", 'x*exp(-x**2)')
limite_1 = st.number_input("Ingrese el valor inicial (xi):", value=-0.6)
tolerancia = st.number_input("Ingrese el valor de la tolerancia:", value=0.0001)

# Ejecutar el método de Newton-Raphson al presionar un botón
if st.button("Calcular Newton-Raphson"):
    newton_raphson(Funcion, limite_1, tolerancia)