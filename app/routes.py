import os
import secrets
from random import choice
from string import ascii_letters, digits
from datetime import date
from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, ChildForm, TeacherForm, ParentForm, EmployeeForm
from app.models import User, Employee, Teacher, Parent, Child
from flask_login import login_user, current_user, logout_user, login_required


def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = ascii_letters
    return ''.join(choice(letters) for i in range(stringLength))



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(FirstName=form.firstname.data,LastName= form.lastname.data, Email=form.email.data, Password=hashed_password, Street=form.street.data, City=form.city.data, )
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.Password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

"""
def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) # use the _ to remove the variable or not use it 
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    form_picture.save(picture_path)
    
    return picture_fn
"""

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.FirstName = form.firstname.data
        current_user.LastName = form.lastname.data
        current_user.Email = form.email.data
        current_user.Street = form.street.data
        current_user.City = form.city.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.firstname.data = current_user.FirstName
        form.lastname.data = current_user.LastName
        form.email.data = current_user.Email
        form.street.data = current_user.Street
        form.city.data = current_user.City
    return render_template('account.html',title='account', form=form)


@app.route('/child/create', methods=['GET','POST'])
@login_required
def child_create():
    form = ChildForm()
    if form.validate_on_submit():
        child = Child(FirstName=form.firstname.data, LastName=form.lastname.data, Password= randomString(8), Age= form.age.data, Grade = form.grade.data, Degree= form.degree.data.upper(), Disability_Type = form.disability_type.data, ClassRoom= form.class_room.data.upper())
        db.session.add(child)
        db.session.commit()
        return redirect(url_for('child_list'))
    return render_template('child_create.html', form=form)


@app.route('/child/list')
@login_required
def child_list():
   # if current_user.role == 'Admin':
    children = Child.query.all()
    return render_template('child_list.html', children=children)
    """
    else:
        flash('You need to be admin to view this page.','danger')
        return redirect(url_for('home'))
        """

@app.route('/child/<int:child_id>/show')
@login_required
def child_show(child_id):
    child = Child.query.get_or_404(child_id)
  #  if current_user.role == 'Admin' or current_user == guest.user:
    return render_template('child_details.html', title='Details', child=child)
    """
    else:
        flash('You need to be admin to view this page.','danger')
        return redirect(url_for('home'))
"""

@app.route('/child/<int:child_id>/delete')
@login_required
def child_delete(child_id):
    child = Child.query.get_or_404(child_id)
   # if current_user.role == 'Admin' or current_user == guest.user:
    return render_template('child_delete.html', child=child)
    """
    else:
        flash('You need to be admin to view this page.','danger')
        return redirect(url_for('home'))
"""

@app.route('/child/<int:child_id>/confirm_delete', methods=['POST'])
def child_confirm_delete(child_id):
    child = Child.query.get_or_404(child_id)
  #  if current_user.role == 'Admin' or current_user == guest.user:
    db.session.delete(child)
    db.session.commit()
    flash('Child has been deleted!', 'success')
     #   if current_user.role == "Admin":
      #      return redirect(url_for('reservation_list'))
       # else:
    return redirect(url_for('child_list'))
    """
    else:
        flash('You need to be admin to view this page.','danger')
        return redirect(url_for('home'))
    """

@app.route('/child/<int:child_id>/update', methods=['GET', 'POST'])
@login_required
def child_update(child_id):
    guest = Child.query.get_or_404(child_id)
   # if current_user.role == 'Admin' or current_user == guest.user:
    form = ChildForm()
    child = Child.query.get_or_404(child_id)
    if form.validate_on_submit():
        child.FirstName = form.firstname.data
        child.LastName = form.lastname.data
        child.Age = form.age.data
        child.Grade = form.grade.data
        child.Degree = form.degree.data.upper()
        child.Disability_Type = form.disability_type.data
        child.ClassRoom = form.class_room.data.upper()
        db.session.commit()
        flash('Child has been Updated!','success')
          #  if current_user.role == 'Admin':
          #      return redirect(url_for('reservation_list'))
          #  else:
        return redirect(url_for('child_list'))
    elif request.method == 'GET':
        form.firstname.data = child.FirstName
        form.lastname.data = child.LastName
        form.age.data = child.Age
        form.grade.data = child.Grade
        form.degree.data = child.Degree
        form.disability_type.data = child.Disability_Type
        form.class_room.data = child.ClassRoom
    return render_template('child_update.html', title="Reservation Update", form=form)
    """
    else:
        flash('You need to be admin to view this page.','danger')
        return redirect(url_for('home'))
    """