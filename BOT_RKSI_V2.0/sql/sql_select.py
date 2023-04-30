from psycopg2 import Error
import psycopg2
import config
import os

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def sql_select_funk(bot, __name__, message):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from Raspisanie".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                b = str(row[1])
                c = str(row[2])
                d = str(row[3])
                e = str(row[4])                                 
                f = str(row[5])
                g = str(row[6])                
                raspis=("|ИД=" + a + "|" + b + ", " + c + ", " + d + "\n" + e + ", " + f + ", " + g + "\n\n")
                bot.send_message(message.chat.id, raspis)
                #print("ИД =", row[0], "| Дата =", row[1], "| Время начала =", row[2], "| Время конца =", row[3], "| Предмет =", row[4], "| Преподователь =", row[5], "| Кабинет =", row[6])                      
                with open ('rasp.txt', 'a') as f:
                    f.write(raspis)
            with open("rasp.txt") as file:
                data = file.read()
            
            os.remove("rasp.txt")
               
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(message.chat.id, "Поиск завершен")

def select_request_SQL_s_0(message, bot, __name__, text_select_ts_0, text_select_ts_1):
    if __name__ == '__main__':
        try:        
            #text_select_ts_1 = message.text
            time_s = [text_select_ts_0, text_select_ts_1]
            cursor = connection.cursor()                              
            cursor.execute("SELECT *   from raspisanie r  WHERE (time_s , time_s) OVERLAPS (%s::time , %s::time);", (time_s))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                b = str(row[1])
                c = str(row[2])
                d = str(row[3])
                e = str(row[4])                                 
                f = str(row[5])
                g = str(row[6])                
                raspis=("|ИД=" + a + "|" + b + ", " + c + ", " + d + "\n" + e + ", " + f + ", " + g + "\n\n")
                bot.send_message(message.chat.id, raspis)
                #print("ИД =", row[0], "| Дата =", row[1], "| Время начала =", row[2], "| Время конца =", row[3], "| Предмет =", row[4], "| Преподователь =", row[5], "| Кабинет =", row[6])                      
                with open ('rasp.txt', 'a') as f:
                    f.write(raspis)
            with open("rasp.txt") as file:
                data = file.read()
            
            os.remove("rasp.txt")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))                
        finally: 
                bot.send_message(message.chat.id, "Поиск завершен!".format(name = message.text))
                
def select_request_SQL_s_1(message, bot, __name__, text_select_tp_0, text_select_tp_1):
    if __name__ == '__main__':
        try:         
            #text_select_tp_1 = message.text
            time_p = [text_select_tp_0, text_select_tp_1]
            cursor = connection.cursor()                              
            cursor.execute("SELECT *   from raspisanie WHERE (time_p , time_p) OVERLAPS (%s::time , %s::time);", (time_p))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                b = str(row[1])
                c = str(row[2])
                d = str(row[3])
                e = str(row[4])                                 
                f = str(row[5])
                g = str(row[6])                
                raspis=("|ИД=" + a + "|" + b + ", " + c + ", " + d + "\n" + e + ", " + f + ", " + g + "\n\n")
                bot.send_message(message.chat.id, raspis)
                #print("ИД =", row[0], "| Дата =", row[1], "| Время начала =", row[2], "| Время конца =", row[3], "| Предмет =", row[4], "| Преподователь =", row[5], "| Кабинет =", row[6])                      
                with open ('rasp.txt', 'a') as f:
                    f.write(raspis)
            with open("rasp.txt") as file:
                data = file.read()
            
            os.remove("rasp.txt")           
        except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
                bot.send_message(message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        finally: 
                bot.send_message(message.chat.id, "Поиск завершен!".format(name = message.text))

def select_request_SQL_admin(message, bot, __name__, call):
    if __name__ == '__main__':
        try:                  
            cursor = connection.cursor()                              
            cursor.execute("select * from  admin_table")
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                a = str(row[0])
                b = str(row[1])
                c = str(row[2])
                d = str(row[3])
                e = str(row[4])                                 
                f = str(row[5])                                
                admin_l=("|№=" + a + "|user_id: " + b + "\nИмя: " + c + ", Фамилия: " + d + ", Отчество: " + e + "\nПримечание: " + f + "\n\n")
                #print("ИД =", row[0], "| Дата =", row[1], "| Время начала =", row[2], "| Время конца =", row[3], "| Предмет =", row[4], "| Преподователь =", row[5], "| Кабинет =", row[6])                      
                with open ('admin_list.txt', 'a') as f:
                    f.write(admin_l)
            with open("admin_list.txt") as file:
                data = file.read()
            bot.send_message(call.message.chat.id, data)
            os.remove("admin_list.txt")
            print(admin_l)           
        except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
                bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        finally: 
                bot.send_message(call.message.chat.id, "Поиск завершен!".format(name = message.text))