import numpy as np

def crear_array_1():
    """Crea un array unidimensional con los valores [88, 23, 39, 41]"""
    return np.array([88, 23, 39, 41])

def crear_array_2():
    """Crea una matriz 2x3 con los valores dados"""
    return np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])

def crear_array_3():
    """Crea una matriz columna (3x1) con los valores dados"""
    return np.array([[12], [4], [9], [8]])

if __name__ == "__main__":
    print("Array 1:")
    print(crear_array_1())

    print("\nArray 2:")
    print(crear_array_2())

    print("\nArray 3:")
    print(crear_array_3())
