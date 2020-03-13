from datetime import datetime
from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User



class RegistrationForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', 
     validators=[DataRequired(), EqualTo('password')])

    street = StringField("Street")

    city = StringField("City")

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(Email = email.data).first()
        if user:
            raise ValidationError('That Email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    street = StringField("Street")

    city = StringField("City")

    submit = SubmitField('Update')


    def validate_email(self, email):
        if email.data != current_user.Email:
            user = User.query.filter_by(Email = email.data).first()
            if user:
                raise ValidationError('That Email is taken. Please choose a different one.')




class ParentForm(FlaskForm):

    child_week_report = TextAreaField('Password')
    
    submit = SubmitField('Submit')



class TeacherForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    phone_number = StringField('Phone Number')
    
    class_room = StringField("Class Room", validators=[DataRequired()])

    submit = SubmitField('Submit')


class ChildForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    age = IntegerField('Age', validators=[DataRequired()])

    grade = IntegerField('Grade', validators=[DataRequired()])

    degree = StringField('Degree', validators=[DataRequired()])

    disability_type = StringField('Disability Type', validators=[DataRequired()])
    
    class_room = StringField("Class Room", validators=[DataRequired()])

    submit = SubmitField('Submit')



class EmployeeForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    age = IntegerField('Age', validators=[DataRequired()])

    address = StringField('Address', validators=[DataRequired()])

    salary = StringField('Salary', validators=[DataRequired()])
    
    job = StringField('Job', validators=[DataRequired()])

    submit = SubmitField('Submit')