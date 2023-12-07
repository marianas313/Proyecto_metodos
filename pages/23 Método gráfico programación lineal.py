#Método Gráfico para Programación Lineal

import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, y = sp.symbols('x y')

num_restricciones = st.number_input("Ingrese el número de restricciones:")

restricciones = []
for i in range(num_restricciones):
    restriccion_str = st.text_input(f"Ingrese la ecuación de la restricción {i + 1} en términos de x e y:")
    restriccion = sp.sympify(restriccion_str)
    restricciones.append(restriccion)

# Configurar el rango para las variables
x_vals = np.linspace(0, 30, 100)

# Graficar las restricciones
for restriccion in restricciones:
    y_restriccion = sp.solve(restriccion, y)[0]
    func_restriccion = sp.lambdify(x, y_restriccion, modules=['numpy'])
    plt.plot(x_vals, func_restriccion(x_vals), label=sp.latex(restriccion))

plt.xlim(0, 30)
plt.ylim(0, 30)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.title('Método Gráfico para Programación Lineal')
plt.legend()
st.pyplot()
