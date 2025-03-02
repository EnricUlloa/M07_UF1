def read(conn):
    conn = conn
    cursor = conn.cursor()

    sql_read = ''' SELECT user_id, user_name, user_surname, user_age, user_email
                      FROM users'''

    cursor.execute(sql_read)
    conn.commit()

    result = cursor.fetchall()

    return result
