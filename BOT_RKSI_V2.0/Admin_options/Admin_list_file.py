import config
import psycopg2
from psycopg2 import Error
import schedule
from threading import Thread
from time import sleep

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

# Admin_list
class Admin_user_id():
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name_user = name

Admin_user_0 = Admin_user_id (0000000, "xxxxxxxx")
Admin_list = {0}


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    try:
        cursor = connection.cursor()                              
        cursor.execute("select user_id from admin_table")
        connection.commit()
        record = cursor.fetchall()
        Admin_list.clear()
        for row in record:
            a={int(row[0])}
            Admin_list.update(a)
            print(Admin_list)

    
    except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

schedule.every(5).seconds.do(function_to_run)
Thread(target=schedule_checker).start() 