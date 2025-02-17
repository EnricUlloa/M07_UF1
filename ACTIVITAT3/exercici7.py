# Crear un diccionari buit per als contactes
contactes = {}

while True:
    # Demanar el nom
    nom = input("Introdueix un nom (o escriu 'no' per acabar): ").strip()

    # Si l'usuari escriu 'no', es para el programa
    if nom.lower() == "no":
        print("Finalitzant l'entrada de contactes...")
        break

    # Comprovar si el nom ja existeix al diccionari
    if nom in contactes:
        print("Aquest nom ja està registrat. No s’afegirà al diccionari.")
        continue  # Tornar a demanar un altre contacte

    # Demanar l'edat i validar que sigui un número
    while True:
        try:
            edat = int(input(f"Introdueix l'edat de {nom}: "))
            break  # Sortir del bucle si l'entrada és vàlida
        except ValueError:
            print("Si us plau, introdueix una edat vàlida (nombre enter).")

    # Afegir el contacte al diccionari
    contactes[nom] = edat
    print(f"Contacte {nom} afegit correctament.\n")

# Mostrar el diccionari final
print("\nContactes guardats:")
for nom, edat in contactes.items():
    print(f"{nom}: {edat} anys")
