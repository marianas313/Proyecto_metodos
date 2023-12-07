import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

st.markdown('## Reglas de Simpson')
tabs= st.tabs(['Simpson 1/3','Simpson 3/8'])
with tabs[0]:
    def simpsons_rule(a, b, n, func):
        x = sp.symbols('x')
        fx = sp.sympify(func)

        h = (b - a) / n
        odd_terms = [4 * fx.subs(x, a + i * h) for i in range(1, n, 2)]
        even_terms = [2 * fx.subs(x, a + i * h) for i in range(2, n - 1, 2)]

        I = (h / 3) * (fx.subs(x, a) + sum(odd_terms) + sum(even_terms) + fx.subs(x, b))

        return I

    # Interfaz de usuario con Streamlit
    st.title("Regla de Simpson 1/3")

    # Entrada de los límites y número de intervalos
    a = st.number_input("Ingrese el límite inferior a:", value=1)
    b = st.number_input("Ingrese el límite superior b:", value=2)
    n = st.number_input("Ingrese el número de intervalos n:", value=4, step=2)

    # Entrada de la función
    func = st.text_input("Ingrese la función f(x):", "x**2")

    # Calcular la integral con la regla de Simpson 1/3
    try:
        I_approx = simpsons_rule(a, b, n, func)
        st.write(f"La integral aproximada es: {I_approx}")

        # Calcular la integral real usando sympy
        x = sp.symbols('x')
        fx = sp.sympify(func)
        I_real = sp.integrate(fx, (x, a, b))
        st.write(f"La integral real por sympy es: {I_real}")

        # Calcular el error relativo
        error = abs((I_real - I_approx) / I_real) * 100
        st.write(f"El error relativo es: {error:.2f}%")

        # Crear gráfica
        x_values = np.linspace(a, b, 100)
        y_values = [fx.subs(x, val) for val in x_values]

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, color='blue', label='f(x)')
        ax.grid()

        # Plano cartesiano (Ejes)
        ax.vlines(x=0, ymin=0, ymax=max(y_values), color='k')
        ax.hlines(y=0, xmin=a, xmax=b, color='k')

        # Límites xl y xu
        ax.vlines(x=a, ymin=0, ymax=fx.subs(x, a), color='r', linestyle='--')
        ax.vlines(x=b, ymin=0, ymax=fx.subs(x, b), color='r', linestyle='--')

        # Área bajo la curva
        x_fill = np.linspace(a, b, 100)
        y_fill = [fx.subs(x, val) for val in x_fill]
        ax.fill_between(x_fill, y_fill, color='r', alpha=0.2, label='Área bajo la curva')

        plt.grid(True)
        plt.legend()

        # Mostrar gráfica
        st.pyplot(fig)

    except Exception as e:
        st.write(f"Error: {e}")


with tabs[1]:
    st.markdown("Simpson 3/8")
    st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrXcP6z77LAuWpyCEFfjd102XshQiVVjM1uTm1Of6rDn5tS9G9bg90yslI_q009LvdKvD6jZPVwB4u2ItIc1GpYaZacKes9pmhJpIEv-hhvymHXOtLhQupPeyYMQRiG2VgjCLMnEAmz60-o4KPeEW5LbA_DDSjsw24jn7twugTRv9VLwCGpCnzfeyR/s953/SIMPLEX.png',width=500)
    #codigo aqui

    #codigo aqui
