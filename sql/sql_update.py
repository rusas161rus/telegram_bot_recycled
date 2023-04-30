import psycopg2
import config
from psycopg2 import Error

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def create_request_SQL_ss0(message, bot, __name__, text_0):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_0]       
            cursor = connection.cursor()                              
            cursor.execute("""Update Raspisanie set TIME_S = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   
def create_request_SQL_ss1(message, bot, __name__, text_1):
    if __name__ == '__main__':      
        try:         
            text_only_one_1 = [text_1]       
            cursor = connection.cursor()              
            cursor.execute("""Update Raspisanie set TIME_P = '{}' where id = %s""".format(message.text), (text_only_one_1))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))   
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   
def create_request_SQL_ss2(message, bot, __name__, text_2):
    if __name__ == '__main__':      
        try:
            text_only_one_2 = [text_2]
            cursor = connection.cursor()                              
            cursor.execute("""Update Raspisanie set DATE = '{}' where id = %s""".format(message.text), (text_only_one_2))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   
def create_request_SQL_ss3(message, bot, __name__, text_3):  
    if __name__ == '__main__':    
        try:        
            text_only_one_3 = [text_3]
            cursor = connection.cursor()                              
            cursor.execute("""Update Raspisanie set PREDMET = '{}' where id = %s""".format(message.text), (text_only_one_3))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   
def create_request_SQL_ss4(message, bot, __name__, text_4):   
    if __name__ == '__main__':   
        try:         
            text_only_one_4 = [text_4]
            cursor = connection.cursor()                              
            cursor.execute("""Update Raspisanie set PREPODOVATEL = '{}' where id = %s""".format(message.text), (text_only_one_4))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))    
def create_request_SQL_ss5(message, bot, __name__, text_5):   
    if __name__ == '__main__':   
        try:         
            text_only_one_5 = [text_5]
            cursor = connection.cursor()                              
            cursor.execute("""Update Raspisanie set KABINET = '{}' where id = %s""".format(message.text), (text_only_one_5))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))     
            
