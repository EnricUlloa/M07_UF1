# Crear un diccionari per emmagatzemar assignatures i notes
notes_assignatures = {}

# Demanar les notes a l'usuari
for assignatura in ["Matemàtiques", "Història", "Biologia", "Anglès", "Física", "Informàtica"]:
    while True:
        try:
            nota = float(input(f"Introdueix la nota de {assignatura}: "))
            notes_assignatures[assignatura] = nota
            break
        except ValueError:
            print("Si us plau, introdueix una nota vàlida (nombre).")

# Mostrar els resultats
print("\nResultats:")
for assignatura, nota in notes_assignatures.items():
    print(f"A {assignatura} ha tret {nota}.")
