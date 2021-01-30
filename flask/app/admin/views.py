
#flask/app/admin/views.py
from flask import render_template, url_for
from ..models import User

@admin.route("/users", methods=["GET", "POST"])
def list_users():
    """
    List all users
    """
    users = User.query.all()

    return render_template("admin/users.html", users=users, title-"Users")

"""
- view all users
- view a user


"""
