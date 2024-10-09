# Demanem a l'usuari que introdueixi dues paraules qualsevols
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# Comprovem si les dues paraules te almeys dos caracters per poder continuar amb el programa
if len(paraula1) >= 2 and len(paraula2) >= 2:
    # Codi per intercanviar les dos primeres lletres de cada paraula
    paraulanova1 = paraula2[:2] + paraula1[2:]
    paraulanova2 = paraula1[:2] + paraula2[2:]
    
    # Mostrem el resultat
    print(f"Resultat: {paraulanova1} {paraulanova2}")
else:
    print("Escriu dues paraules")