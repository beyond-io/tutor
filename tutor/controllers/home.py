from flask import render_template
from tutor.models.users import Users


def home():
    return render_template('index.html')


def private(id):
    user = Users.query.filter_by(id=id).first()
    username = user.username
    favorites = user.favorites
    return render_template('private.html', username=username,
                           favorites=favorites)
