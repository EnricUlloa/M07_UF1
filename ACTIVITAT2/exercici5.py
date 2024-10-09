# Introduir un numero
numero = int(input("Introdueix un número: "))

# Comprovem si el numero introduit per l'usuari es parell o senar
if numero % 2 == 0:
    print(f"El numero {numero} es parell.")
else:
    print(f"El numero {numero} es senar.")