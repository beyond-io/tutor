from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, URL


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=3, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')


class AddCourse(FlaskForm):
    name = StringField('Course Name', validators=[
                        DataRequired(), Length(max=50)])
    submit = SubmitField('Add Course')


class resourceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    link = TextAreaField('Link',
                validators=[DataRequired(), URL(require_tld=True, message="Not a valid URL")])
    submit = SubmitField('Post')
