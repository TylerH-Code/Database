import Sql


class User:
    def __init__(self, id, name, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def get_balance(self):
        self.balance = Sql.execute(
            f"SELECT balance FROM data WHERE id={self.id}")[0][0]
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"b:{self.balance} {self.id}")
            # Update the SQL table with the new balance
            Sql.retreive(
                f"UPDATE data SET balance = {self.balance} WHERE id = {self.id};")

            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # Update the SQL table with the new balance
            Sql.retreive(
                f"UPDATE data SET balance = {self.balance} WHERE id = {self.id};")
            return True
        else:
            return False


list = Sql.execute("select * from data")
new_list = []
for user in list:
    new_list.append(User(user[0], user[1], user[2]))


def get_users():
    return new_list


def get_user(id):
    for user in new_list:
        if id == user.id:
            print(user.id)
            return user


print(get_user(5).id)
