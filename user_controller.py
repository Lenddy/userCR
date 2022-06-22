from users_clases import Users
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)


# home page
@app.route("/")
@app.route("/users")
def display_all_usesr():
    all_users = Users.get_all_users()
    return render_template("all_users.html", all_users=all_users)


# to add a new user
@app.route("/new/user")
def display_new_user():
    return render_template('add_new_user.html')


@app.route("/new/user", methods=["POST"])
def new_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
# you need to put the name of the class and the @classmethod that you are calling
    Users.add_new_user(data)
    return redirect("/users")
