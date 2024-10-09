# Demanen a l'usuari que introdueixi un numero
numero = int(input("Introdueix un numero per mostrar la seva taula de multiplicar: "))

# Mostrar tuala de multiplicar
print(f"Taula de multiplicar:")
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")