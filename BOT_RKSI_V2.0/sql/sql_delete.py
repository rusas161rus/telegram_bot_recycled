import psycopg2
import config
from psycopg2 import Error

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def create_request_delete_1(message, bot, __name__):
    if __name__ == '__main__':           
        try:                  
            cursor = connection.cursor()                              
            cursor.execute("""Delete from Raspisanie where id = ('{}')""".format(message.text))
            connection.commit()
            print(cursor.rowcount, "Запись успешно удалена")        
            bot.send_message(message.chat.id, "Запись успешно удалена".format(name = message.text))  
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text)) 