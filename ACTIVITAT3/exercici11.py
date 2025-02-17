# Crear un diccionari de divises amb els seus símbols
divises = {
    "Euro": "€",
    "Dòlar": "$",
    "Lliura": "£",
    "Ien": "¥",
    "Franc suís": "CHF",
    "Dòlar canadenc": "C$",
    "Pesos mexicans": "$",
    "Yuan": "¥"
}

# Demanar una divisa a l'usuari
divisa_usuari = input("Introdueix una divisa (per exemple: Euro, Dòlar, Lliura...): ").strip()

# Comprovar si la divisa existeix al diccionari
if divisa_usuari in divises:
    print(f"El símbol de {divisa_usuari} és: {divises[divisa_usuari]}")
else:
    print(f"La divisa {divisa_usuari} no està al diccionari.")
