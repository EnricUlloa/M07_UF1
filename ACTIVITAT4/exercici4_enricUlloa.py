import numpy as np

def crear_matriz():
    """Crea una matriz de 3x4 con valores aleatorios entre 0 y 80"""
    matriz = np.random.randint(0, 81, (3, 4))  # Matriz 3x4
    print("Matriz original (3x4):")
    print(matriz)
    return matriz

def modificar_matriz(matriz):
    """Convierte la matriz de 3x4 en 4x3, pasando la última fila como última columna"""
    fila_extra = matriz[-1, :]  # Última fila (1x4)
    matriz_modificada = np.delete(matriz, -1, axis=0)  # Eliminar última fila (queda 2x4)
    
    # Transponer la matriz para cambiarla a 4x2
    matriz_modificada = matriz_modificada.T  # Ahora es 4x2

    # Apilar la fila_extra como última columna
    matriz_modificada = np.column_stack((matriz_modificada, fila_extra))  # Ahora es 4x3

    print("\nMatriz modificada (4x3):")
    print(matriz_modificada)
    return matriz_modificada

def ajustar_ultima_columna(matriz):
    """Modifica la última columna para que todos sus valores sean iguales al primero de la columna"""
    valor_fijo = matriz[0, -1]  # Primer valor de la última columna
    matriz[:, -1] = valor_fijo  # Reemplazar toda la última columna con este valor

    print("\nMatriz final con última columna ajustada:")
    print(matriz)
    return matriz

if __name__ == "__main__":
    matriz = crear_matriz()
    matriz_modificada = modificar_matriz(matriz)
    matriz_final = ajustar_ultima_columna(matriz_modificada)
