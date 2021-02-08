# webapp/flask/app/auth/forms.py

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, ValidationError, SubmitField

from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User

class RegistrationForm(FlaskForm):
    """
    Form for registering
    """
    name = StringField("Name", validators=[DataRequired()])
    last_name = StringField("Last Name")
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    password = PasswordField("Password", validators=[DataRequired(), 
                             EqualTo("confirm_password")])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Submit")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already in use")


class LoginForm(FlaskForm):
    """
    Form for logging in a user
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
    

