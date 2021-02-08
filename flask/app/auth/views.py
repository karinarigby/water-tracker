from flask import render_template, url_for
from flask_login import logout_user, login_user
from ..models import User, Access
from . import auth, RegistrationForm, LoginForm

from . import auth

@auth.route('/register', methods=("GET", "POST"))
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

    render_template("auth/register.html", form=form, title="Sign Up")


@auth.route('/login', methods=("GET", "POST"))
def login():
    """
    Allow a user to login using credentials
    """
    return render_template()

