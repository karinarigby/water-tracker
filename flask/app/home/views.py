# flask/app/home/views.py

from flask import render_template

from . import home


@home.route("/")
def homepage():
    """
    Render the home page on the / route
    """
    return render_template("home/index.html", title="Home")


@home.route("/dashboard")
def dashboard():
    """
    Render the dashboard on the /dashboard route
    """
    # if


    return render_template("home/dashboard.html", title="Dashboard")


@home.route("/howitworks")
def how_it_works(methods=("GET")):
    """
    Render the page that explains how the product works
    """
    return render_template("home/howitworks.html", title="How It Works")