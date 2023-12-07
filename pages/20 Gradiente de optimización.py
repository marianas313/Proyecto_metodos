import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def descenso_gradiente_univariado(f, variable, ci=0, tasa_aprendizaje=0.01, max_iteraciones=1000, tolerancia=1e-6):
    info_iteracion = []

    derivada = sp.diff(f, variable)
    puntos = [ci]

    for iteracion in range(max_iteraciones):
        valor_gradiente = derivada.subs(variable, ci)
        ci -= tasa_aprendizaje * valor_gradiente
        valor_f = f.subs(variable, ci)
        error = abs(valor_gradiente)
        convergencia = error < tolerancia

        info_iteracion.append({
            'Iteración': iteracion + 1,
            'Valor Variable': round(ci, 6),
            'Valor Función': round(valor_f, 6),
            'Derivada': round(valor_gradiente, 6),
            'Error Absoluto': round(error, 6),
            'Convergencia': convergencia
        })

        if convergencia:
            break

    df_info_iteracion = pd.DataFrame(info_iteracion)

    resultado_final = {
        'Resultado Final': round(ci, 4),
        'Convergencia': convergencia
    }

    return df_info_iteracion, resultado_final

st.title("Descenso del Gradiente Univariado")

funcion_usuario = st.text_input("Ingrese la función (usando 'x' como variable):")
funcion_usuario_sympy = sp.sympify(funcion_usuario)

tasa_aprendizaje = st.number_input("Ingrese la tasa de aprendizaje:", min_value=0.01, max_value=1.0, value=0.1)

tabla_resultados, resultado_final = descenso_gradiente_univariado(funcion_usuario_sympy, 'x', tasa_aprendizaje=tasa_aprendizaje)

st.write("Tabla de Iteraciones:")
st.dataframe(tabla_resultados)

st.write("Resultado Final:")
st.write(resultado_final)

x_vals = np.linspace(float(tabla_resultados['Valor Variable'].min()) - 2, float(tabla_resultados['Valor Variable'].max()) + 2, 400)
y_vals = [funcion_usuario_sympy.subs('x', xi) for xi in x_vals]
plt.plot(x_vals, y_vals, label=str(funcion_usuario_sympy))
plt.scatter(tabla_resultados['Valor Variable'], tabla_resultados['Valor Función'], color='red')
plt.title("Método de Descenso del Gradiente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
st.pyplot(plt)
