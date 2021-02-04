# webapp/flask/app/admin/forms.py

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired, Email

from ..models import User, Plant

class UserForm(FlaskForm):
    """
    Form for admin to add or edit a user
    """
    name = StringField("Name", validators=[DataRequired()])
    last_name = StringField("Last Name")
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


class PlantForm(FlaskForm):
    """
    Form for admin to add or edit a plant
    """
    type = StringField("Type")
    submit = SubmitField("Submit")