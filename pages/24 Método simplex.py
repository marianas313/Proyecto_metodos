#Metodo simplex

import streamlit as st
import numpy as np
from scipy.optimize import linprog

# Encabezado de la aplicación
st.title("Resolución de Problemas de Programación Lineal")

# Solicitar coeficientes de la función objetivo
c = [st.number_input(f"Ingrese el coeficiente c{i+1} de la función objetivo:", key=f"c{i+1}") for i in range(2)]

# Solicitar coeficientes de las restricciones
num_restricciones = st.number_input("Ingrese el número de restricciones:", min_value=1, step=1)
A = []
b = []
for i in range(num_restricciones):
    restriccion = [st.number_input(f"Ingrese el coeficiente A{i+1}{j+1} de la restricción {i+1}:", key=f"A{i+1}{j+1}") for j in range(2)]
    lado_derecho = st.number_input(f"Ingrese el lado derecho (b) de la restricción {i+1}:", key=f"b{i+1}")
    A.append(restriccion)
    b.append(lado_derecho)

# Solicitar límites de las variables
x_lower_bound = st.number_input("Ingrese el límite inferior para x:", key="x_lower_bound")
x_upper_bound = st.number_input("Ingrese el límite superior para x (deje en blanco para infinito):", key="x_upper_bound", value=float('inf'))
y_lower_bound = st.number_input("Ingrese el límite inferior para y:", key="y_lower_bound")
y_upper_bound = st.number_input("Ingrese el límite superior para y (deje en blanco para infinito):", key="y_upper_bound", value=float('inf'))

# Límites inferiores y superiores de las variables
x_bounds = (x_lower_bound, x_upper_bound)
y_bounds = (y_lower_bound, y_upper_bound)

# Resolver el problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Mostrar el resultado en la interfaz
st.header("Resultado:")
st.write("Valor óptimo:", -result.fun)
st.write("Variables óptimas:", result.x)