def create_registre(conn):
    if conn is None:
        print("❌ No hay conexión con la base de datos")
        return
    
    try:
        print("ℹ️ Ejecutando create_registre...")  # Para verificar que la función corre

        cursor = conn.cursor()

        sql = ''' 
        INSERT INTO users (user_name, user_surname, user_age, user_email)
        VALUES ('Paco', 'Lopez', 18, 'loquesea@gmail.com')
        '''
        
        cursor.execute(sql)
        conn.commit()
        print("✅ Registre creat correctament")

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Error en la inserció:", str(e))
