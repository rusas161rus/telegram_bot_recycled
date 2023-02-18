import requests as requests
import config
import telebot
import logging
from telebot import types
import schedule
from threading import Thread
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
    schedule.every().day.at("07:50:00").do(function_to_run)
    schedule.every().day.at("09:30:00").do(function_to_run)
    schedule.every().day.at("11:20:00").do(function_to_run)
    schedule.every().day.at("13:00:00").do(function_to_run)
    schedule.every().day.at("14:50:00").do(function_to_run)
    schedule.every().day.at("16:30:00").do(function_to_run) 
    schedule.every().day.at("18:10:00").do(function_to_run)    
    Thread(target=schedule_checker).start() 

message_handler_admin.massege_handler_content_admin(bot, __name__)
message_handler_text.massege_handler_content(bot, __name__)



    
if __name__=='__main__':
   bot.polling(none_stop=True, timeout=30)
