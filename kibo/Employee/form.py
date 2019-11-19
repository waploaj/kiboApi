from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from  wtforms.validators import DataRequired,Length,ValidationError



class LoginForm(FlaskForm):

        username = StringField("Username",validators=[DataRequired(),Length(min=3,max=10)])
        password = PasswordField("password", validators=[DataRequired(),Length(min=6)])
        submit = SubmitField("Login")


