from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired, ValidationError
from ..models.users import Users


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

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first
        if user:
            raise ValidationError('Email already registered. Login or choose a different email.')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first
        if user:
            raise ValidationError('Username already registered. Please choose a different one.')



class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired()])
    password = PasswordField('Password',
                validators=[DataRequired()])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')