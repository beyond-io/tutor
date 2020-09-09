from flask import Flask, Response, render_template, request, redirect, url_for
from .forms import RegistrationForm, LoginForm

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('get_course_info_route', id=1))
    return render_template('register.html', form=form)
