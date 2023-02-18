import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",                                
                                password="xxxx
                                host="localhost",
                                port="5432",
                                database="BOT_TEL_TEST")

try:  
    cursor = connection.cursor()   
    create_table_query ='''CREATE TABLE ADMIN_TABLE
                          (ID SERIAL PRIMARY  KEY      NOT NULL,
                           USER_ID            INT      NOT NULL,                          
                           USER_LAST_NAME     TEXT         NULL,
                           USER_FERST_NAME    TEXT         NULL,
                           USER_SUR_NAME      TEXT         NULL,  
                           PRIMECHANIE        TEXT         NULL)'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

try:    
    cursor = connection.cursor()   
    create_table_query ='''CREATE TABLE Raspisanie
                          (ID SERIAL PRIMARY KEY     NOT NULL,
                          DATE            DATE NOT NULL DEFAULT NOW(),                          
                          TIME_S          TIME    NOT NULL,
                          TIME_P          TIME    NOT NULL,
                          PREDMET         TEXT    NOT NULL,
                          PREPODOVATEL    TEXT    NOT NULL,
                          KABINET         TEXT    NOT NULL)'''    
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
