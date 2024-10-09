# Introduir el valor en Euros
valeuro = float(input("Introdueix un valor en Euros: "))

# Introduir el percentatge d'IVA que s'aplicara a el valor anterior
while True:
    IVA = int(input("Introdueix el percentatge d'IVA: "))
    if IVA in [4, 10, 21]:
        break
    else:
        print("IVA incorrecte. Posi un dels 3 percentatges valids.")

# El resultat final del valor un cop aplicat l'IVA
resultat = float(valeuro * (1 + (IVA / 100)))

# Mostrar per pantalla els diferents valors que s'han demanat
print(f"Valor introduït: {valeuro}" + " euros.")
print(f"Percentatge d'IVA: {IVA}" + "%.")
print(f"Valor final amb l'IVA afegit: {resultat}")
