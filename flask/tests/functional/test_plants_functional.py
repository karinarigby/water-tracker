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
    
    def test_view_plants(self, flask_app, make_db_test_plant, tested_db):
        """
        GIVEN the test Flask app and DB,
        WHEN the '/plants' route is requested (GET)
        THEN ensure the response is valid
        """
        plant1 = make_db_test_plant(type="test1type")
        plant2 = make_db_test_plant(type="test2type")

        response = flask_app.get("/plants", follow_redirects=True)
        assert response.status_code == 200
        assert Plant.query.count() == 2
        tested_db.session.delete(plant1)
        tested_db.session.delete(plant2)


    def test_view_plant(self, flask_app, make_db_test_plant, tested_db):
        """
        GIVEN the flask app and db
        WHEN the '/plants/<id>' route is requested (GET)
        THEN ensure the response is valid
        """
        plant = make_db_test_plant(type="test_type")

        response = flask_app.get("/plants/{}".format(plant.id), follow_redirects=True)
        assert response.status_code == 200
        
        # when entered wrong plant id
        response = flask_app.get("/plants/3333888333")
        assert response.status_code == 404 

        tested_db.session.delete(plant)


    def test_add_plant(self, flask_app, tested_db):
        """
        GIVEN the flask app and db,
        WHEN The "plants/add" route is called
        THEN ensure the responses are valid
        """
        # how to test that the form get passed? Mock!

        response = flask_app.get("/plants/add", follow_redirects=True)
        assert response.status_code == 200


    def test_edit_plant(self, flask_app, make_db_test_plant, tested_db):
        """
        GIVEN the flask app and db,
        WHEN the "plants/<id>/edit" route is called
        THEN ensure the response is valid
        """
        plant = make_db_test_plant(type="test-type")
        plant_id = plant.id
        response = flask_app.get("plants/{}/edit".format(plant_id), follow_redirects=True)
        
        assert response.status_code == 200
        tested_db.session.delete(plant)
        
        # response = flask_app.get("plants/{}/edit".format(plant_id), follow_redirects=True)
        # assert response.status_code == 404

    def test_delete_plant(self, flask_app, make_db_test_plant, tested_db):
        """
        GIVEN the flask app and db,
        WHEN the "plants/<id>/delete" route is called
        THEN ensure the response is valid
        """
        plant = make_db_test_plant(type="test-type")
        plant_id = plant.id
        response = flask_app.get("plants/{}/delete".format(plant_id), follow_redirects=True)
        
        assert response.status_code == 200
        assert Plant.query.count() == 0

        response = flask_app.get("plants/{}/delete".format(plant_id), follow_redirects=True)
        assert response.status_code == 404

        