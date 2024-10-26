import numpy as np

def MatrizInversa(matriz):
    matriz = np.array(matriz, dtype=float)
    matrices = []
    n = matriz.shape[0]
    
    identidad = np.eye(n)
    matriz = np.hstack((matriz, identidad))

    for i in range(n):
        # Si el pivote es 0, intercambiamos filas
        if matriz[i, i] == 0:
            for k in range(i + 1, n):
                if matriz[k, i] != 0:
                    matriz[[i, k]] = matriz[[k, i]]
                    break
            else:
                raise ValueError("La matriz no es invertible.")
        
        # Hacemos la diagonal en 1s
        matriz[i] = matriz[i] / matriz[i, i]

        # Hacemos ceros en las demás filas de la columna actual
        for j in range(n):
            if i != j:
                factor = matriz[j, i]
                matriz[j] = matriz[j] - factor * matriz[i]
            matrices.append(matriz)
    # Extraemos la parte derecha (la inversa)
    inversa = matriz[:, n:]
    return np.round(inversa, 5)

# Matriz a invertir
matriz = [[4, 3, 10, 5],
          [5, -7, -3, -5],
          [-5, -8, 2, 0],
          [4, 0, -6, 4]]

# Obtener la inversa
print("Matriz inversa:")
matriz = np.array(matriz, float)
inversa = MatrizInversa(matriz)
print(inversa)

# Procesar la parte derecha de la matriz aumentada
matrizResultado = inversa

# Matriz A para desencriptar
A = np.array([[303, 317, 376, 263],
              [-37, -136, -164, -70],
              [-87, -204, -4, -180],
              [-22, 170, -100, 134]])

# Realizamos la multiplicación
multiplicacion = np.dot(matrizResultado, A)
multiplicacion = np.round(multiplicacion)
print("Multiplicacion")
print(multiplicacion)
# Diccionario de letras
abecedario = {1: "a", 2: "b", 3: "c", 4: "d",
              5: "e", 6: "f", 7: "g", 8: "h",
              9: "i", 10: "j", 11: "k", 12: "l",
              13: "m", 14: "n", 15: "ñ", 16: "o",
              17: "p", 18: "q", 19: "r", 20: "s",
              21: "t", 22: "u", 23: "v", 24: "w",
              25: "x", 26: "y", 27: "z", 28: " "}

# Desencriptar mensaje
mensajeDesencriptado = np.zeros(multiplicacion.shape, dtype=str)

for fila in range(multiplicacion.shape[0]):
    for columna in range(multiplicacion.shape[1]):
        numeroAux = int(multiplicacion[fila, columna])
        if numeroAux in abecedario:
            mensajeDesencriptado[fila, columna] = abecedario[numeroAux]
        else:
            mensajeDesencriptado[fila, columna] = '?'  # En caso de error

print("\nMensaje desencriptado:")
message = ""
mensajeDesencriptado = mensajeDesencriptado.T
for i in range(mensajeDesencriptado.shape[0]):
    for j in range(mensajeDesencriptado.shape[1]):
        message += mensajeDesencriptado[i, j]
print(message)