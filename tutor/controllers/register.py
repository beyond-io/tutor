from flask import render_template, redirect, url_for, flash
from .forms.registration_form import RegistrationForm
from ..models.users import Users
from .. import db
from flask_login import current_user


def register():
    if current_user.is_authenticated:
        flash('You must logout before registering another user', 'danger')
        return redirect(url_for('courses_route'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = Users.hash_pass(form.password.data)
        user = Users(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('courses_route'))
    return render_template('register.html', form=form)
