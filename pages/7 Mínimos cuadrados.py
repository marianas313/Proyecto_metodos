import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

# Título de la aplicación
st.title('Interpolación y Ajuste de Recta')

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

# Verificar si se ha subido un archivo
if uploaded_file is not None:
    # Leer el archivo CSV
    data = pd.read_csv(uploaded_file)
    df = pd.DataFrame(data)

    x = np.array(df["X"])
    y = np.array(df["Y"])

    sx = np.sum(x)
    sy = np.sum(y)

    sx2 = np.sum(x**2)
    sxy = np.sum(x*y)

    n = len(x)

    # Calcular la pendiente (m) y la ordenada al origen (b)
    m = ((n*sxy) - (sx*sy))/((n*sx2)-(sx**2))
    b = (sy - (m*sx))/n

    # Calcular la recta de interpolación
    recta = m*x + b

    # Calcular R^2
    r2 = r2_score(y, recta)
    st.write(f"Coeficiente de determinación (R^2): {r2:.4f}")

    # Calcular MSE
    mse = mean_squared_error(y, recta)
    st.write(f"Error cuadrático medio (MSE): {mse:.4f}")

    # Graficar los datos y la recta de interpolación
    fig, ax = plt.subplots()
    ax.scatter(df["X"].to_list(), df["Y"].to_list(), color='blue', label="Datos")
    ax.plot(x, recta, color='red', label=f"y = {m:.4f}x + {b:.4f}")

    ax.set_title("Interpolación y Ajuste de Recta")
    ax.grid()
    ax.legend()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
