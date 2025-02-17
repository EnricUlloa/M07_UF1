# Demanar a l'usuari que introdueixi 10 números separats per un espai
while True:
    try:
        entrada = input("Introdueix 10 números separats per un espai: ")
        numeros = list(map(int, entrada.split()))

        if len(numeros) == 10:
            break
        else:
            print("Has d'introduir exactament 10 números.")
    except ValueError:
        print("Si us plau, introdueix només números vàlids.")

# Ordenar els números de menor a major i convertir-los en una tupla
tupla_ordenada = tuple(sorted(numeros))

# Mostrar la tupla per pantalla
print("Números ordenats:", tupla_ordenada)
