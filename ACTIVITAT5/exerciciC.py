import pandas as pd
import matplotlib.pyplot as plt

# IDs a filtrar
ids_filtrados = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

# Función para graficar el clock speed
def mostrar_clock_speed(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['id'], df['clock_speed'], color='blue', alpha=0.7)
    plt.xlabel("ID del móvil")
    plt.ylabel("Clock Speed (GHz)")
    plt.title("Clock Speed según el ID del móvil")
    plt.xticks(df['id'])
    plt.legend(["Clock Speed"])
    plt.show()

# Función para graficar los megapíxeles
def mostrar_megapixels(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['id'], df['pc'], color='green', alpha=0.7)
    plt.xlabel("ID del móvil")
    plt.ylabel("Megapixels (PC)")
    plt.title("Megapixels según el ID del móvil")
    plt.xticks(df['id'])
    plt.legend(["Megapixels"])
    plt.show()

# Función para graficar la batería
def mostrar_battery_power(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['id'], df['battery_power'], color='red', alpha=0.7)
    plt.xlabel("ID del móvil")
    plt.ylabel("Battery Power (mAh)")
    plt.title("Battery Power según el ID del móvil")
    plt.xticks(df['id'])
    plt.legend(["Battery Power"])
    plt.show()

# Función principal
def main():
    # Cargar el CSV
    df = pd.read_csv(r"C:\Users\Enric\M7_Repositorios\M07_UF1\ACTIVITAT5\mobiles.csv")
    
    # Filtrar solo los IDs especificados
    df_filtrado = df[df['id'].isin(ids_filtrados)]
    
    # Generar las gráficas
    mostrar_clock_speed(df_filtrado)
    mostrar_megapixels(df_filtrado)
    mostrar_battery_power(df_filtrado)

# Ejecutar el script
if __name__ == "__main__":
    main()
