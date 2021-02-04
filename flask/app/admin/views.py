
#flask/app/admin/views.py
from flask import render_template, url_for, flash, redirect
from ..models import User, Plant
from .forms import admin, PlantForm, UserForm

# Users

@admin.route("/users", methods=["GET", "POST"])
def view_users():
    """
    List all users
    """
    users = User.query.all()
    return render_template("user/users.html", users=users, title="Users")

@admin.route("/users/<int:id>", methods=["GET", "POST"])
def view_user(id):
    """
    View a user's info
    """
    user = User.query.get_or_404(id)
    raise NotImplementedError

@admin.route("/users/add", methods=["GET", "POST"])
def add_user():
    """
    Add a new user to the database
    """
    form = UserForm()
    if form.validate_on_submit():
        name = str.lower(form.name.data)
        last_name = str.lower(form.last_name.data)
        email = str.lower(form.email.data)
        user = User(
            name=name,
            last_name=last_name,
            email=email,
            # some permissions
        )
        # try
        db.session.add(user)
        db.session.commit(user)
        flash("You have successfully added user {} to the database".format(user.name))
        
        return redirect(url_for("admin._user", id=user.id))
    return render_template("user/user.html", title="Add New User")

@admin.route("/users/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    """
    Edit a user with given id
    """
    user = User.query.get_or_404(id)
    # user form
    form = UserForm(user)


    return render_template("plant/plant.html", plant=plant, title="Edit User {}".format(user.name))

@admin.route("/users/delete/<int:id>", methods=["GET", "POST"])
def delete_user(id):
    """
    Delete a user with given id
    """
    user = User.query.get_or_404(id)
    user_name = user.name

    db.session.delete(user)
    db.session.commit()

    flash("You have successfully deleted user {}".format(user_name))
    redirect(url_for("admin.view_users"))

# Plants

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
    form = PlantForm(plant)
    if form.validate_on_submit():
        plant.type = form.type.data

        db.session.add(plant)
        db.session.commit()
        flash("You have successfully added the new plant to the database.")
        return redirect(url_for("admin.view_plants"))
    form.type = plant.type
    return render_template("plant/plant.html", 
        title="Edit Plant {}".format(plant.type.data),
        form=form,
        add_plant=False,
    )

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