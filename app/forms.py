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

    child_week_report = TextAreaField('Child Weekly Report')
    
    submit = SubmitField('Submit')



class TeacherForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    phone_number = StringField('Phone Number')
    
    class_room = StringField("Class Room", validators=[DataRequired()])

    submit = SubmitField('Submit')

years = [(0, 'Please Select Year...'), ("First", "First"), ("Second", "Second"), ("Third", "Third"), ("Fourth", "Fourth"), ("Fifth", "Fifth")]

marks = [(0, 'Please Select Mark...'), ("A+", "A+"), ("A", "A"), ("B+", "B+"), ("B", "B"), ("C+", "C+"), ("C", "C"), ("D+", "D+"), ("D", "D")]

disability_types = [(0, 'Please Select Disability Type...'), ("Autism", "Autism"), ("Blindness", "Blindness"), ("Deafness", "Deafness"), ("Emotional Disturbance", "Emotional Disturbance"), ("Hearing Impairment", "Hearing Impairment"), ("Intellectual Disability", "Intellectual Disability"), ("Multiple Disabilities", "Multiple Disabilities"), ("Orthopedic Impairment", "Orthopedic Impairment"), ("Other Health Impaired", "Other Health Impaired"), ("Specific Learning Disability", "Specific Learning Disability"), ("Speech or Language Impairment", "Speech or Language Impairment"), ("Traumatic Brain Injury", "Traumatic Brain Injury"), ("Visual Impairment", "Visual Impairment") ]

classrooms = [(0, 'Please Select Classroom...'), ("A", "A"), ("B", "B"), ("C", "C"), ("D","D"), ("E", "E")]

class ChildForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    age = IntegerField('Age', validators=[DataRequired()])

    year = SelectField('Year', validators=[DataRequired()], choices=years)

    mark = SelectField('Exam Mark', validators=[DataRequired()], choices=marks)

    disability_type = SelectField('Disability Type', validators=[DataRequired()], choices=disability_types)
    
    class_room = SelectField("Class Room", validators=[DataRequired()], choices=classrooms)

    submit = SubmitField('Submit')



class EmployeeForm(FlaskForm):

    firstname = StringField('Firstname', validators=[DataRequired()])

    lastname = StringField('LastName', validators=[DataRequired()])
    
    age = IntegerField('Age', validators=[DataRequired()])

    address = StringField('Address', validators=[DataRequired()])

    salary = StringField('Salary', validators=[DataRequired()])
    
    job = StringField('Job', validators=[DataRequired()])

    submit = SubmitField('Submit')