import psycopg2

def connection_db():
    try:
        conn = psycopg2.connect(
            database="postgres_24255",
            user="user_postgres1",
            password="pass_postgres1",
            host="localhost",
            port="5433"  # Cambiado de 5432 a 5433
        )
        print("✅ Conexión establecida correctamente")
        return conn
    except Exception as e:
        print("❌ Error en la conexión:", str(e))
        return None

if __name__ == "__main__":
    connection_db()
