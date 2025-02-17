# Demanar un número a l'usuari entre 1 i 10
while True:
    try:
        num = int(input("Introdueix un número entre 1 i 10: "))
        if 1 <= num <= 10:
            break
        else:
            print("El número ha d'estar entre 1 i 10.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# Crear la taula de multiplicar i mostrar-la per pantalla
taula = tuple(num * i for i in range(1, 11))
print(", ".join(map(str, taula)))
