#Bot
TOKEN='Your token'

#sqlconnect
USER="your data"                                
PASSWORD="your data"
HOST="your data"
PORT="your data"
DATABASE="your data"

# notification
my_chat_id = 0000000

# Admin_list
class Admin_user_id():
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name_user = name

Admin_user_0 = Admin_user_id (0000000, "xxxxxxxx")
Admin_user_1 = Admin_user_id (0000000, "xxxxxxxx")
Admin_user_2 = Admin_user_id (0000000, "xxxxxxxx")
Admin_user_3 = Admin_user_id (0000000, "xxxxxxxx")
Admin_user_4 = Admin_user_id (0000000, "xxxxxxxx")

Admin_list = {Admin_user_0.id_user, Admin_user_1.id_user, Admin_user_2.id_user, Admin_user_3.id_user, Admin_user_4.id_user}
