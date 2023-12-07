#Modelo depredador-presa de Lotka-Volterra

import streamlit as st
import matplotlib.pyplot as plt

def lotka_volterra(p_inicial, h_inicial, r_p, r_h, a, b, tiempo):
    p = [p_inicial]
    h = [h_inicial]

    for _ in range(tiempo):
        dp_dt = r_p * p[-1] - a * p[-1] * h[-1]
        dh_dt = -r_h * h[-1] + b * p[-1] * h[-1]

        p_nueva = p[-1] + dp_dt
        h_nueva = h[-1] + dh_dt

        p.append(p_nueva)
        h.append(h_nueva)

    return p, h

# Función para graficar
def graficar_poblaciones(tiempo, poblaciones_p, poblaciones_h):
    plt.plot(tiempo, poblaciones_p, label='Presas (p)')
    plt.plot(tiempo, poblaciones_h, label='Depredadores (h)')
    plt.xlabel('Tiempo')
    plt.ylabel('Población')
    plt.title('Modelo Lotka-Volterra')
    plt.legend()
    st.pyplot()

st.title('Simulación del Modelo Lotka-Volterra')

p_inicial = st.number_input("Población inicial de presas (p)")
h_inicial = st.number_input("Población inicial de depredadores (h)")
r_p = st.number_input("Tasa intrínseca de crecimiento de presas (r_p)")
r_h = st.number_input("Tasa intrínseca de decrecimiento de depredadores (r_h)")
a = st.number_input("Tasa de encuentro entre presa y depredador (a)")
b = st.number_input("Eficiencia con la cual los encuentros aumentan depredadores (b)")
tiempo = st.number_input("Número de pasos de tiempo")

# Simular el modelo Lotka-Volterra
poblaciones_p, poblaciones_h = lotka_volterra(p_inicial, h_inicial, r_p, r_h, a, b, tiempo)

graficar_poblaciones(list(range(tiempo + 1)), poblaciones_p, poblaciones_h)