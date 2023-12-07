import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

# Solicitar al usuario ingresar las condiciones iniciales y el rango de tiempo
condiciones_iniciales_rk = [st.number_input(f"Ingrese la condición inicial para y{i + 1}(0):") for i in range(2)]
rango_tiempo_rk = (st.number_input("Ingrese el tiempo inicial:"), st.number_input("Ingrese el tiempo final:"))
paso_tiempo_rk = st.number_input("Ingrese el tamaño del paso (dt):")

tabs= st.tabs(['Runge Kutta orde 2','Runge Kutta orde 3', 'Runge Kutta orde 4'])
with tabs[0]:

    def runge_kutta_2(funcs, y0, t_range, dt):
        valores_tiempo = np.arange(t_range[0], t_range[1], dt)
        valores_y = [np.array(y0)]

        for t in valores_tiempo[:-1]:
            y_actual = valores_y[-1]

            k1 = np.array([f(t, *y_actual) for f in funcs])
            k2 = np.array([f(t + dt, *(y_actual + dt * k1)) for f in funcs])

            y_siguiente = y_actual + (dt/2) * (k1 + k2)
            valores_y.append(y_siguiente)

        return valores_tiempo, np.array(valores_y).T

    # Funciones para el sistema de ecuaciones diferenciales
    def func1(t, y1, y2):
        return y1 - y2

    def func2(t, y1, y2):
        return y1 + y2

    # Interfaz de usuario con Streamlit
    st.title("Runge-Kutta de Orden 2 para Sistema de Ecuaciones Diferenciales")


    # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 2
    valores_tiempo_rk, valores_y_rk = runge_kutta_2([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

    # Graficando la solución aproximada
    st.pyplot(plt.figure(figsize=(8, 6)))
    plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
    plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
    plt.xlabel('Tiempo')
    plt.ylabel('Variables y(t)')
    plt.title('Solución usando Runge-Kutta de orden 2')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

with tabs[1]:
    def runge_kutta_3(funcs, y0, t_range, dt):
        valores_tiempo = np.arange(t_range[0], t_range[1], dt)
        valores_y = [np.array(y0)]

        for t in valores_tiempo[:-1]:
            y_actual = valores_y[-1]

            k1 = np.array([f(t, *y_actual) for f in funcs])
            k2 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k1)) for f in funcs])
            k3 = np.array([f(t + dt, *(y_actual - dt*k1 + 2*dt*k2)) for f in funcs])

            y_siguiente = y_actual + (dt/6) * (k1 + 4*k2 + k3)
            valores_y.append(y_siguiente)

        return valores_tiempo, np.array(valores_y).T

        # Funciones para el sistema de ecuaciones diferenciales
        def func1(t, y1, y2):
            return y1 - y2

        def func2(t, y1, y2):
            return y1 + y2

        # Interfaz de usuario con Streamlit
        st.title("Runge-Kutta de Orden 3 para Sistema de Ecuaciones Diferenciales")


        # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 3
        valores_tiempo_rk, valores_y_rk = runge_kutta_3([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

        # Graficando la solución aproximada
        st.pyplot(plt.figure(figsize=(8, 6)))
        plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
        plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
        plt.xlabel('Tiempo')
        plt.ylabel('Variables y(t)')
        plt.title('Solución usando Runge-Kutta de orden 3')
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

with tabs[2]:
    def runge_kutta_4(funcs, y0, t_range, dt):
        valores_tiempo = np.arange(t_range[0], t_range[1], dt)
        valores_y = [np.array(y0)]

        for t in valores_tiempo[:-1]:
            y_actual = valores_y[-1]

            k1 = np.array([f(t, *y_actual) for f in funcs])
            k2 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k1)) for f in funcs])
            k3 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k2)) for f in funcs])
            k4 = np.array([f(t + dt, *(y_actual + dt * k3)) for f in funcs])

            y_siguiente = y_actual + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
            valores_y.append(y_siguiente)

        return valores_tiempo, np.array(valores_y).T

    # Funciones para el sistema de ecuaciones diferenciales
    def func1(t, y1, y2):
        return y1 - y2

    def func2(t, y1, y2):
        return y1 + y2

    # Interfaz de usuario con Streamlit
    st.title("Runge-Kutta de Orden 4 para Sistema de Ecuaciones Diferenciales")

    # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 4
    valores_tiempo_rk, valores_y_rk = runge_kutta_4([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

    # Graficando la solución aproximada
    st.pyplot(plt.figure(figsize=(8, 6)))
    plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
    plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
    plt.xlabel('Tiempo')
    plt.ylabel('Variables y(t)')
    plt.title('Solución usando Runge-Kutta de orden 4')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)    