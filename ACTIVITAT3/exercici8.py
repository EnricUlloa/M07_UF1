# Demanar 10 números a l'usuari separats per espais
while True:
    try:
        entrada = input("Introdueix 10 números separats per un espai: ")
        numeros = list(map(float, entrada.split()))

        if len(numeros) == 10:
            break
        else:
            print("Has d'introduir exactament 10 números.")
    except ValueError:
        print("Si us plau, introdueix només números vàlids.")

# Calcular la suma total i la mitjana
suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

# Afegir la suma i la mitjana a la llista
numeros.append(suma_total)
numeros.append(mitjana)

# Mostrar els resultats
print("\nNúmeros de l’usuari:", numeros[:-2])
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
