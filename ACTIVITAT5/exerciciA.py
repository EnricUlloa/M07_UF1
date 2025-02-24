import pandas as pd
import matplotlib.pyplot as plt

def casos_per_mes_pais(df):
    df_filtered = df.groupby(['location', 'month'])['new_cases'].sum().unstack()
    df_filtered.T.plot(kind='bar', figsize=(10, 5))
    plt.title("Casos per mes per país")
    plt.xlabel("Mes")
    plt.ylabel("Nombre de casos")
    plt.legend(title="Países")
    plt.show()

def morts_per_mes_pais(df):
    df_filtered = df.groupby(['location', 'month'])['new_deaths'].sum().unstack()
    df_filtered.T.plot(kind='bar', figsize=(10, 5))
    plt.title("Morts per mes per país")
    plt.xlabel("Mes")
    plt.ylabel("Nombre de morts")
    plt.legend(title="Países")
    plt.show()

def reproduction_rate_per_mes_pais(df):
    df_filtered = df.groupby(['location', 'month'])['reproduction_rate'].mean().unstack()
    df_filtered.T.plot(kind='line', marker='o', figsize=(10, 5))
    plt.title("Taxa de reproducció per mes per país")
    plt.xlabel("Mes")
    plt.ylabel("Taxa de reproducció")
    plt.legend(title="Países")
    plt.show()

def main():
    df = pd.read_csv(r"C:\Users\Enric\M7_Repositorios\M07_UF1\ACTIVITAT5\df_covid19_countries.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    df_filtered = df[df['location'].isin(["Spain", "France", "Italy", "Germany", "USA", "Brazil", "India", "Russia", "UK", "Mexico"]) & (df['date'].dt.year == 2021)]
    
    casos_per_mes_pais(df_filtered)
    morts_per_mes_pais(df_filtered)
    reproduction_rate_per_mes_pais(df_filtered)

if __name__ == "__main__":
    main()
