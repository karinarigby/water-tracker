
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
def view_plants():
    """
    List all types of plants
    """
    plants = Plant.query.all()
    return render_template("plant/plants.html", plants=plants, title="Plants")

@admin.route("/plants/add", methods=["GET", "POST"])
def add_plant():
    """
    Add a plant to the database
    """
    return render_template("plant/plant.html", title="Add a New Plant")

@admin.route("/plants/edit/<int:id>", methods=["GET", "POST"])
def edit_plant(id):
    """
    Edit a plant with the id
    """
    plant = Plant.query.get_or_404(id)
    return render_template("plant/plant.html", title="Edit Plant {}".format(plant.type.data))

@admin.route("/plants/delete/<int:id>", methods=["GET", "POST"])
def delete_plant(id):
    """
    Delete a plant with the id
    """
    plant = Plant.query.get_or_404(id)
    plant_type = plant.type
    db.session.delete(plant)
    db.session.commit()
    flash('You have successfully deleted plant type {}'.format(plant_type))

    return redirect(url_for("admin.view_plants"))