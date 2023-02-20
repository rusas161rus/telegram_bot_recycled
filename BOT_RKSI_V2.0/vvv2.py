import psycopg2
from psycopg2 import Error




connection = psycopg2.connect(user="postgres",                                
                                password="657834",
                                host="localhost",
                                port="5432",
                                database="BOT_TEL_TEST")

try:             
        us_id=[658118472]
        cursor = connection.cursor()                              
        cursor.execute("select user_id from admin_table WHERE user_id = %s", (us_id))
        connection.commit()            
        record = cursor.fetchall()
        for row in record:
                a={int(row[0])}    
                
                print(a)

except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)