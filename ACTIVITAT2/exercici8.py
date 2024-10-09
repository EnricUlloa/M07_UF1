# Introduir entre 1 i 3 paraules
entrada = input("Introdueix entre 1 i 3 paraules: ")

paraules = entrada.split()

# Comptar el numero de paraules
if 1 <= len(paraules) <= 3:
    
    for paraula in paraules:
        longitud = len(paraula)
        primercaracter = paraula[0]
        ultimcaracter = paraula[-1]
        
        # Mostrem els resultats
        print(f"Paraula: '{paraula}'")
        print(f"Nombre de caracters: {longitud}")
        print(f"Primer caracter: '{primercaracter}'")
        print(f"Ultim caracter: '{ultimcaracter}'")
        print()
else:
    print("Introdueix entre 1 i 3 paraules!!!!")