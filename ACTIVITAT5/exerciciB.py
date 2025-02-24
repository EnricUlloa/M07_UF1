import pandas as pd
import matplotlib.pyplot as plt

def mostrar_poblacion(df):
    plt.figure(figsize=(8, 8))
    plt.pie(df['Population'], labels=df['City'], autopct='%1.1f%%', startangle=140)
    plt.title("Población total por ciudad")
    plt.legend(title="Ciudades", loc="best")
    plt.show()

def mostrar_densidad_km2(df):
    df['Density (/km²)'] = df['Population'] / df['Area (km²)']
    plt.figure(figsize=(8, 8))
    plt.pie(df['Density (/km²)'], labels=df['City'], autopct='%1.1f%%', startangle=140)
    plt.title("Densidad por KM² por ciudad")
    plt.legend(title="Ciudades", loc="best")
    plt.show()

def mostrar_densidad_m2(df):
    df['Density (/mi²)'] = df['Population'] / (df['Area (km²)'] * 1e6)
    plt.figure(figsize=(8, 8))
    plt.pie(df['Density (/mi²)'], labels=df['City'], autopct='%1.1f%%', startangle=140)
    plt.title("Densidad por M² por ciudad")
    plt.legend(title="Ciudades", loc="best")
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\Enric\M7_Repositorios\M07_UF1\ACTIVITAT5\cities_population.csv")
    df.columns = df.columns.str.strip()

    # Limpiar la columna 'Population'
    df['Population'] = df['Population'].str.replace(r'\[.*?\]', '', regex=True)  # Elimina referencias en corchetes
    df['Population'] = df['Population'].str.replace(',', '').astype(float)  # Elimina comas y convierte a número
    
    # Limpiar la columna 'Area (km²)'
    df['Area (km²)'] = df['Area (km²)'].str.replace(r'\[.*?\]', '', regex=True)  # Elimina referencias en corchetes
    df['Area (km²)'] = df['Area (km²)'].astype(float)  # Convierte a float

    df_filtrado = df.head(10)  # Seleccionamos 10 ciudades
    
    mostrar_poblacion(df_filtrado)
    mostrar_densidad_km2(df_filtrado)
    mostrar_densidad_m2(df_filtrado)

if __name__ == "__main__":
    main()
