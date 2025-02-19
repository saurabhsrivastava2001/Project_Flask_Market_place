from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username= StringField(label='User Name:')
    emailid = StringField(label='Eamil Address:')
    password1 = PasswordField(label= 'Password')
    password2 = PasswordField(label= 'Confirm Password')
    submit= SubmitField(label='Create Account')

