from telebot import types
from message_handler_rep import callback_handler_1_request
from Admin_options import Admin_list_file




def massege_handler_content_admin(bot, __name__):
    if __name__ == '__main__':    
        @bot.message_handler(func=lambda message: message.text == "Администрация")

        def send_text(message):            
            if message.text == 'Администрация':
                Admin_list_file.sql_admin_check(__name__, message)                
                while True:                    
                    try:                                       
                        id_message_user = message.from_user.id                        
                        Admin_list = Admin_list_file.Admin_list
                    except ValueError:
                        print("что то пошло не так")                        
                        continue                    
                    if id_message_user in Admin_list: 
                        markup = types.InlineKeyboardMarkup(row_width=3)
                        markup.add(types.InlineKeyboardButton("Список Админов", callback_data = 'admin_a'))
                        btm_l_1 = types.InlineKeyboardButton("Добавить Админа", callback_data = 'admin_b')
                        btm_l_2 = types.InlineKeyboardButton("Удалить Админа", callback_data = 'admin_c')
                        markup.add(btm_l_1, btm_l_2)          
                        bot.send_message(message.chat.id, "Ваши действия?", reply_markup = markup)
                        callback_handler_1_request.callback_handler_0_content(bot, __name__, message)
                        break                    
                    if id_message_user not in Admin_list:
                        bot.send_message(message.chat.id, "Вход только по пропускам")
                        break   