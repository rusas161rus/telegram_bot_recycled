import config
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)
Admin_list = {0} 
# Admin_list
def sql_admin_check(__name__, message):
     if __name__ == '__main__':  
        try:
            id_message_user = message.from_user.id
            text=[id_message_user]
            cursor = connection.cursor()                              
            cursor.execute("select user_id from admin_table where user_id = %s", (text))
            connection.commit()
            record = cursor.fetchall()
            Admin_list.clear()
            for row in record:
                a={int(row[0])}
                Admin_list.update(a)
                print(Admin_list)
        
        except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)

        