import psycopg2
import create_table as ct
import conn as cn
import create_registre as cr
import read as rd
import delete as dl
import update as up

if __name__ == "__main__":
    try:
        conn = cn.connection_db()

        if conn is None:
            print("❌ No se pudo establecer conexión con la base de datos.")
        else:
            while conn:
                option = input('''\nSelecciona opció:
 1. Create Table
 2. Create user
 3. Read table
 4. Update user
 5. Delete user
 6. Tancar sessió
\nIndica opció menú posant número: ''')

                match option:
                    case "1":
                        print('Creating table...')
                        print(ct.create_table(conn))
                    case "2":
                        print('Creating registre...')
                        print(cr.create_registre(conn))
                    case "3":
                        print('Reading registre...')
                        result = rd.read(conn)
                        for i in result:
                            print(f"user_id: {i[0]}\nuser_name: {i[1]}\nuser_surname: {i[2]}\nuser_age: {i[3]}\nuser_email: {i[4]}\n")
                    case "4":
                        print('Modificant usuari...')
                        result = up.update(conn)
                        print(f'Registres modificats: {result}')
                    case "5":
                        print('Deleting...')
                        print(dl.delete(conn))
                    case "6":
                        print("🛑 Tancant sessió...")
                        conn.close()
                        break  # Sale del bucle

    except (Exception, psycopg2.Error) as error:
        print("❌ Error:", error)
    finally:
        print('✅ FINALLY')
