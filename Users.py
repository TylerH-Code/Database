import Sql
import Users


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


list = Sql.exucute("select * from users")
new_list = []
for user in list:
    new_list.append(Users.User(user[0], user[1]))

def get_users():
    return new_list