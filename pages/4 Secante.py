import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Inicializar variables
x = sp.symbols('x')

# Función de la secante
def secante(Funcion, x0, x1, tolerancia):
    y = sp.sympify(Funcion)

    xi_2 = x0
    xi = x1

    columnas = ['xi', 'xi+1', 'f(xi)', 'xi-1', 'f(xi-1)', 'er(%)']
    tabla = pd.DataFrame(columns=columnas)

    er = tolerancia + 1
    it = 1
    r = np.linspace(xi_2, xi, 100)

    fig, ax = plt.subplots()

    # Placeholder para la gráfica en Streamlit
    fig_placeholder = st.pyplot(fig)

    # Placeholder para la tabla en Streamlit
    table_placeholder = st.empty()

    while er > tolerancia:
        fxi_2 = round(y.subs({x: xi_2}), 4)
        fxi = round(y.subs({x: xi}), 4)

        ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")

        ax.vlines(x=0, ymin=min(fx) - 0.1, ymax=max(fx) + 0.1, color='k')
        ax.hlines(y=0, xmin=min(r) - 0.1, xmax=max(r) + 0.1, color='k')
        ax.plot([xi_2], [fxi_2], color='red', marker='o', label=f'$(x_{it-1},f(x_{it-1}))= ({xi_2},{fxi_2})')
        ax.plot([xi], [fxi], color='red', marker='x', label=f'$(x_{it},f(x_{it}))= ({xi},{fxi})')

        # Aproximación de la pendiente
        dfxi = round((fxi - fxi_2) / (xi - xi_2), 4)

        xi_3 = round(xi - (fxi / dfxi), 4)

        ax.plot([xi_2], [0], color='red', marker='o', label=f'$(x_{it+1},0) = ({xi_3},0)$')

        ax.set_title(f"${sp.latex(y)}$")
        ax.grid()
        ax.legend()
        plt.show()

        er = np.abs((xi_3 - xi) / xi_3) * 100

        fig_placeholder.pyplot(fig)

        nueva_fila = {'xi': xi, 'xi+1': xi_3, 'f(xi)': fxi, 'xi-1': xi_2, 'f(xi-1)': fxi_2, 'er(%)': round(er, 4)}
        nueva_fila = pd.DataFrame([nueva_fila])
        tabla = pd.concat([tabla, nueva_fila], ignore_index=True)
        
        table_placeholder.table(tabla)

        it += 1
        xi_2 = xi
        xi = xi_3

    return tabla, xi_3, er

# Interfaz de usuario con Streamlit
st.title("Método de la Secante")

# Ingresar la función, valores iniciales y tolerancia
Funcion_sec = st.text_input("Ingrese la función con la que desea trabajar (Secante):", 'exp(x) - x * cos(x) - 2')
x0_sec = st.number_input("Ingrese el valor de x0 (Secante):", value=-4.0)
x1_sec = st.number_input("Ingrese el valor de x1 (Secante):", value=2.0)
tolerancia_sec = st.number_input("Ingrese el valor de la tolerancia (Secante):", value=0.001)

# Ejecutar el método de la secante al presionar un botón
if st.button("Calcular Secante"):
    tabla_sec, xs_sec, error_sec = secante(Funcion_sec, x0_sec, x1_sec, tolerancia_sec)
    st.table(tabla_sec)
    st.success(f"El error final es: {error_sec}%")
    st.success(f"La raíz está en: ({xs_sec})")
