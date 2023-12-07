import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def punto_fijo(g, x0, tol, it_max):
    x = sp.symbols('x')
    gx = sp.sympify(g)

    xi = x0
    error = tol + 1
    i = 0
    tabla = []

    st.title('Método del Punto Fijo')

    # Placeholder para la gráfica en Streamlit
    fig, ax = plt.subplots()
    fig_placeholder = st.pyplot(fig)

    while error > tol and i < it_max:
        gi = gx.subs({x: xi})
        error = abs((gi - xi) / gi) * 100
        i += 1
        tabla.append([i, error, gi, xi])

        # Plotting the function
        x_vals = np.linspace(min(float(xi.evalf()), float(gi.evalf())) - 1, max(float(xi.evalf()), float(gi.evalf())) + 1, 100)
        y_vals = sp.lambdify(x, gx)(x_vals)

        # Plotting the iteration points
        ax.plot(x_vals, y_vals, label=f"${sp.latex(gx)}$")
        ax.scatter(float(xi.evalf()), float(gi.evalf()), color='red', label=f'Iteración {i}')

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Método del Punto Fijo')
        ax.legend()
        ax.grid(True)

        # Actualizar el placeholder en Streamlit para la gráfica
        fig_placeholder.pyplot(fig)

        st.text(f"Iteración: {i}, Error: {error:.4f}, xi: {float(xi.evalf()):.4f}, gi: {float(gi.evalf()):.4f}")
        st.text("-----------------------------")

        # Añadir un pequeño retraso entre iteraciones para dar tiempo a la interfaz de Streamlit para actualizar
        st.experimental.sleep(1)

        # Limpiar la figura para la próxima iteración
        ax.clear()

        xi = gi

    tabla = np.array(tabla)
    df = pd.DataFrame(tabla, columns=['Iteraciones', 'Error', 'gi', 'xi'])

    # Mostrar la tabla completa al finalizar las iteraciones
    st.dataframe(df)

    return df

# Interfaz de usuario con Streamlit
st.sidebar.title('Parámetros')
funcion = st.sidebar.text_input("Ingrese la función g(x):", 'x*exp(-x**2)')
limite_1 = st.sidebar.number_input("Ingrese el valor inicial x0:", value=-0.6)
tolerancia = st.sidebar.number_input("Ingrese la tolerancia:", value=0.1)
itera_max = st.sidebar.number_input("Ingrese el número máximo de iteraciones:", value=1000)

# Botón para ejecutar el método del punto fijo
if st.sidebar.button("Calcular Punto Fijo"):
    tabla = punto_fijo(funcion, limite_1, tolerancia, itera_max)
