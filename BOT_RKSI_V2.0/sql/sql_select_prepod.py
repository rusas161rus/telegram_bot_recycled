from psycopg2 import Error
import psycopg2
import config

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def sql_select_funk_Trichuk(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Трищук С.А.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Fichuk(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Фищук А.И.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Ygegova(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Ужегова Е.А.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Alibisheva(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Алябышева С.Н.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Vidineeva(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Видинеева Е.А.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Zadorognii(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Задорожный К.А.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Melnikova(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Мельникова М.В.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Necvetaeva(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Нецветаева А.Е.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Dozorova(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Дозорова Е.В.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Marisheva(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Марышева О.В.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Maheeva(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Махеева П.А.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")


def sql_select_funk_Dgalagonia(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Джалагония М.Ш.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Shterenzeer(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Штерензеер Т.И.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")

def sql_select_funk_Bolovihina(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREPODOVATEL_NAME = 'Болховитина О.И.'".format(message.text))
            connection.commit()            
            record = cursor.fetchall()
            for row in record:
                id = str(row[0])
                prepodovatel_name = str(row[1])
                predmet = str(row[2])
                ref = str(row[3])
                mail = str(row[4])                                 
                on_line_cabinet = str(row[5])
                fone = str(row[6])
                primechanie = str(row[7])                
                raspis=("|ИД=" + id + "|\n" + prepodovatel_name + ", " + predmet + "\nПочта: " + mail + "\nНомер телефона: " + fone + "\nПримечание: " +primechanie + "\n\n Ссылка на облако -" + ref + "\n\n Ссылка на online кабинет -" + on_line_cabinet)
                bot.send_message(call.message.chat.id, raspis)                                    
                       
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            bot.send_message(call.message.chat.id, "Ошибка при работе с PostgreSQL".format(name = message.text))
        bot.send_message(call.message.chat.id, "Поиск завершен")