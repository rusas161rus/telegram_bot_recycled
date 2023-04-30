import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",                                
                                password="657834",
                                host="localhost",
                                port="5432",
                                database="BOT_TEL_TEST")

try:  
    cursor = connection.cursor()   
    create_table_query ='''CREATE TABLE ADMIN_TABLE
                          (ID SERIAL PRIMARY  KEY      NOT NULL,
                           USER_ID            INT8      NOT NULL,                          
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


try:  
    cursor = connection.cursor()   
    create_table_query ='''CREATE TABLE PREPODOVATEL_TABLE
                          (ID SERIAL PRIMARY  KEY      NOT NULL,                                                    
                           PREPODOVATEL_NAME     TEXT         NULL,                           
                           PREDMET               TEXT         NULL,
                           REF                   TEXT         NULL,
                           MAIL                  TEXT         NULL,                           
                           ON_LINE_CABINET       TEXT         NULL,
                           FONE                  INT          NULL,
                           PRIMECHANIE           TEXT         NULL)'''

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
    file1 = open('1.txt', 'r', encoding='utf-8')   
    for line in file1:
        cursor.execute("""INSERT INTO PREPODOVATEL_TABLE (PREPODOVATEL_NAME, PREDMET, REF, MAIL, ON_LINE_CABINET) VALUES {}""".format(line.strip()))
        print(line)                                
    connection.commit()
    print(cursor.rowcount, "1 Запись успешно Вставлена")                        
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

