#Newton para optimización

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def metodo_newton_max(func, xi, tol):
    x = sp.symbols('x')
    f = sp.sympify(func)
    f_principal = sp.diff(f, x)
    f_doble_principal = sp.diff(f_principal, x)

    x_val = xi
    iteracion = 0

    while True:
        f_prime_val = f_principal.subs(x, x_val)
        f_doble_prime_val = f_doble_principal.subs(x, x_val)

        if f_doble_prime_val == 0:
            st.write("El método de Newton no converge en este punto.")
            return None

        x_val_nuevo = x_val - f_prime_val / f_doble_prime_val

        if abs(x_val_nuevo - x_val) < tol:
            break

        x_val = x_val_nuevo
        iteracion += 1

    return x_val, f.subs(x, x_val), iteracion

# Interfaz de usuario con Streamlit
st.title("Método de Newton para encontrar el máximo")

# Solicitar al usuario ingresar la función
funcion_usuario = st.text_input("Ingrese la función (usando 'x' como variable):")

# Convertir la función ingresada a formato sympy
funcion_usuario_sympy = sp.sympify(funcion_usuario)

# Solicitar al usuario ingresar el punto inicial (xi)
xi = st.number_input("Ingrese el punto inicial (xi):")

# Solicitar al usuario ingresar la tolerancia
tolerancia = st.number_input("Ingrese la tolerancia para la convergencia:")

# Aplicar el método de Newton
resultado = metodo_newton_max(funcion_usuario_sympy, xi, tolerancia)

# Mostrar resultados y graficar
if resultado:
    x_max, f_max, iteraciones = resultado
    st.write(f"\nEl máximo de la función es: {f_max}")
    st.write(f"Se encontró en x = {x_max} después de {iteraciones} iteraciones.")

    # Generar datos para la gráfica
    x_vals = np.linspace(xi - 2, xi + 2, 400)
    y_vals = [funcion_usuario_sympy.subs('x', xi) for xi in x_vals]

    # Graficar la función y el punto máximo
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=str(funcion_usuario_sympy), color='blue')
    ax.scatter(x_max, f_max, color='red', label='Máximo')
    ax.set_title("Método de Newton para encontrar el máximo")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    ax.legend()
    st.pyplot(fig)
