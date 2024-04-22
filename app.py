import Bank
import Users
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    form_id = request.form.get("id")
    form_name = request.form.get("name")
    try:
        # Check if the submitted user information is valid
        if (int(form_id) == Users.get_user(int(form_id)).id and form_name == Users.get_user(int(form_id)).name):
            # Redirect to the user's account page
            return redirect(f"/{form_id}")
        else:
            # Return an error message and redirect back to the home page
            return "Invalid user<script>setTimeout(function() {window.location.replace('/');}, 1000);</script>"
    except Exception as e:
        return "invalid choice"
@app.route("/<id>")
def page(id):
    # Update the Bank module with the current user's information
    Bank.update(id)
    
    # Render the account page template with the user's balance, id, and name
    return render_template("bank.html", balance=Bank.balance, id=Bank.current_id, name=Bank.name)

@app.route("/<id>/withdraw/<amount>")
def withdraw(id, amount):
    # Update the Bank module with the current user's information
    Bank.update(id)
    
    # Withdraw the specified amount from the user's account
    Bank.user.withdraw(float(amount))
    
    # Redirect back to the user's account page
    return redirect(f"/{id}")

@app.route("/<id>/deposit/<amount>")
def deposit(id, amount):
    # Update the Bank module with the current user's information
    Bank.update(id)
    
    # Deposit the specified amount into the user's account
    Bank.user.deposit(float(amount))
    
    # Redirect back to the user's account page
    return redirect(f"/{id}")

@app.route("/create_account", methods=['POST'])
def create_account():
    form_name = request.form.get("name")
    
    # Create a new user account with the provided name and a balance of 0
    Users.create_user(form_name, 0)
    
    # Return a success message and redirect back to the home page
    return "Account created successfully!<script>setTimeout(function() {window.location.replace('/');}, 1000);</script>"

@app.route("/close_account", methods=['POST'])
def close_account():
    id = request.form.get("id")
    
    # Close the user account with the provided id
    Users.close_user(id)
    
    # Return a success message and redirect back to the home page
    return "Account closed successfully!<script>setTimeout(function() {window.location.replace('/');}, 1000);</script>"

if __name__ == '__main__':
    app.run()