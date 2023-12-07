import numpy as np
import streamlit as st

st.title("Eliminación Gaussiana y Pivoteo")


def eliminacion_gaussiana(matriz_aumentada):
    # Pivoteo parcial por filas
    tamano = np.shape(matriz_aumentada)
    n = tamano[0]

    for i in range(0, n-1, 1):
        # Columna desde diagonal i en adelante
        columna = abs(matriz_aumentada[i:, i])
        dax = np.argmax(columna)

        # Si dondemax no está en la diagonal
        if dax != 0:
            # Intercambiar filas
            temporal = np.copy(matriz_aumentada[i, :])
            matriz_aumentada[i, :] = matriz_aumentada[dax+i, :]
            matriz_aumentada[dax+i, :] = temporal

    # Sustitución hacia atrás
    X = np.zeros(n, dtype=float)

    for i in range(n-1, -1, -1):
        suma = 0
        for j in range(i+1, n, 1):
            suma = suma + matriz_aumentada[i, j] * X[j]
        b = matriz_aumentada[i, n]
        X[i] = (b - suma) / matriz_aumentada[i, i]

    X = np.transpose([X])
    return X

# Matrices originales
matriz_coeficientes = np.array([[1, -2, 2, -3],
                                [3, 4, -1, 1],
                                [2, -3, 2, -1],
                                [1, 1, -3, -2]])

matriz_resultados = np.array([[15],
                              [-6],
                              [17],
                              [-7]])

# Matriz aumentada
matriz_aumentada = np.concatenate((matriz_coeficientes, matriz_resultados), axis=1)

# Aplicar eliminación gaussiana
solucion = eliminacion_gaussiana(matriz_aumentada)

st.subheader("Matriz Aumentada:")
st.write(matriz_aumentada)

st.subheader("Resultado:")
st.write(solucion)