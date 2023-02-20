import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",                                
                                password="657834",
                                host="localhost",
                                port="5432",
                                database="BOT_TEL_TEST")


try:
    cursor = connection.cursor()
    # Выполнение SQL-запроса для вставки данных в таблицу
    insert_query = """ INSERT INTO admin_table (USER_ID, USER_LAST_NAME) VALUES ('658118472', 'Ruslan')"""    
    cursor.execute(insert_query)
    connection.commit()
    print("1 запись успешно вставлена")
    #

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")