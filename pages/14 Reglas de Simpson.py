import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

st.markdown('## Reglas de Simpson')
# Entrada de los límites y la función
a = st.number_input("Ingrese el límite inferior a:", value=1)
b = st.number_input("Ingrese el límite superior b:", value=6)
fx_input = st.text_input("Ingrese la función f(x):", "x * sin(x) + 3 * x - 1")
tabs= st.tabs(['Simpson 1/3','Simpson 3/8'])
with tabs[0]:

    # Interfaz de usuario con Streamlit
    st.title("Regla de Simpson 1/3")

    # Definir la variable simbólica x y la función simbólica fx
    x = sp.symbols('x')
    fx = sp.sympify(fx_input)

    # Evaluar la función en a, b y m
    fa = fx.subs(x, a)
    fb = fx.subs(x, b)
    m = (a + b) / 2
    fm = fx.subs(x, m)

    st.write(f"f(a) = {fa} \nf(b) = {fb} \nf(m) = {fm:.2f}")

    # Aplicar la regla de Simpson 1/3
    I = (b - a) * ((fa + 4 * fm + fb) / 6)
    st.write(f"I = {I} U^2")

    # Calcular la integral real usando sympy
    I_real = sp.integrate(fx, (x, a, b))
    st.write("La integral por sympy es:", I_real)

    # Calcular el error relativo
    error = abs((I_real - I) / I_real) * 100
    st.write(f"El error relativo es: {error:.2f}%")

    # Crear gráfica
    x_values = np.linspace(0, b, 100)
    y_values = [fx.subs(x, val) for val in x_values]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, color='blue', label='f(x)')
    ax.grid()

    # Plano cartesiano (Ejes)
    ax.vlines(x=0, ymin=0, ymax=max(y_values), color='k')
    ax.hlines(y=0, xmin=0, xmax=b, color='k')

    # Límites xl y xu
    ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')

    ax.fill([a, a, m, b, b], [0, fa, fm, fb, 0], 'r', alpha=0.2)

    plt.grid(True)
    plt.legend()

    # Mostrar gráfica en Streamlit
    st.pyplot(fig)



with tabs[1]:

    # Función para la regla de Simpson 3/8
    def simpsons_3_8_rule(a, b, n, func):
        x = sp.symbols('x')
        fx = sp.sympify(func)

        h = (b - a) / n
        terms = [3 * fx.subs(x, a + i * h) for i in range(1, n, 3)]
        terms += [3 * fx.subs(x, a + i * h) for i in range(2, n - 2, 3)]
        terms += [2 * fx.subs(x, a + i * h) for i in range(3, n - 3, 3)]

        I = (3 * h / 8) * (fx.subs(x, a) + sum(terms) + fx.subs(x, b))

        return I

    # Interfaz de usuario con Streamlit
    st.title("Regla de Simpson 3/8")

    # Entrada del número de segmentos
    n = st.number_input("Ingrese el número de segmentos n:", value=4, step=3)

    # Calcular la integral con la regla de Simpson 3/8
    I_approx = simpsons_3_8_rule(a, b, n, fx_input)
    st.write(f"La integral aproximada es: {I_approx}")

    # Crear gráfica
    x_values = np.linspace(a, b, 100)
    y_values = [sp.lambdify('x', fx_input)(val) for val in x_values]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, color='blue', label='f(x)')
    ax.grid()

    # Plano cartesiano (Ejes)
    ax.vlines(x=0, ymin=0, ymax=max(y_values), color='k')
    ax.hlines(y=0, xmin=a, xmax=b, color='k')

    # Límites xl y xu
    ax.vlines(x=a, ymin=0, ymax=sp.lambdify('x', fx_input)(a), color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=sp.lambdify('x', fx_input)(b), color='r', linestyle='--')

    # Área bajo la curva
    x_fill = np.linspace(a, b, 100)
    y_fill = [sp.lambdify('x', fx_input)(val) for val in x_fill]
    ax.fill_between(x_fill, y_fill, color='r', alpha=0.2, label='Área bajo la curva')

    plt.grid(True)
    plt.legend()

    # Mostrar gráfica en Streamlit
    st.pyplot(fig)
