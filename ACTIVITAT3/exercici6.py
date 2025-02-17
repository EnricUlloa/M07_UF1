# Llista inicial amb les àrees del pis
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, 
             "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# 1. Imprimir el segon element
print(f"El segon element és: {areas_pis[1]}")

# 2. Imprimir l’últim element
print(f"L'últim element és: {areas_pis[-1]}")

# 3. Imprimir l’àrea de la terrassa
index_terrassa = areas_pis.index("Terrassa") + 1
print(f"L'àrea de la terrassa és: {areas_pis[index_terrassa]}")

# 4. Imprimir del primer element al tercer element
print(f"Del primer element al tercer element: {areas_pis[:3]}")

# 5. Imprimir del tercer element a l’últim
print(f"Del tercer element a l'últim: {areas_pis[2:]}")

# 6. Imprimir el total de l'àrea de les dues habitacions
index_hab1 = areas_pis.index("Habitació1") + 1
index_hab2 = areas_pis.index("Habitació2") + 1
total_habitacions = areas_pis[index_hab1] + areas_pis[index_hab2]
print(f"Total de l'àrea de les dues habitacions: {total_habitacions}")

# 7. Modificar l’àrea del lavabo i imprimir la nova llista
index_lavabo = areas_pis.index("Lavabo") + 1
areas_pis[index_lavabo] = 8.5  # Modifiquem l'àrea
print(f"Llista amb l'àrea del lavabo modificada: {areas_pis}")

# 8. Afegir "Pati interior" i 2.78 a les últimes posicions
areas_pis.extend(["Pati interior", 2.78])
print(f"Llista amb el pati interior afegit: {areas_pis}")

# 9. Imprimir el total de l’àrea del pis
total_area = sum(areas_pis[1::2])  # Sumar només els valors numèrics (els elements de posició senar)
print(f"Total de l'àrea del pis: {total_area}")
