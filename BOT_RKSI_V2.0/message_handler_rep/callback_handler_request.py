from message_handler_rep import funk
from sql import sql_delete
from sql import sql_insert
from sql import sql_update
from sql import sql_select
from sql import sql_select_prepod
from sql import sql_seleqt_predmet
from sql import sql_update_predmet



def callback_handler_content(bot, __name__,message):
    if __name__ == '__main__':           
        @bot.callback_query_handler(func = lambda call: True)        
        def answer(call):
            if call.data == 'pamatca0': # МБ                                                     
                funk.pamatka0(bot, message, __name__, call)                
            if call.data == 'pamatca1': # Терминал      
                funk.pamatka1(bot, message, __name__, call)

            if call.data == 'raspis_0': # просто расписание                                                     
                funk.raspis_0(bot, message, __name__, call)                
            if call.data == 'raspis_1': # с учетом кл часов      
                funk.raspis_1(bot, message, __name__, call)
            if call.data == 'raspis_2': # Сокращённое      
                funk.raspis_2(bot, message, __name__, call)                 
                                              
            if call.data == 'a': # Время Начала                                                     
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                                               
                bot.register_next_step_handler(msg, create_request_message_0)                
            if call.data == 'b': # Время Конца      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_1)
            if call.data == 'c': # Дата      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_2)
            if call.data == 'd': # Предмет      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_3)
            if call.data == 'e': # Учитель      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_4)
            if call.data == 'f': # Кабинет     
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")               
                bot.register_next_step_handler(msg, create_request_message_5)
            if call.data == 'g': # Удалить запись      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_delete_1s)
            if call.data == 'k': # Создать целую запись       
                msg = bot.send_message(call.message.chat.id, "Введите дату в формате гггг-мм-дд")                
                bot.register_next_step_handler(msg, create_insrt_request_message_0)
            if call.data == 'admin_a': # Список админов                                 
                sql_select.select_request_SQL_admin(message, bot, __name__, call)                
            if call.data == 'admin_b': # Добавить админов
                msg = bot.send_message(call.message.chat.id, "Введите ИД")                
                bot.register_next_step_handler(msg, create_insrt_request_admin_message_0)
            if call.data == 'admin_c': # Удалить админов
                msg = bot.send_message(call.message.chat.id, "Введите номер записи")                
                bot.register_next_step_handler(msg, create_request_admin_delete_1s) 

            if call.data == 'nachalo': # Поиск по времени          
                msg = bot.send_message(call.message.chat.id, "Введите время начала с в формате хх:хх")
                bot.register_next_step_handler(msg, create_select_request_message_0)
            if call.data == 'conec':   # Поиск по времени       
                msg = bot.send_message(call.message.chat.id, "Введите время конца с в формате хх:хх")
                bot.register_next_step_handler(msg, create_select_request_message_1)

            # Добавление по 1 параметру для предметов и преподов
            if call.data == 'name': # Имя учителя                                                    
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                                               
                bot.register_next_step_handler(msg, create_request_message_predmet_0)                
            if call.data == 'predmet': # Предмет      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_predmet_1)
            if call.data == 'mail': # Почта      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_predmet_2)
            if call.data == 'fone': # Телефон      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_predmet_3)
            if call.data == 'ref': # Ссылка на облако      
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")                
                bot.register_next_step_handler(msg, create_request_message_predmet_4)
            if call.data == 'on_line': # Онлайн кабинет     
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")               
                bot.register_next_step_handler(msg, create_request_message_predmet_5)
            if call.data == 'primechanie': # Примечание     
                msg = bot.send_message(call.message.chat.id, "Введите ИД записи")               
                bot.register_next_step_handler(msg, create_request_message_predmet_6)             

            if call.data == 'Trichuk': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Trichuk(bot, __name__, message, call)
            if call.data == 'Fichuk': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Fichuk(bot, __name__, message, call)
            if call.data == 'Ygegova': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Ygegova(bot, __name__, message, call)
            if call.data == 'Alibisheva': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Alibisheva(bot, __name__, message, call)
            if call.data == 'Vidineeva': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Vidineeva(bot, __name__, message, call)
            if call.data == 'Zadorognii': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Zadorognii(bot, __name__, message, call)
            if call.data == 'Melnikova': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Melnikova(bot, __name__, message, call)
            if call.data == 'Necvetaeva': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Necvetaeva(bot, __name__, message, call)
            if call.data == 'Dozorova': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Dozorova(bot, __name__, message, call)
            if call.data == 'Marisheva': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Marisheva(bot, __name__, message, call)
            if call.data == 'Maheeva': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Maheeva(bot, __name__, message, call)
            if call.data == 'Dgalagonia': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Dgalagonia(bot, __name__, message, call)
            if call.data == 'Shterenzeer': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Shterenzeer(bot, __name__, message, call)
            if call.data == 'Bolovihina': # Поиск по фамилии без ввода          
                sql_select_prepod.sql_select_funk_Bolovihina(bot, __name__, message, call)

            if call.data == 'Arhitectur': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_Arhitectur(bot, __name__, message, call)
            if call.data == 'Standart_sert': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_Standart_sert(bot, __name__, message, call)
            if call.data == 'bgd': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_bgd(bot, __name__, message, call)
            if call.data == 'language': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_language(bot, __name__, message, call)
            if call.data == 'inform_teh': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_inform_teh(bot, __name__, message, call)
            if call.data == 'history': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_history(bot, __name__, message, call)
            if call.data == 'system': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_system(bot, __name__, message, call)
            if call.data == 'web': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_web(bot, __name__, message, call)
            if call.data == 'algoritmy': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_algoritmy(bot, __name__, message, call)
            if call.data == 'kibernetic': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_kibernetic(bot, __name__, message, call)
            if call.data == 'psihology': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_psihology(bot, __name__, message, call)
            if call.data == 'fiz_ra': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_fiz_ra(bot, __name__, message, call)
            if call.data == 'aconomy': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_aconomy(bot, __name__, message, call)
            if call.data == 'vishei_matematic': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_vishei_matematic(bot, __name__, message, call)
            if call.data == 'diskret_matematic': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_diskret_matematic(bot, __name__, message, call)
            if call.data == 'troria_veroatnosty': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_troria_veroatnosty(bot, __name__, message, call)
            if call.data == 'chislennii_metod': # Поиск по предмету без ввода          
                sql_seleqt_predmet.sql_select_funk_chislennii_metod(bot, __name__, message, call)            

        # Поиск по времени                  
        def create_select_request_message_0(message):
            global text_select_ts_0
            text_select_ts_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите время начала по в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, select_request_SQL_ss_0)
        def create_select_request_message_1(message):
            global text_select_tp_0
            text_select_tp_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите время конца по в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, select_request_SQL_ss_1)

        def select_request_SQL_ss_0(message):
            global text_select_ts_1
            text_select_ts_1 = message.text                       
            sql_select.select_request_SQL_s_0(message, bot, __name__, text_select_ts_0, text_select_ts_1)
        def select_request_SQL_ss_1(message):
            global text_select_tp_1
            text_select_tp_1 = message.text                      
            sql_select.select_request_SQL_s_1(message, bot, __name__, text_select_tp_0, text_select_tp_1)

        # Для удаления
        def create_request_delete_1s(message):
            sql_delete.create_request_delete_1(message, bot, __name__)
        # Для удаления
        def create_request_admin_delete_1s(message):
            sql_delete.create_request_admin_delete_1(message, bot, __name__)

        # Добавление по 1 параметру для предметов и преподов
        def create_request_message_predmet_0(message):
            global text_predmet_0
            text_predmet_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите ФИО преподователя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet0)
        def create_request_SQL_predmet0(message):                                   
            sql_update_predmet.create_request_SQL_predmet0(message, bot, __name__, text_predmet_0)
        def create_request_message_predmet_1(message):
            global text_predmet_1
            text_predmet_1 = message.text
            msg=bot.send_message(message.chat.id, "Введите название урока".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet1)
        def create_request_SQL_predmet1(message):                                   
            sql_update_predmet.create_request_SQL_predmet1(message, bot, __name__, text_predmet_1)
        def create_request_message_predmet_2(message):
            global text_predmet_2
            text_predmet_2 = message.text
            msg=bot.send_message(message.chat.id, "Введите почту преподователя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet2)
        def create_request_SQL_predmet2(message):                                   
            sql_update_predmet.create_request_SQL_predmet2(message, bot, __name__, text_predmet_2)
        def create_request_message_predmet_3(message):
            global text_predmet_3
            text_predmet_3 = message.text
            msg=bot.send_message(message.chat.id, "Введите телефон преподователя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet3)
        def create_request_SQL_predmet3(message):                                   
            sql_update_predmet.create_request_SQL_predmet3(message, bot, __name__, text_predmet_3)
        def create_request_message_predmet_4(message):
            global text_predmet_4
            text_predmet_4 = message.text
            msg=bot.send_message(message.chat.id, "Введите ссылку на облако".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet4)
        def create_request_SQL_predmet4(message):                                   
            sql_update_predmet.create_request_SQL_predmet4(message, bot, __name__, text_predmet_4)
        def create_request_message_predmet_5(message):
            global text_predmet_5
            text_predmet_5 = message.text
            msg=bot.send_message(message.chat.id, "Введите ссылку на онлайн кабинет".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet5)
        def create_request_SQL_predmet5(message):                                   
            sql_update_predmet.create_request_SQL_predmet5(message, bot, __name__, text_predmet_5)
        def create_request_message_predmet_6(message):
            global text_predmet_6
            text_predmet_6 = message.text
            msg=bot.send_message(message.chat.id, "Введите примечание".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_predmet6)
        def create_request_SQL_predmet6(message):                                   
            sql_update_predmet.create_request_SQL_predmet6(message, bot, __name__, text_predmet_6)

        # Добавление по 1 параметру
        def create_request_message_0(message):
            global text_0
            text_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите время начала в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s0)
        def create_request_SQL_s0(message):                                   
            sql_update.create_request_SQL_ss0(message, bot, __name__, text_0)
        def create_request_message_1(message):
            global text_1
            text_1 = message.text
            msg=bot.send_message(message.chat.id, "Введите время конца в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s1)
        def create_request_SQL_s1(message):                                   
            sql_update.create_request_SQL_ss1(message, bot, __name__, text_1)
        def create_request_message_2(message):
            global text_2
            text_2 = message.text
            msg=bot.send_message(message.chat.id, "Введите дату в формате гггг-мм-дд".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s2)
        def create_request_SQL_s2(message):                                   
            sql_update.create_request_SQL_ss2(message, bot, __name__, text_2)
        def create_request_message_3(message):
            global text_3
            text_3 = message.text
            msg=bot.send_message(message.chat.id, "Введите название урока".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s3)
        def create_request_SQL_s3(message):                                   
            sql_update.create_request_SQL_ss3(message, bot, __name__, text_3)
        def create_request_message_4(message):
            global text_4
            text_4 = message.text
            msg=bot.send_message(message.chat.id, "Введите Имя преподователя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s4)
        def create_request_SQL_s4(message):                                   
            sql_update.create_request_SQL_ss4(message, bot, __name__, text_4)
        def create_request_message_5(message):
            global text_5
            text_5 = message.text
            msg=bot.send_message(message.chat.id, "Введите № кабинета".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s5)
        def create_request_SQL_s5(message):                                   
            sql_update.create_request_SQL_ss5(message, bot, __name__, text_5)

        # Функция пошагового добавления записи расписания       
        def create_insrt_request_message_0(message):
            global text_insert_0
            text_insert_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите время начала в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_message_s0)
        def create_insrt_request_message_s0(message):
            global text_insert_1
            text_insert_1 = message.text
            msg=bot.send_message(message.chat.id, "Введите время конца в формате хх:хх".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_message_s1)
        def create_insrt_request_message_s1(message):
            global text_insert_2
            text_insert_2 = message.text
            msg=bot.send_message(message.chat.id, "Введите название урока".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_message_s2)
        def create_insrt_request_message_s2(message):
            global text_insert_3
            text_insert_3 = message.text
            msg=bot.send_message(message.chat.id, "Введите Имя преподователя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_message_s3)
        def create_insrt_request_message_s3(message):
            global text_insert_4
            text_insert_4 = message.text
            msg=bot.send_message(message.chat.id, "Введите № кабинета".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_SQL_s6)

        def create_request_SQL_s6(message):
            global text_insert_5
            text_insert_5 = message.text                       
            sql_insert.create_request_SQL_ss6(message, bot, __name__, text_insert_0, text_insert_1, text_insert_2, text_insert_3, text_insert_4, text_insert_5)
        
        # Функция пошагового добавления записи админа
        def create_insrt_request_admin_message_0(message):
            global text_admin_insert_0
            text_admin_insert_0 = message.text
            msg=bot.send_message(message.chat.id, "Введите Имя".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_admin_message_s0)
        def create_insrt_request_admin_message_s0(message):
            global text_admin_insert_1
            text_admin_insert_1 = message.text
            msg=bot.send_message(message.chat.id, "Введите Фамилию".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_admin_message_s1)
        def create_insrt_request_admin_message_s1(message):
            global text_admin_insert_2
            text_admin_insert_2 = message.text
            msg=bot.send_message(message.chat.id, "Введите Отчестов".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_insrt_request_admin_message_s2)
        def create_insrt_request_admin_message_s2(message):
            global text_admin_insert_3
            text_admin_insert_3 = message.text
            msg=bot.send_message(message.chat.id, "Примечание".format(message.from_user, bot.get_me()),
            parse_mode = 'html')            
            bot.register_next_step_handler(msg, create_request_admin_SQL_s6)        

        def create_request_admin_SQL_s6(message):
            global text_admin_insert_4
            text_admin_insert_4 = message.text                       
            sql_insert.create_request_admin_SQL_ss6(message, bot, __name__, text_admin_insert_0, text_admin_insert_1, text_admin_insert_2, text_admin_insert_3, text_admin_insert_4)