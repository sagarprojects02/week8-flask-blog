from flask import render_template, redirect, url_for, flash
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app import db

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login successful")
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
