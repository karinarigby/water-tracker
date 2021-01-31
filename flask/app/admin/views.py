
#flask/app/admin/views.py
from flask import render_template, url_for
from ..models import User, Plant
from . import admin

@admin.route("/users", methods=["GET", "POST"])
def list_users():
    """
    List all users
    """
    users = User.query.all()
    return render_template("admin/users.html", users=users, title="Users")


@admin.route("/plants", methods=["GET", "POST"])
def list_plants():
    """
    List all types of plants
    """
    plants = Plant.query.all()
    return render_template("admin/plants.html", plants=plants, title="Plants")