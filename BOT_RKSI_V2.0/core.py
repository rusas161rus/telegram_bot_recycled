import requests as requests
import config
import telebot
import logging
from telebot import types
import schedule
from threading import Thread
import time
from time import sleep
from message_handler_rep import message_handler_text
from Admin_options  import message_handler_admin


logger=telebot.logger
telebot.logger.setLevel(logging.DEBUG)
logging.basicConfig(filename="fullsearch.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot=telebot.TeleBot(config.TOKEN)

my_chat_id = config.my_chat_id

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(my_chat_id, "Звонок через 10 минут")
if __name__ == "__main__":
    #schedule.every().day.at("07:50:00").do(function_to_run)
    #schedule.every().day.at("09:30:00").do(function_to_run)
    #schedule.every().day.at("11:20:00").do(function_to_run)
    #schedule.every().day.at("13:00:00").do(function_to_run)
    #schedule.every().day.at("14:50:00").do(function_to_run)
    #schedule.every().day.at("16:30:00").do(function_to_run) 
    #schedule.every().day.at("18:10:00").do(function_to_run)    
    Thread(target=schedule_checker).start() 

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, данный бот призван облегчить твое взаимодействие с колледжом РКСИ.\nНапоминанаю, что при нажатии кнопки меню слева или если ввести в поле ввода сообщения слеш откроется меню с 3 вариантами:\n/raspisanie - покажет актуальное расписание нашей группы\n/admin_menu - если ты не админ то туда не нажимай\n/faq - здесь актуальная информация по преподователям и предметам, а так же ссылки на облако')

@bot.message_handler(commands = ['raspisanie'])
def button(message):        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)    
    btm4 = types.KeyboardButton('Расписание с сайта')    
    btm1 = types.KeyboardButton('Расписание из БД')    
    btm5 = types.KeyboardButton('Поиск по времени')       
    markup.add(btm4, btm1, btm5)
    btm20 = types.KeyboardButton('Расписание звонков общее!')
    markup.add(btm20)    
    bot.send_message(message.chat.id, 'Бот запущен!', reply_markup = markup)

@bot.message_handler(commands = ['admin_menu'])
def button(message):        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)     
    btm3 = types.KeyboardButton('Обновить расписание в базе')
    btm2 = types.KeyboardButton('Изменить расписание')
    btm4 = types.KeyboardButton('Изменить предмет')               
    markup.add(btm3, btm2, btm4)
    btm7 = types.KeyboardButton('Администрация')        
    markup.add(btm7)    
    bot.send_message(message.chat.id, 'Бот запущен!', reply_markup = markup)

@bot.message_handler(commands = ['faq'])
def button(message):        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btm6 = types.KeyboardButton('Сайт РКСИ и Ссылка на Облако, Ссылка на Онлайн кабинеты!')
    markup.add(btm6)     
    btm9 = types.KeyboardButton('Список преподователей')    
    btm10 = types.KeyboardButton('Список предметов')              
    btm11 = types.KeyboardButton('ЧаВо!')
    btm12 = types.KeyboardButton('Памятка по оплате!') 
    markup.add(btm9, btm10, btm11, btm12)
    btm8 = types.KeyboardButton('Мой-ID')
    markup.add(btm8)
    bot.send_message(message.chat.id, 'Бот запущен!', reply_markup = markup)


message_handler_admin.massege_handler_content_admin(bot, __name__)
message_handler_text.massege_handler_content(bot, __name__)

if __name__=='__main__':
   while True:
        
    try:
        bot.polling(none_stop=True, timeout=30)
    except Exception as e:
        time.sleep(3)
        print(e)