#webapp/flask/tests/unit/test_plants.py

from pytest import mark
from unittest.mock import Mock
from app.models import Plant
from app.admin.views import (
    view_plants,
    add_plant,
    edit_plant,
    delete_plant,
)

@mark.plant
class PlantTests:
    
    def test_view_plants(self, flask_app, tested_db):
        raise NotImplementedError

    def test_view_plant(self, flask_app, tested_db):
        raise NotImplementedError

    def test_add_plant(self, flask_app, tested_db):
        raise NotImplementedError

    def test_edit_plant(self, flask_app, tested_db):
        raise NotImplementedError

    def test_delete_plant(self, flask_app, tested_db):
        raise NotImplementedError
