import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Análisis de optimos")
expr_str = st.text_input("Ingrese la función en términos de x:")
x = sp.symbols('x')

if expr_str:
    f = sp.sympify(expr_str)

    # Calcular la primera derivada
    f_prime = sp.diff(f, x)

    # Encontrar los puntos críticos resolviendo f'(x) = 0
    puntos_criticos = sp.solve(f_prime, x)

    # Calcular la segunda derivada
    f_doble_prime = sp.diff(f_prime, x)

    # Determinar la naturaleza de los puntos críticos
    naturaleza_puntos_criticos = []
    for punto in puntos_criticos:
        if f_doble_prime.subs(x, punto) > 0:
            naturaleza = "mínimo"
        elif f_doble_prime.subs(x, punto) < 0:
            naturaleza = "máximo"
        else:
            naturaleza = "inconclusivo"
        naturaleza_puntos_criticos.append(naturaleza)

    # Mostrar los resultados
    st.subheader("Resultados:")
    st.write(f"Puntos críticos: {puntos_criticos}")
    st.write(f"Naturaleza de los puntos críticos: {naturaleza_puntos_criticos}")

    # Graficar la función y sus puntos críticos
    f_lambda = sp.lambdify(x, f, "numpy")
    valores_x = np.linspace(float(min(puntos_criticos)) - 2, float(max(puntos_criticos)) + 2, 400)
    valores_y = f_lambda(valores_x)

    st.subheader("Gráfico:")
    # st.pyplot(plt.figure(figsize=(10, 6)))
    plt.plot(valores_x, valores_y, label=str(f), color='blue')
    for punto, naturaleza in zip(puntos_criticos, naturaleza_puntos_criticos):
        plt.scatter(punto, f.subs(x, punto), color='red')
        plt.text(punto, f.subs(x, punto), f'{punto}: {naturaleza}')

    plt.title("Función y sus puntos críticos")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    st.pyplot(plt)