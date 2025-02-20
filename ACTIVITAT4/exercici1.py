import numpy as np

def crear_matriz():
    # Crear una matriz de ceros de 50x50
    matriz = np.zeros((50, 50), dtype=int)
    
    # Rellenar la diagonal con valores de 0 a 49
    np.fill_diagonal(matriz, np.arange(50))
    
    return matriz

def guardar_matriz(matriz, filename="exercici1.npy"):
    # Guardar la matriz en un archivo .npy
    np.save(filename, matriz)

if __name__ == "__main__":
    matriz = crear_matriz()
    guardar_matriz(matriz)
    print(f"Matriz guardada en 'exercici1.npy'")
