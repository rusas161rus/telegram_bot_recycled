from telebot import types
import pyperclip
import os
from Admin_options import Admin_list_file
from message_handler_rep import pars_web_site_0
from message_handler_rep import pars_web_site_1
from sql import sql_select
from sql import sql_insert
from message_handler_rep import callback_handler_request

Admin_list = {}
user_dict = {}
class User:
    def __init__(self, name):
        self.name = name 

def massege_handler_content(bot, __name__):
    if __name__ == '__main__':    
        @bot.message_handler(content_types = ['text', 'document', 'photo', 'audio', 'video', 'voice'])
        
        def send_text(message):
            try:        
                chat_id = message.chat.id
                name = message.from_user.id
                user = User(name)
                user_dict[chat_id] = user

                if message.text=='Мой-ID':
                    bot.send_message(message.chat.id, "Ваш логин: {0.username} и Ваш ID: {0.id}.".format(message.from_user, bot.get_me(),
                    parse_mode='html'))
                if message.text == 'ЧаВо!':
                    doc = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/ЧаВо.pdf', 'rb')
                    bot.send_document(message.chat.id, doc)
                if message.text == 'скрыть кнопки':                
                    bot.send_message(message.chat.id, 'что бы снова открыть кнопки введи /start', reply_markup=types.ReplyKeyboardRemove())
                    bot.edit_message_reply_markup(message.chat.id, message_id = message.message_id, reply_markup = '')                             
                if message.text=='Сайт РКСИ и Ссылка на Облако, Ссылка на Онлайн кабинеты!':
                    markup=types.InlineKeyboardMarkup(row_width=2)
                    btm_ss_0 = types.InlineKeyboardButton("Облако с Заданиями", url="https://cloud.mail.ru/public/Tb2G/Fuc5s2Sks")
                    btm_ss_1 = types.InlineKeyboardButton("Сайт РКСИ", url="https://www.rksi.ru/schedule")
                    btm_ss_2 = types.InlineKeyboardButton("Онлайн кабинеты", url="https://docs.google.com/spreadsheets/d/1TYqoU3pGHd_u1UWjHV5TaHKOZr_d3nYG1MG0cVKye3Q/view#gid=1185239252")
                    markup.add(btm_ss_0, btm_ss_1, btm_ss_2)
                    bot.send_message(message.chat.id, 'Сайт РКСИ и Ссылка на Облако, Ссылка на Онлайн кабинеты!', reply_markup=markup)
                if message.text=='Памятка по оплате!':
                    markup=types.InlineKeyboardMarkup(row_width=2)
                    btm_sp_0 = types.InlineKeyboardButton("Через МБ", callback_data = 'pamatca0')
                    btm_sp_1 = types.InlineKeyboardButton("Через Терминал", callback_data = 'pamatca1')
                    markup.add(btm_sp_0, btm_sp_1)
                    bot.send_message(message.chat.id, 'Памятка по оплате!', reply_markup=markup)
                    callback_handler_request.callback_handler_content(bot, __name__, message)
                if message.text=='Расписание звонков общее!':
                    markup=types.InlineKeyboardMarkup(row_width=3)
                    btm_spr_0 = types.InlineKeyboardButton("Расписание звонков", callback_data = 'raspis_0')
                    btm_spr_1 = types.InlineKeyboardButton("с учетом кл часов", callback_data = 'raspis_1')
                    btm_spr_2 = types.InlineKeyboardButton("сокращенное", callback_data = 'raspis_2')
                    markup.add(btm_spr_0, btm_spr_1, btm_spr_2)
                    bot.send_message(message.chat.id, 'Расписание звонков общее!', reply_markup=markup)
                    callback_handler_request.callback_handler_content(bot, __name__, message)
                if message.text == 'Расписание с сайта':                         
                    pars_web_site_1.pars_site(__name__)                            
                    with open("pars.txt") as file:
                        data = file.read()
                    os.remove("pars.txt")
                    pyperclip.copy(data)
                    bot.send_message(message.chat.id, 'Расписание с сайта')  
                    bot.send_message(message.chat.id, data)                
                if message.text == 'Обновить расписание в базе':
                    Admin_list_file.sql_admin_check(__name__, message)
                    while True:
                        try:  
                            id_message_user = message.from_user.id                        
                            Admin_list = Admin_list_file.Admin_list
                        except ValueError:
                            print("что то пошло не так") 
                        if id_message_user in Admin_list:
                            sql_insert.sql_insert_funk(bot, __name__, message)
                            break                           
                        if id_message_user not in Admin_list:
                            bot.send_message(message.chat.id, "Что бы обновить расписание нужно быть админом")
                            break
                if message.text == 'Расписание из БД':
                    sql_select.sql_select_funk(bot, __name__, message)
                if message.text == 'Поиск по времени':
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    btmin_s=types.InlineKeyboardButton("По Времени Начала", callback_data = 'nachalo')
                    btmin_p=types.InlineKeyboardButton("По Времени Конца", callback_data = 'conec')
                    markup.add(btmin_s, btmin_p)              
                    bot.send_message(message.chat.id, "Нажмите кнопку!", reply_markup = markup)
                    callback_handler_request.callback_handler_content(bot, __name__, message)
                if message.text == 'Изменить расписание':
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
                            bot.send_message(message.chat.id, "Выберете что хотите отредактировать", reply_markup = markup)                                               
                            callback_handler_request.callback_handler_content(bot, __name__, message)                                                                     
                            break
                        if id_message_user not in Admin_list:
                            bot.send_message(message.chat.id, "Что бы менять расписание нужно быть админом")
                            break

                if message.text == 'Изменить предмет':
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
                            btm_l_1 = types.InlineKeyboardButton("Имя преподователя", callback_data = 'name')
                            btm_l_2 = types.InlineKeyboardButton("Предмет", callback_data = 'predmet')
                            markup.add(btm_l_1, btm_l_2)
                            markup.add(types.InlineKeyboardButton("Почта", callback_data = 'mail'))
                            btm_l_3 = types.InlineKeyboardButton("Телефон", callback_data = 'fone')
                            btm_l_4 = types.InlineKeyboardButton("Ссылка на облако", callback_data = 'ref')
                            btm_l_5 = types.InlineKeyboardButton("Ссылка на онлайн кабинет", callback_data = 'on_line')
                            markup.add(btm_l_3, btm_l_4, btm_l_5)
                            markup.add(types.InlineKeyboardButton("Примечание", callback_data = 'primechanie'))                                                  
                            bot.send_message(message.chat.id, "Выберете что хотите отредактировать", reply_markup = markup)                                               
                            callback_handler_request.callback_handler_content(bot, __name__, message)                                                                     
                            break
                        if id_message_user not in Admin_list:
                            bot.send_message(message.chat.id, "Что бы менять нужно быть админом")
                            break        
                #faq        
                if message.text=='Список преподователей':
                    markup = types.InlineKeyboardMarkup(row_width=3)   
                    btm_p_1 = types.InlineKeyboardButton("Трищук С.А.", callback_data = 'Trichuk')
                    btm_p_2 = types.InlineKeyboardButton("Фищук А.И.", callback_data = 'Fichuk')
                    btm_p_3 = types.InlineKeyboardButton("Болховитина О.И.", callback_data = 'Bolovihina')
                    markup.add(btm_p_1, btm_p_2, btm_p_3)
                    btm_p_4 = types.InlineKeyboardButton("Ужегова Е.А.", callback_data = 'Ygegova')
                    btm_p_5 = types.InlineKeyboardButton("Алябышева С.Н.", callback_data = 'Alibisheva')
                    btm_p_6 = types.InlineKeyboardButton("Видинеева Е.А.", callback_data = 'Vidineeva')
                    markup.add(btm_p_4, btm_p_5, btm_p_6)
                    btm_p_7 = types.InlineKeyboardButton("Задорожный К.А.", callback_data = 'Zadorognii')
                    btm_p_8 = types.InlineKeyboardButton("Мельникова М.В.", callback_data = 'Melnikova')
                    btm_p_9 = types.InlineKeyboardButton("Нецветаева А.Е.", callback_data = 'Necvetaeva')
                    markup.add(btm_p_7, btm_p_8, btm_p_9)
                    btm_p_10 = types.InlineKeyboardButton("Дозорова Е.В.", callback_data = 'Dozorova')
                    btm_p_11 = types.InlineKeyboardButton("Марышева О.В.", callback_data = 'Marisheva')
                    btm_p_12 = types.InlineKeyboardButton("Махеева П.А.", callback_data = 'Maheeva')
                    markup.add(btm_p_10, btm_p_11, btm_p_12)
                    btm_p_13 = types.InlineKeyboardButton("Штерензеер Т.И.", callback_data = 'Shterenzeer')
                    btm_p_14 = types.InlineKeyboardButton("Джалагония М.Ш.", callback_data = 'Dgalagonia')                        
                    markup.add(btm_p_13, btm_p_14)                                                                          
                    bot.send_message(message.chat.id, "Выберете фамилию", reply_markup = markup)                                               
                    callback_handler_request.callback_handler_content(bot, __name__, message)   

                if message.text=='Список предметов':
                    markup = types.InlineKeyboardMarkup(row_width=1)   
                    btm_pp_1 = types.InlineKeyboardButton("Архитектура компьютерных систем", callback_data = 'Arhitectur')
                    btm_pp_2 = types.InlineKeyboardButton("Стандартизация и сертификация", callback_data = 'Standart_sert')
                    btm_pp_3 = types.InlineKeyboardButton("БЖД", callback_data = 'bgd')                
                    btm_pp_4 = types.InlineKeyboardButton("Иностранный язык", callback_data = 'language')
                    btm_pp_5 = types.InlineKeyboardButton("Информационные технологии", callback_data = 'inform_teh')
                    btm_pp_6 = types.InlineKeyboardButton("История", callback_data = 'history')               
                    btm_pp_7 = types.InlineKeyboardButton("Операцинные системы", callback_data = 'system')
                    btm_pp_8 = types.InlineKeyboardButton("Основы WEB-технологий", callback_data = 'web')
                    btm_pp_9 = types.InlineKeyboardButton("Основы Алгоритмов [python]", callback_data = 'algoritmy')               
                    btm_pp_10 = types.InlineKeyboardButton("Основы кибернетики", callback_data = 'kibernetic')
                    btm_pp_11 = types.InlineKeyboardButton("Психология", callback_data = 'psihology')
                    btm_pp_12 = types.InlineKeyboardButton("Физкультура", callback_data = 'fiz_ra')             
                    btm_pp_13 = types.InlineKeyboardButton("Экономика отрасли", callback_data = 'aconomy')
                    btm_pp_14 = types.InlineKeyboardButton("Элементы высшей математики", callback_data = 'vishei_matematic')
                    btm_pp_15 = types.InlineKeyboardButton("Дискретная математика", callback_data = 'diskret_matematic')             
                    btm_pp_16 = types.InlineKeyboardButton("Теория вероятности", callback_data = 'troria_veroatnosty')
                    btm_pp_17 = types.InlineKeyboardButton("Численные методы", callback_data = 'chislennii_metod')                        
                    markup.add(btm_pp_1, btm_pp_2, btm_pp_3, btm_pp_4, btm_pp_5, btm_pp_6, btm_pp_7, btm_pp_8, btm_pp_9, btm_pp_10, btm_pp_11, btm_pp_12, btm_pp_13, btm_pp_14, btm_pp_15, btm_pp_16, btm_pp_17)                                                                          
                    bot.send_message(message.chat.id, "Выберете предмет", reply_markup = markup)                                               
                    callback_handler_request.callback_handler_content(bot, __name__, message)                                                                                                                                       
                   
            except Exception as e:
                bot.reply_to(message, 'oooops')