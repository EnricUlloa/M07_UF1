# Llista d'assignatures
assignatures = ["Matemàtiques", "Història", "Biologia", "Anglès", "Física", "Informàtica"]

# Llista per emmagatzemar les notes
notes = []

# Demanar les notes a l'usuari
for assignatura in assignatures:
    while True:
        try:
            nota = float(input(f"Introdueix la nota de {assignatura}: "))
            notes.append(nota)
            break
        except ValueError:
            print("Si us plau, introdueix una nota vàlida (nombre).")

# Mostrar els resultats
print("\nResultats:")
for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}.")
