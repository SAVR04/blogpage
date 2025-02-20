from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField ,SubmitField

class Registerform(FlaskForm):
     email=StringField(label="email")
     password = PasswordField(label="pass1")
     password2 = PasswordField(label="pass2")
     submit=SubmitField(label="submit")
