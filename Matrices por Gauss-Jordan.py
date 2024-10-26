import numpy as np

def Gauss_Jordan(matriz):
    matrices = []
    matrices.append(np.copy(matriz))
    
    filas, columnas = matriz.shape
    for i in range(filas):
        # Ponemos en 1 todas las filas de la diagonal
        matriz[i] = matriz[i] / matriz[i, i]
        
        # Transformamos todas las que no sean de la diagonal como 0
        for j in range(filas):
            if i != j:
                k = matriz[j, i]
                matriz[j] = matriz[i] * (-k) + matriz[j]
        matrices.append(np.copy(matriz))
        
    # Devolvemos la lista de matrices
    return np.round(np.array(matrices), 1)

def MetodoParaValores(metodo, matriz):
    if (metodo == "Gauss-Jordan"):
        return Gauss_Jordan(matriz)
    else:
        return "Metodo no disponible :c"

matriz = [[4, 1, 2, 9],
          [2, 4, -1, -5],
          [1, 1, -3, -9]]

matriz = np.array(matriz, float)

print(MetodoParaValores("Gauss-Jordan", matriz))