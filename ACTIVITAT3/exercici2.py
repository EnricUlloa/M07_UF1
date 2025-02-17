# Crear una tupla amb els mesos de l'any (indexats del 1 al 12)
mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", 
         "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

while True:
    try:
        # Demanar un número a l'usuari
        num = int(input("Introdueix un número entre 0 i 12 (0 per sortir): "))

        if num == 0:
            print("Programa finalitzat.")
            break
        elif 1 <= num <= 12:
            print(f"{mesos[num - 1]}")
        else:
            print("Si us plau, introdueix un número entre 0 i 12.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")
