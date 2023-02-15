from telebot import types
import pyperclip
import config
from message_handler_rep import pars_web_site
from sql import sql_select
from sql import sql_insert
from message_handler_rep import callback_handler_0_request
from message_handler_rep import callback_handler_1_request

Admin_list = config.Admin_list

def massege_handler_content(bot, __name__):
    if __name__ == '__main__':    
        @bot.message_handler(content_types = ['text', 'document', 'photo', 'audio', 'video', 'voice'])
        
        def send_text(message):            
            if message.text=='Сайт РКСИ и Ссылка на Облако с заданиями':
                markup=types.InlineKeyboardMarkup(row_width=2)
                btm_ss_0 = types.InlineKeyboardButton("Облако с Заданиями", url="https://cloud.mail.ru/public/Tb2G/Fuc5s2Sks")
                btm_ss_1 = types.InlineKeyboardButton("Сайт РКСИ", url="https://www.rksi.ru/schedule")
                markup.add(btm_ss_0, btm_ss_1)
                bot.send_message(message.chat.id, 'Сайт РКСИ и Ссылка на Облако с заданиями!', reply_markup=markup)
            if message.text == 'Расписание с сайта РКСИ':                         
                pars_web_site.pars_site(__name__)                            
                with open("pars.txt") as file:
                    data = file.read()
                pyperclip.copy(data)  
                bot.send_message(message.chat.id, data)
            if message.text == 'Обновить расписание в базе':
                while True:
                    try:  
                        id_message_user = message.from_user.id
                    except ValueError:
                        print("Обновить расписание в базе") 
                    if id_message_user in Admin_list:
                        sql_insert.sql_insert_funk(bot, __name__, message)
                        break                           
                    if id_message_user not in Admin_list:
                        bot.send_message(message.chat.id, "Что бы обновить расписание нужно быть админом")
                        break
            if message.text == 'Расписание':
                sql_select.sql_select_funk(bot, __name__, message)
            if message.text == 'Поиск по времени':
                markup = types.InlineKeyboardMarkup(row_width=2)
                btmin_s=types.InlineKeyboardButton("По Времени Начала", callback_data = 'nachalo')
                btmin_p=types.InlineKeyboardButton("По Времени Конца", callback_data = 'conec')
                markup.add(btmin_s, btmin_p)              
                bot.send_message(message.chat.id, "Нажмите кнопку!", reply_markup = markup)
                callback_handler_0_request.callback_handler_0_content(bot, __name__)
            if message.text == 'Изменить расписание':
                while True:
                    try:                
                        id_message_user = message.from_user.id                                                           
                    except ValueError:
                        print("что то пошло не так")                        
                        continue        
                    if id_message_user in Admin_list:
                        markup = types.InlineKeyboardMarkup(row_width=3)
                        markup.add(types.InlineKeyboardButton("Создать целую запись", callback_data = 'k'))
                        btm_l_1 = types.InlineKeyboardButton("Время Начала", callback_data = 'a')
                        btm_l_2 = types.InlineKeyboardButton("Время Конца", callback_data = 'b')
                        markup.add(btm_l_1, btm_l_2)
                        markup.add(types.InlineKeyboardButton("Дата", callback_data = 'c'))
                        btm_l_3 = types.InlineKeyboardButton("Предмет", callback_data = 'd')
                        btm_l_4 = types.InlineKeyboardButton("Учитель", callback_data = 'e')
                        btm_l_5 = types.InlineKeyboardButton("Кабинет", callback_data = 'f')
                        markup.add(btm_l_3, btm_l_4, btm_l_5)
                        markup.add(types.InlineKeyboardButton("Удалить запись", callback_data = 'g')) 
                        #markup.add(types.InlineKeyboardButton("Обновить целую запись", callback_data = 'l'))    
                        bot.send_message(message.chat.id, "Выберете что хотите отредактировать", reply_markup = markup)
                        callback_handler_1_request.callback_handler_0_content(bot, __name__, message)
                        break
                    if id_message_user not in Admin_list:
                        bot.send_message(message.chat.id, "Что бы менять расписание нужно быть админом")
                        break   