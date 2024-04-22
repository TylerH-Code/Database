import Sql

# Define the User class
class User:
    def __init__(self, id, name, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def get_balance(self):
        # Retrieve the balance from the SQL table for the user
        self.balance = Sql.execute(f"SELECT balance FROM data WHERE id={self.id}")[0][0]
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            # Deduct the specified amount from the user's balance
            self.balance -= amount
            print(f"b:{self.balance} {self.id}")

            # Update the SQL table with the new balance
            Sql.retreive(f"UPDATE data SET balance = {self.balance} WHERE id = {self.id};")
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            # Add the specified amount to the user's balance
            self.balance += amount

            # Update the SQL table with the new balance
            Sql.retreive(f"UPDATE data SET balance = {self.balance} WHERE id = {self.id};")
            return True
        else:
            return False


# Retrieve the list of users from the SQL table
user_list = Sql.execute("SELECT * FROM data")
new_list = []

# Create User objects for each user in the list
for user in user_list:
    new_list.append(User(user[0], user[1], user[2]))


# Function to get all users
def get_users():
    return new_list


# Function to get a specific user by their ID
def get_user(id):
    for user in new_list:
        if id == user.id:
            print(user.id)
            return user


# Function to create a new user
def create_user(name, balance):
    sql_query = f"INSERT INTO data (name, balance) VALUES ('{name}', {balance})"
    Sql.retreive(sql_query)


# Function to delete a user
def close_user(user_id):
    sql_query = f"DELETE FROM data WHERE id={user_id}"
    Sql.retreive(sql_query)