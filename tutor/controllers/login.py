from flask import Flask, Response, render_template, request, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from .. import bcrypt
from flask_login import login_user, current_user
from ..routes import course
from ..models.users import Users

def login():
    if current_user.is_authenticated:
    	flash('You are already logged in.', 'success')
    	return redirect(url_for('get_course_info_route', id=1))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
        	login_user(user, remember=form.remember.data)
        	return redirect(url_for('get_course_info_route', id=1))
        else:
        	flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)