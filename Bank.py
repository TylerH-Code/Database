import Users
name = None
user = None
balance = None
current_id = None


def update(id):
    try:
        global name
        global user
        global current_id
        global balance
        current_id = id
        user = Users.get_user(int(current_id))
        name = user.name
        balance = f"{user.get_balance()}"
    except:
        print("failed")
