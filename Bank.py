import Users

# Initialize the global variables
name = None
user = None
balance = None
current_id = None

# Function to update the global variables based on the provided id
def update(id):
    try:
        global name
        global user
        global current_id
        global balance
        
        # Assign the provided id to the current_id variable
        current_id = id
        
        # Retrieve the user object using the get_user function from the Users module
        user = Users.get_user(int(current_id))
        
        # Assign the user's name and balance to the respective global variables
        name = user.name
        balance = f"{user.get_balance()}"
    except:
        print("failed")