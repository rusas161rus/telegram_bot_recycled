import os
import psycopg2
import config
from psycopg2 import Error
from message_handler_rep import pars_web_site_0

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def sql_insert_funk(bot, __name__, message):
    if __name__ == '__main__':
        try:
            pars_web_site_0.pars_site(__name__)                            
            file1 = open('pars.txt')
            cursor = connection.cursor()
            cursor.execute (''' DELETE FROM Raspisanie ''')    
            cursor = connection.cursor()
            file1 = open('pars.txt', 'r')   
            for line in file1:
                cursor.execute("""INSERT INTO Raspisanie (TIME_S, TIME_P, PREDMET, PREPODOVATEL, KABINET) VALUES {}""".format(line.strip()))
                print(line)                                
            connection.commit()
            print(cursor.rowcount, "1 Запись успешно Вставлена")
            bot.send_message(message.chat.id, "Расписание в базе успешно обновлено".format(message.from_user, bot.get_me()), 
            parse_mode = 'html')                        
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при обновлении".format(message.from_user, bot.get_me()))   
        finally:            
            if connection:                            
                print("Соединение с PostgreSQL закрыто")
                file1.close()
                os.remove("pars.txt")     
def create_request_SQL_ss6(message, bot, __name__, text_insert_0, text_insert_1, text_insert_2, text_insert_3, text_insert_4, text_insert_5):
    if __name__ == '__main__':    
        try:                
            #text_insert_5 = message.text
            text = [text_insert_0, text_insert_1, text_insert_2, text_insert_3, text_insert_4, text_insert_5]           
            cursor = connection.cursor()                              
            cursor.execute("""INSERT INTO Raspisanie (DATE, TIME_S, TIME_P, PREDMET, PREPODOVATEL, KABINET) VALUES (%s, %s, %s, %s, %s, %s)""".format(message.text), (text))
            connection.commit()
            print(cursor.rowcount, "1 Запись успешно Вставлена")        
            bot.send_message(message.chat.id, "1 Запись успешно Вставлена".format(name = message.text))  
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
def create_request_admin_SQL_ss6(message, bot, __name__, text_admin_insert_0, text_admin_insert_1, text_admin_insert_2, text_admin_insert_3, text_admin_insert_4):
    if __name__ == '__main__':    
        try:                
            #text_insert_5 = message.text
            text = [text_admin_insert_0, text_admin_insert_1, text_admin_insert_2, text_admin_insert_3, text_admin_insert_4]           
            cursor = connection.cursor()                              
            cursor.execute("""INSERT INTO admin_table (USER_ID, USER_LAST_NAME, USER_FERST_NAME, USER_SUR_NAME, PRIMECHANIE) VALUES (%s, %s, %s, %s, %s)""".format(message.text), (text))
            connection.commit()
            print(cursor.rowcount, "1 Запись успешно Вставлена")        
            bot.send_message(message.chat.id, "1 Запись успешно Вставлена".format(name = message.text))  
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))