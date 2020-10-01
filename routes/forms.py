from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField,FileField,FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo , URL



class RegistrationForm(FlaskForm):
        email= StringField('Email', validators=[DataRequired(), Email()])
        password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])
        confirm_password= PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
        submit=SubmitField('Sign up')