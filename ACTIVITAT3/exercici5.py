# Demanar una frase a l'usuari
frase = input("Introdueix una frase: ")

# Eliminar espais i guardar els caràcters en una tupla
tupla_caracters = tuple(frase.replace(" ", ""))

# Eliminar caràcters repetits mantenint l'ordre
frase_sense_repetits = "".join(dict.fromkeys(tupla_caracters))

# Mostrar els resultats
print("Contingut de la tupla:", tupla_caracters)
print("Frase sense caràcters repetits:", frase_sense_repetits)
