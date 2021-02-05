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
