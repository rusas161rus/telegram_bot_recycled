#Bot
TOKEN='5771211381:AAE5n5qtUS0SRMBpvboM_vtwdUIbQxLu5y4'

#sqlconnect
USER="postgres"                                
PASSWORD="657834"
HOST="localhost"
PORT="5432"
DATABASE="BOT_TEL_TEST"

# notification
my_chat_id = -680891031

# Admin_list
class Admin_user_id():
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name_user = name

Admin_user_0 = Admin_user_id (648841533, "Вова")
Admin_user_1 = Admin_user_id (658118472, "Руслан")
Admin_user_2 = Admin_user_id (8350493, "Анатолий")
Admin_user_3 = Admin_user_id (0000000, "xxxxxxxx")
Admin_user_4 = Admin_user_id (0000000, "xxxxxxxx")

Admin_list = {Admin_user_0.id_user, Admin_user_1.id_user, Admin_user_2.id_user, Admin_user_3.id_user, Admin_user_4.id_user}