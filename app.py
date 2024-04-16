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
    if (int(form_id) == Users.get_user(int(form_id)).id and form_name == Users.get_user(int(form_id)).name):
        return redirect(f"/{form_id}")
    else:
        return "Invalid user<script>setTimeout(function() {window.location.replace('/');}, 1000);</script>"


@app.route("/<id>")
def page(id):
    Bank.update(id)
    return render_template("bank.html", balance=Bank.balance, id=Bank.current_id, name=Bank.name)


@app.route("/<id>/withdraw/<amount>")
def withdraw(id, amount):
    Bank.update(id)
    Bank.user.withdraw(float(amount))
    return redirect(f"/{id}")


@app.route("/<id>/deposit/<amount>")
def deposit(id, amount):
    Bank.update(id)
    Bank.user.deposit(float(amount))
    return redirect(f"/{id}")


if __name__ == '__main__':
    app.run()
