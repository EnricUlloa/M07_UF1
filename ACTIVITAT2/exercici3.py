# Introduir un valor qualsevol
valor1 = float(input("Introdueix un valor qualsevol: "))

# Introduir un altre valor qualsevol
valor2 = float(input("Introduiex un altre valor qualsevol: "))

# Comparar els valors introduits i mostrar el valor mes gran
if valor1 > valor2:
    print(f"El valor més gran es: {valor1}")
elif valor2 > valor1:
    print(f"El valor més gran es: {valor2}")
else:
    print(f"Els dos valors són iguals.")
    