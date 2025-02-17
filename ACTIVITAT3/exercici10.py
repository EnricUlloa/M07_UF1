# Emmagatzemar l'abecedari en una llista
abecedari = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Eliminar les lletres en les posicions múltiples de 3
abecedari_filtrat = [lletra for index, lletra in enumerate(abecedari) if (index + 1) % 3 != 0]

# Convertir la llista resultant en una tupla
tupla_resultant = tuple(abecedari_filtrat)

# Mostrar la llista i la tupla
print("Llista filtrada:", abecedari_filtrat)
print("Tupla resultant:", tupla_resultant)
