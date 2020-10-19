from .. import app
from ..controllers import home, register, login, logout
from flask import flash, request


@app.route('/')
@app.route("/home")
def index_route():
    return home.home()


@app.route("/register", methods=['GET', 'POST'])
def register_route():
    return register.register()


@app.route("/login", methods=['GET', 'POST'])
def login_route():
    return login.login()


@app.route("/flash")
def flash_route():
    flash('Test message', 'success')
    return home.home()


@app.route("/logout")
def logout_route():
    return logout.logout()


@app.route('/user')
def private_route():
    id = request.args.get('id')
    return home.private(id)
