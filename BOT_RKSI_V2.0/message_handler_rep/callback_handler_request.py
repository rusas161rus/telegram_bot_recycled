from sql import sql_delete
from sql import sql_insert
from sql import sql_update
from sql import sql_select


def callback_handler_content(bot, __name__,message):
    if __name__ == '__main__':           
        @bot.callback_query_handler(func = lambda call: True)        
        def answer(call):              
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
                sql_select.select_request_SQL_admin(message, bot, __name__)                
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