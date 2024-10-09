import random

# Escollim un numero aleatori entre 1 i 100
numero_adivina = random.randint(1, 100)

# Comptador d'intents
intents = 0

# Fem el bucle
while True:
    # Demanem a l'usuari que introdueixi un numero
    intent = int(input("Endevina el numero (entre 1 i 100): "))
    
    #
    intents += 1
    
    # Comprovació del numero
    if intent < numero_adivina:
        print("El numero es mes gran.")
    elif intent > numero_adivina:
        print("El numero es mes petit.")
    else:
        print(f"Felicitats! El numero era: {numero_adivina}")
        print(f"Ho has trobat en {intents} intents.")
        break