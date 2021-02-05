#webapp/tests/conftest.py

from unittest.mock import Mock

import pytest
from app import create_app, db
from app.models import User, Plant
from flask import current_app

@pytest.fixture(scope="session")
def flask_app():

    # Pass in test configurations
    config_name = "testing"
    app = create_app(config_name)
    test_client = app.test_client()
    # Make an application context before running the tests
    connection = app.app_context()
    connection.push()
    yield test_client # testing happens here

    # After tests are done clean up. 
    connection.pop()

@pytest.fixture(scope="session")
def tested_db(flask_app):

    # Grab whatever current app db context is running
    from app import db

    with current_app.app_context():
        db.session.close()
        db.drop_all()
        db.create_all()
        yield db # all the fun stuff happens here
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="function")
def user():
    # create a test user
    return User(
        name="test_name",
        last_name="test_last_name",
        email="testemail",
        password="testpassword",
    )

@pytest.fixture(scope="function")
def plant():
    return Plant(
        type="testtype",
    )

@pytest.fixture(scope="function")
def make_db_test_user(tested_db):
    def _make_db_test_user(**user_kwargs):
        test_user = User(**user_kwargs)
        db.session.add(test_user)
        return test_user
    return _make_db_test_user

@pytest.fixture(scope="function")
def make_db_test_plant(tested_db):
    def _make_test_plant(**plant_kwargs):
        test_plant = Plant(**plant_kwargs)
        db.session.add(test_plant)
        return test_plant
    return _make_test_plant