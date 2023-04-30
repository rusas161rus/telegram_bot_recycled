import psycopg2
import config
from psycopg2 import Error

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def create_request_SQL_predmet0(message, bot, __name__, text_predmet_0):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_0]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set PREPODOVATEL_NAME = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   

def create_request_SQL_predmet1(message, bot, __name__, text_predmet_1):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_1]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set PREDMET = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))   

def create_request_SQL_predmet2(message, bot, __name__, text_predmet_2):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_2]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set MAIL = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))

def create_request_SQL_predmet3(message, bot, __name__, text_predmet_3):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_3]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set FONE = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))

def create_request_SQL_predmet4(message, bot, __name__, text_predmet_4):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_4]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set REF = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))

def create_request_SQL_predmet5(message, bot, __name__, text_predmet_5):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_5]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set ON_LINE_CABINET = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))

def create_request_SQL_predmet6(message, bot, __name__, text_predmet_6):
    if __name__ == '__main__':     
        try:         
            text_only_one_0 = [text_predmet_6]       
            cursor = connection.cursor()                              
            cursor.execute("""Update PREPODOVATEL_TABLE set PRIMECHANIE = '{}' where id = %s""".format(message.text), (text_only_one_0))
            connection.commit()
            print(cursor.rowcount, "Запись успешно обновлена")        
            bot.send_message(message.chat.id, "Запись успешно обновлена".format(name = message.text))         
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))