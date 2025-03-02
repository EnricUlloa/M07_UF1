import psycopg2
from conn import connection_db  # Importa la conexión

def create_table():
    conn = connection_db()  # Conectar a la BD
    if conn is None:
        print("❌ No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conn.cursor()

        sql = ''' 
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_surname VARCHAR(255) NOT NULL,
            user_age BIGINT NOT NULL,
            user_email VARCHAR(255) NOT NULL,
            user_phone VARCHAR(20) NOT NULL  -- 🔹 Añadido el sexto campo
        );'''

        cursor.execute(sql)
        conn.commit()
        print("✅ Tabla 'users' creada correctamente.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error al crear la tabla:", str(e))

# Ejecutar la función cuando se corra el script
if __name__ == "__main__":
    create_table()
