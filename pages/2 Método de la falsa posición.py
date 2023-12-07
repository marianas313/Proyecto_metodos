import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Inicializar variables
x = sp.symbols('x')

# Función de falsa posición
def falsaposicion(y1, xl, xu, tol):
    y = sp.sympify(y1)
    f = sp.lambdify(x, y)
    xr=None
    error = tol + 1
    xr_ant = xl
    it = 1

    columnas = ['Iteración', 'Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
    tabla1 = pd.DataFrame(columns=columnas)

    r = np.linspace(xl - 0.5, xu + 0.5, 100)
    fx = [y.subs({x: xi}) for xi in r]

    fig, ax = plt.subplots()

    ax.plot(r, f(r), color='blue', label=f"${sp.latex(y)}$")
    
    ax.vlines(x=0, ymin=round(min(f(r)), 4) - 0.5, ymax=round(max(f(r)), 4) + 0.5, color='k')
    ax.hlines(y=0, xmin=round(min(r), 4) - 0.5, xmax=round(max(r), 4) + 0.5, color='k')
    ax.grid()

    # Placeholder para la gráfica en Streamlit
    fig_placeholder = st.pyplot(fig)

    # Placeholder para la tabla en Streamlit
    table_placeholder = st.empty()

    while error > tol:
        # Evaluamos la función en los puntos del intervalo.
        xr = round(((f(xl) * xu) - (f(xu) * xl)) / (f(xl) - f(xu)), 4)
        if (f(xl) * f(xr)) < 0:
            xu = xr
        elif (f(xl) * f(xr)) > 0:
            xl = xr
        elif (f(xl) * f(xr)) == 0:
            print(f"Terminé")
            break

        error = round(np.abs((xr - xr_ant) / (xr_ant)) * 100, 4)

        nueva_fila = {'Iteración': it, 'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': f(xl), 'f(Xu)': f(xu), 'f(Xr)': f(xr)}
        nueva_fila = pd.DataFrame([nueva_fila])

        tabla1 = pd.concat([tabla1, nueva_fila], ignore_index=True)

        # Limpiar la gráfica y mostrar la tabla
        ax.clear()
        ax.plot(r, f(r), color='blue', label=f"${sp.latex(y)}$")
        ax.vlines(x=0, ymin=round(min(f(r)), 4) - 0.5, ymax=round(max(f(r)), 4) + 0.5, color='k')
        ax.hlines(y=0, xmin=round(min(r), 4) - 0.5, xmax=round(max(r), 4) + 0.5, color='k')
        ax.grid()

        # Agregar solo los puntos de la iteración actual
        ax.plot(xr, f(xr), 'ro', label='Raíz')
        ax.legend()

        # Actualizar el placeholder en Streamlit para la gráfica
        fig_placeholder.pyplot(fig)

        # Actualizar el placeholder en Streamlit para la tabla
        table_placeholder.table(tabla1)
        
        xr_ant=xr
        it += 1

    # Marcador para la raíz
    ax.plot(xr, f(xr), 'ro', label='Raíz')
    ax.legend()

    return tabla1, y, x, xr, error, fig

# Interfaz de usuario con Streamlit
st.title("Método de Falsa Posición")

# Ingresar la función, límites y tolerancia
Funcion = st.text_input("Ingrese la función con la que desea trabajar:", 'exp(x) - x * cos(x) - 2')
limite_1 = st.number_input("Ingrese el valor de xl:", value=-4.0)
limite_2 = st.number_input("Ingrese el valor de xu:", value=2.0)
tolerancia = st.number_input("Ingrese el valor de la tolerancia:", value=0.001)

# Ejecutar el método de falsa posición al presionar un botón
if st.button("Calcular Falsa Posición"):
    tabla1, y, x, xf, error, fig = falsaposicion(Funcion, limite_1, limite_2, tolerancia)

    st.success(f"El error final es: {error}%")
    st.success(f"La raíz está en: ({xf},{y.subs({x: xf})})")
