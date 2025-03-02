def delete(conn):
    conn = conn
    cursor = conn.cursor()

    sql_delete = '''DELETE FROM public.USERS WHERE user_id = 1'''

    cursor.execute(sql_delete)
    conn.commit()
    resposta = "Usuari eliminat correctament"
    return resposta
