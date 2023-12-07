import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import time
# Función de bisección
def biseccion(y1, xl, xu, tol):
    x = sp.symbols('x')
    y = sp.sympify(y1)

    xr = None
    xr_ant = xu
    error = tol + 1
    it = 1

    columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
    tabla1 = pd.DataFrame(columns=columnas)

    r = np.linspace(xl - 0.5, xu + 0.5, 100)
    fx = [y.subs({x: xi}) for xi in r]

    fig, ax = plt.subplots()
    line, = ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")

    # Agregar título a la gráfica
    ax.set_title(f'Gráfica de la Función: ${sp.latex(y)}$')

    ax.vlines(x=0, ymin=round(min(fx), 4) - 0.5, ymax=round(max(fx), 4) + 0.5, color='k')
    ax.hlines(y=0, xmin=round(min(r), 4) - 0.5, xmax=round(max(r), 4) + 0.5, color='k')

    ax.grid()

    # Placeholder para la gráfica en Streamlit
    fig_placeholder = st.pyplot(fig)
    
    # Placeholder para la tabla en Streamlit
    table_placeholder = st.empty()

    while error > tol:
        fxl = round(y.subs({x: xl}), 4)
        fxu = round(y.subs({x: xu}), 4)

        xr = round((xl + xu) / 2, 4)
        fxr = round(y.subs({x: xr}), 4)

        error = np.abs((xr - xr_ant) / xr) * 100

        nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
        nueva_fila = pd.DataFrame([nueva_fila])

        tabla1 = pd.concat([tabla1, nueva_fila], ignore_index=True)

        if (fxl * fxr) < 0:
            xu = xr
        elif (fxl * fxr) > 0:
            xl = xr

        xr_ant = xr
        it += 1

        # Limpiar la gráfica
        ax.clear()
        ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
        ax.set_title(f'Gráfica de la Función: ${sp.latex(y)}$')
        ax.vlines(x=0, ymin=round(min(fx), 4) - 0.5, ymax=round(max(fx), 4) + 0.5, color='k')
        ax.hlines(y=0, xmin=round(min(r), 4) - 0.5, xmax=round(max(r), 4) + 0.5, color='k')
        ax.grid()

        # Agregar solo los puntos de la iteración actual
        ax.plot(xr, fxr, 'ro', label='Raíz')
        ax.legend()

        # Actualizar el placeholder en Streamlit para la gráfica
        fig_placeholder.pyplot(fig)

        # Actualizar el placeholder en Streamlit para la tabla
        table_placeholder.table(tabla1)

        # Añadir un pequeño retraso entre iteraciones para dar tiempo a la interfaz de Streamlit para actualizar
        time.sleep(0.5)

    # Marcador para la raíz
    ax.plot(xr, fxr, 'ro', label='Raíz')
    ax.legend()

    return tabla1, y, x, xr, error, fig

# Interfaz de usuario con Streamlit
st.title("Método de Bisección")

# Ingresar la función, límites y tolerancia
Funcion = st.text_input("Ingrese la función con la que desea trabajar:")
limite_1 = st.number_input("Ingrese el valor de xl:", value=-0.0)
limite_2 = st.number_input("Ingrese el valor de xu:", value=0.0)
tolerancia = st.number_input("Ingrese el valor de la tolerancia:", value=0.001)

# Ejecutar el método de bisección al presionar un botón
if st.button("Calcular Bisección"):
    tabla1, y, x, xf, error, fig = biseccion(Funcion, limite_1, limite_2, tolerancia)

    st.success(f"El error final es: {error}%")
    st.success(f"La raíz está en: ({xf},{y.subs({x: xf})})")


