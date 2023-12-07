import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sistemas Lineales Triangulares")


# Definimos las matrices
f = np.array([[1, -2, 2, -3],
              [3, 4, -1, 1],
              [2, -3, 2, -1],
              [1, 1, -3, -2]])

s = np.array([[15],
              [-6],
              [17],
              [-7]])

# La matriz a tipo float para evitar truncamiento en operaciones
f = np.array(f, dtype=float)

# Tenemos la matriz aumentada
fs = np.concatenate((f, s), axis=1)
fs0 = np.copy(fs)

# Pivoteo por filas
tamano = np.shape(fs)
n = tamano[0]
m = tamano[1]

# Para cada fila en fs
for i in range(0, n-1, 1):
    # Columna desde diagonal i en adelante
    columna = abs(fs[i:, i])
    dax = np.argmax(columna)

    # Si dondemax no está en la diagonal
    if (dax != 0):
        # Intercambiar filas
        temporal = np.copy(fs[i, :])
        fs[i, :] = fs[dax+i, :]
        fs[dax+i, :] = temporal

# Eliminación hacia adelante
for i in range(0, n-1, 1):
    pivote = fs[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = fs[k, i] / pivote
        fs[k, :] = fs[k, :] - fs[i, :] * factor

# Sustitución hacia atrás
ultfila = n-1
ultcolumna = m-1
X = np.zeros(n, dtype=float)

for i in range(ultfila, 0-1, -1):
    suma = 0
    for j in range(i+1, ultcolumna, 1):
        suma = suma + fs[i, j] * X[j]
    b = fs[i, ultcolumna]
    X[i] = (b - suma) / fs[i, i]

X = np.transpose([X])

# Salida
st.write('Matriz aumentada:')
st.write(fs0)
st.write('Pivoteo parcial por filas')
st.write(fs)
st.write('Solución:')
st.write(X)

# Gráficos
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].matshow(fs0, cmap='viridis')
ax[0].set_title('Matriz aumentada')
ax[0].axis('off')

ax[1].matshow(fs, cmap='viridis')
ax[1].set_title('Pivoteo parcial por filas')
ax[1].axis('off')

ax[2].matshow(np.diag(np.ones(n)), cmap='viridis')
ax[2].set_title('Solución')
ax[2].axis('off')

st.pyplot(fig)