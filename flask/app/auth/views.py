from flask import render_template, url_for
from ..models import User

from . import auth

@auth.route('/register', methods=("GET", "POST"))
def register():
    """
    Register a new user into the db
    """
    return render_template()


@auth.route('/login', methods=("GET", "POST"))
def login():
    """
    Allow a user to login using credentials
    """
    return render_template()

