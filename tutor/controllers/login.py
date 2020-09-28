from flask import render_template, redirect, url_for
from .forms import LoginForm


def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index_route'))
    return render_template('login.html', form=form)
