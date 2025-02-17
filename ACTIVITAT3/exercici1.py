# Demanar un número a l'usuari entre 10 i 100
while True:
    try:
        num = int(input("Introdueix un número entre 10 i 100: "))
        if 10 <= num <= 100:
            break
        else:
            print("El número ha d'estar entre 10 i 100.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# Crear la tupla amb els números de l'1 fins al número indicat
numeros = tuple(range(1, num + 1))

# Mostrar la tupla per pantalla
print(numeros)
