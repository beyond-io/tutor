from flask import Flask, Response, render_template, request, redirect, url_for
from .forms import RegistrationForm, LoginForm

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('index_route'))
    return render_template('register.html', form=form) 
