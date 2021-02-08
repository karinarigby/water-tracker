from flask import render_template, url_for, flash
from flask_login import logout_user, login_user

from .. import db
from ..models import User, Access
from . import auth
from .forms import RegistrationForm, LoginForm

@auth.route('/register', methods=["GET", "POST"])
def register():
    """
    Register a new user into the db
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            access=Access.USER,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Hey, you successfully registered! You may now login. ")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form, title="Sign Up")


@auth.route('/login', methods=["GET", "POST"])
def login():
    """
    Allow a user to login using credentials
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user()
            return redirect(url_for("home.dashboard"))
        else:
            flash("You goofed on the email or password")

    return render_template("auth/login.html", form=form, title="Login")


@auth.route('/logout')
def logout():
    """
    Sign out an authenticated user
    """
    logout_user()
    flash("You have successfully been logged out")
    return redirect(url_for("home.homepage"))

