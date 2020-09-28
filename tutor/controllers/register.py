from flask import render_template, redirect, url_for
from .forms import RegistrationForm


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('index_route'))
    return render_template('register.html', form=form)
