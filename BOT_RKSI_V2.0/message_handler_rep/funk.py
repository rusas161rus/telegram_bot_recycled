def pamatka0(bot, message, __name__, call):
    if __name__ == '__main__':  
        doc = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/РКСИ_памятка_по_оплате_обучения_через_МБ.pdf', 'rb')
        bot.send_document(call.message.chat.id, doc) 
def pamatka1(bot, message, __name__, call):
    if __name__ == '__main__':  
        doc = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/РКСИ_памятка_по_оплате_обучения_через_терминал.pdf', 'rb')
        bot.send_document(call.message.chat.id, doc) 
def raspis_0(bot, message, __name__, call):
    if __name__ == '__main__':  
        photo = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/Расписание звонков.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo) 
def raspis_1(bot, message, __name__, call):
    if __name__ == '__main__':  
        photo = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/Расписание звонков с учетом кл часов.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo) 
def raspis_2(bot, message, __name__, call):
    if __name__ == '__main__':  
        photo = open('C:/Users/rusas/Desktop/dev_chernovik/Portfolio/BOT_RKSI_V2.0/DATA/Расписание звонков сокращенное.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo) 

