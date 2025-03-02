def update(conn):
    cursor = conn.cursor()

    sql_update = ''' UPDATE public.USERS SET 
                    user_email ='updateoriol@outlook.com' 
                    WHERE user_id = 2'''  # Cambia 1 por 2

    cursor.execute(sql_update)
    conn.commit()

    # Obtiene el número de filas modificadas
    result = cursor.rowcount

    return result
