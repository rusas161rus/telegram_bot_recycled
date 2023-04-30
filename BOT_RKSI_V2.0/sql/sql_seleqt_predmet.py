from psycopg2 import Error
import psycopg2
import config

connection = psycopg2.connect(  user = config.USER, 
                                password = config.PASSWORD, 
                                host = config.HOST, 
                                port = config.PORT, 
                                database = config.DATABASE)

def sql_select_funk_Arhitectur(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Архитектура компьютерных систем'".format(message.text))
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

def sql_select_funk_Standart_sert(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Стандартизация и сертификация'".format(message.text))
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

def sql_select_funk_bgd(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'БЖД'".format(message.text))
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

def sql_select_funk_language(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Иностранный язык'".format(message.text))
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

def sql_select_funk_inform_teh(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Информационные технологии'".format(message.text))
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

def sql_select_funk_history(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'История'".format(message.text))
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

def sql_select_funk_system(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Операцинные системы'".format(message.text))
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

def sql_select_funk_web(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Основы WEB-технологий'".format(message.text))
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

def sql_select_funk_algoritmy(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Основы Алгоритмов [python]'".format(message.text))
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

def sql_select_funk_kibernetic(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Основы кибернетики'".format(message.text))
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

def sql_select_funk_psihology(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Психология'".format(message.text))
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

def sql_select_funk_fiz_ra(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Физкультура'".format(message.text))
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

def sql_select_funk_aconomy(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Экономика отрасли'".format(message.text))
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

def sql_select_funk_vishei_matematic(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Элементы высшей математики'".format(message.text))
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

def sql_select_funk_diskret_matematic(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Дискретная математика'".format(message.text))
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

def sql_select_funk_troria_veroatnosty(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Теория вероятности'".format(message.text))
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

def sql_select_funk_chislennii_metod(bot, __name__, message, call):
    if __name__ == '__main__':        
        try:             
            cursor = connection.cursor()                              
            cursor.execute("SELECT * from PREPODOVATEL_TABLE WHERE PREDMET = 'Численные методы'".format(message.text))
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