import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

# Definir la variable simbólica x
x = sp.symbols('x')

# Interfaz de usuario con Streamlit
st.title("Regla del Trapecio")

# Entrada de los límites y número de intervalos
a = st.number_input("Ingrese el límite inferior a:", value=1 )
b = st.number_input("Ingrese el límite superior b:", value=6)
n = st.number_input("Ingrese el número de intervalos n:", value=6, step=2)

# Convertir a, b y h a valores numéricos
a, b, n = float(a), float(b), int(n)

# Crear la función simbólica fx
fx = x * sp.sin(x) + 3 * x - 1

# Calcular el ancho de los intervalos
h = (b - a) / n

# Calcular los puntos para la gráfica
t_grafica = np.linspace(a, b, 100)
y_grafica = t_grafica * np.sin(t_grafica) + 3 * t_grafica - 1

# Calcular la integral por la regla del trapecio
t = np.arange(a, b + h, h)
y = [float(round(fx.subs(x, ti), 3)) for ti in t]
I = h / 2 * (y[0] + 2 * sum(y[1:-1]) + y[-1])

# Calcular la integral real usando sympy
I_real = sp.integrate(fx, (x, a, b))

# Calcular el error relativo
error = np.abs((I_real - I) / I_real) * 100

# Mostrar resultados en Streamlit
st.write(f"La integral por la regla del trapecio es: {I}")
st.write(f"La integral por sympy es: {I_real}")
st.write(f"El error relativo es: {error:.2f}%")

# Crear gráfica en Streamlit
fig, ax = plt.subplots()
ax.plot(t_grafica, y_grafica, color='blue', label="f(x)")

# Gráfica de los trapecios
for i in range(n):
    x1 = a + i * h
    x2 = a + (i + 1) * h
    y1 = fx.subs(x, x1)
    y2 = fx.subs(x, x2)
    ax.plot([x1, x1, x2, x2, x1], [0, y1, y2, 0, 0], 'r', alpha=0.2)

ax.grid(True)
plt.legend()

# Mostrar gráfica en Streamlit
st.pyplot(fig)