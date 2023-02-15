from sql import sql_select

def callback_handler_0_content(bot, __name__):
    if __name__ == '__main__':    
        @bot.callback_query_handler(func = lambda call: True)
        def answer(call):  
            if call.data == 'nachalo':        
                msg = bot.send_message(call.message.chat.id, "Введите время начала с в формате хх:хх")
                bot.register_next_step_handler(msg, create_select_request_message_0)
            if call.data == 'conec':        
                msg = bot.send_message(call.message.chat.id, "Введите время конца с в формате хх:хх")
                bot.register_next_step_handler(msg, create_select_request_message_1)
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