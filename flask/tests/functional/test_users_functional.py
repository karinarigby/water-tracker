#webapp/flask/tests/unit/test_users.py

from pytest import mark
from unittest.mock import Mock
from app.models import User
from app.admin.views import (
    view_users,
    view_user,
    add_user,
    edit_user,
    delete_user,
)

@mark.user
class UserTests:
    
    def test_view_users(self, flask_app, tested_db):
        raise NotImplementedError

    def test_view_user(self, flask_app, tested_db):
        raise NotImplementedError

    def test_add_user(self, flask_app, tested_db):
        raise NotImplementedError

    def test_edit_user(self, flask_app, tested_db):
        raise NotImplementedError

    def test_delete_user(self, flask_app, tested_db):
        raise NotImplementedError
