from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    Street = db.Column(db.String(60))
    City = db.Column(db.String(60))
    parent = db.relationship('Parent', backref='User', uselist=False)

    def __repr__(self):
        return f"User('{self.FirstName}', '{self.LastName}', '{self.Email}')"


class Child(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    Password = db.Column(db.String(20),nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Grade = db.Column(db.Integer, nullable=False)
    Degree = db.Column(db.String(10))
    Disability_Type = db.Column(db.String(50), nullable=False)
    ClassRoom = db.Column(db.String(10), nullable = False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    parent = db.relationship('Parent', backref='Child', uselist=False)


class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    PhoneNumber = db.Column(db.String(30))
    Email = db.Column(db.String(120), unique = True, nullable = False)
    ClassRoom = db.Column(db.String(10), nullable = False)
    children = db.relationship('Child', backref ='teacher', lazy=True)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'))
    Child_Weekly_Report = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(60), nullable = False)
    Salary = db.Column(db.Integer, nullable = False)
    Job = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return f"User('{self.FirstName}', '{self.LastName}', '{self.Age}', '{self.Address}' ,'{self.Salary}', '{self.Job}')"
