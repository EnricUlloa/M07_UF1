import numpy as np

def generar_matriz():
    """Genera una matriz de 3x3 con números aleatorios de 0 a 100 y permite redimensionarla."""
    matriz = np.random.randint(0, 101, (3, 3))  # Matriz 3x3 con números aleatorios
    print("Matriz original:")
    print(matriz)

    # Pedir nuevas dimensiones
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    # Redimensionar la matriz si el tamaño coincide
    if filas * columnas == matriz.size:
        matriz_reshaped = matriz.reshape(filas, columnas)
        print("\nMatriz redimensionada:")
        print(matriz_reshaped)
        return matriz_reshaped
    else:
        print("\nError: La cantidad de elementos no coincide con la nueva dimensión.")
        return matriz

def valor_maximo(matriz):
    """Devuelve el valor máximo de la matriz."""
    return np.max(matriz)

def valor_minimo(matriz):
    """Devuelve el valor mínimo de la matriz."""
    return np.min(matriz)

if __name__ == "__main__":
    matriz = generar_matriz()
    print(f"\nValor máximo: {valor_maximo(matriz)}")
    print(f"Valor mínimo: {valor_minimo(matriz)}")
