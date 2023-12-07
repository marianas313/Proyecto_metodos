#Interpolacion cuadratica

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def interpolacion_cuadratica(func, x_vals, tol):
    x = sp.symbols('x')

    # Definir la función simbólica
    f = sp.sympify(func)

    # Inicializar variables
    n = len(x_vals)
    x1, x2, x3 = x_vals[-3:]
    x_vals_plot = []
    f_vals_plot = []

    while True:
        # Calcular las evaluaciones de la función en los puntos dados
        f1 = f.subs(x, x1)
        f2 = f.subs(x, x2)
        f3 = f.subs(x, x3)

        # Calcular los coeficientes del polinomio cuadrático
        a = (f1*(x2 - x3) + f2*(x3 - x1) + f3*(x1 - x2)) / ((x1 - x2)*(x1 - x3)*(x2 - x3))
        b = (f1*(x3**2 - x2**2) + f2*(x1**2 - x3**2) + f3*(x2**2 - x1**2)) / ((x1 - x2)*(x1 - x3)*(x2 - x3))
        c = (f1*(x2 - x3)*x3*x2 + f2*(x3 - x1)*x1*x3 + f3*(x1 - x2)*x2*x1) / ((x1 - x2)*(x1 - x3)*(x2 - x3))

        x_opt = -b / (2 * a)

        # Calcular el valor de la función en el vértice
        f_opt = f.subs(x, x_opt)

        x_vals_plot.extend([x1, x2, x3, x_opt])
        f_vals_plot.extend([f1, f2, f3, f_opt])

        # Verificar la convergencia
        if abs(x_opt - x3) < tol:
            break

        # Actualizar los puntos para la próxima iteración
        x1, x2, x3 = x2, x3, x_opt

    return x_opt, f_opt, x_vals_plot, f_vals_plot

# Interfaz de usuario con Streamlit
st.title("Interpolación Cuadrática")

# Solicitar al usuario la función
funcion = st.text_input("Ingrese la función:")

# Solicitar al usuario el número de valores de x
cantidad_valores = st.number_input("Ingrese el número de valores de x que proporcionará:", min_value=2, step=1, value=3)

# Solicitar al usuario ingresar los valores de x
valores = [st.number_input(f"Ingrese el valor de x{i + 1}:") for i in range(cantidad_valores)]

# Solicitar al usuario ingresar la tolerancia
tolerancia = st.number_input("Ingrese la tolerancia para la convergencia:")

# Aplicar interpolación cuadrática
optimal_x, optimal_f, x_vals_plot, f_vals_plot = interpolacion_cuadratica(funcion, valores, tolerancia)

# Graficar la función y los puntos relevantes durante la interpolación
t = np.linspace(min(valores) - 1, max(valores) + 1, 400)
y = [sp.sympify(funcion).subs('x', xi) for xi in t]

fig, ax = plt.subplots()
ax.plot(t, y, label=str(funcion), color='blue')
ax.scatter(x_vals_plot, f_vals_plot, color='red')
ax.set_title("Interpolación Cuadrática")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid()
ax.legend()
st.pyplot(fig)

# Mostrar resultados
st.write(f"\nEl valor óptimo de x es: {optimal_x}")
st.write(f"El valor óptimo de la función es: {optimal_f}")
