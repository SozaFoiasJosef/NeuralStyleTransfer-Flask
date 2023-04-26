from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
import re
import os
from werkzeug.utils import secure_filename
from . import main

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class EditPointsForm(FlaskForm):
    points = SelectField('Points', choices=[('10', '10 points'), ('25', '25 points'), ('50', '50 points')],
                         validators=[DataRequired()])
    submit = SubmitField('Submit')


class PhotosForm(FlaskForm):
    contentImg = FileField('Content', validators=[DataRequired()])
    styleImg = FileField('Style', validators=[DataRequired()])
    slider = IntegerField('Slider', validators=[NumberRange(min=50, max=400)])
    submit = SubmitField('Submit')

