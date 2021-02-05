#flask/app/models.py

from flask_login import UserMixin
from flask_marshmallow import fields
from werkzeug.security import check_password_hash, generate_password_hash
from enum import Enum, IntEnum
from app import db, ma


class Access(IntEnum):
    USER = 1
    ADMIN = 2


user_plant_assoc_table = db.Table(
    "user_plant_assoc",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id", ondelete="CASCADE")),
    db.Column("plant_id", db.Integer, db.ForeignKey("plants.id", ondelete="CASCADE")),
)


class Plant(db.Model):
    """
    Create a table of plants
    """

    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))

    def __repr__(self):
        return "<Plant: {}>".format(self.type)

# class User(UserMixin, db.Model):
class User(db.Model):
    """
    Create a table of users
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28))
    last_name = db.Column(db.String(50))

    email = db.Column(db.String(60), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    # this will inform what to set the goal 
    daily_goal_amount = db.Column(db.Integer)
    access = db.Column(db.Enum(Access), default=Access.USER)
    # db relationships
    plants = db.relationship("Plant", secondary=user_plant_assoc_table)
    logs = db.relationship("Log", backref="user")

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.access == Access.ADMIN

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return "<User: {}".format(self.name)


class Log(db.Model):
    """
    Create a table of logs
    """

    __tablename__ = "logs"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    water_goal = db.Column(db.Integer)
    water_consumed = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    #relationships
    user = db.relationship("User", backref="logs")

    def __repr__(self):
        return "<Log: {} {} {} >".format(self.user.name, self.water_consumed, self.date)
