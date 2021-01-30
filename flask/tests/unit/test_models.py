#flask/tests/unit/test_models.py

from app.models import User, Plant, Log

class ModelTests:

    def test_new_user(self):
        """
        GIVEN a User model
        WHEN a new User is created 
        THEN ensure that all fields set correctly
        """
        user = User(id=1, name = "first", last_name="last", email="email@email.com")
        
        assert user.id == 1
        assert user.name == "first"
        assert user.last_name == "last"
        assert email == "email@email.com"
    # def test_new_user_password_methods(self, mocker):
    #     """
    #     GIVEN a User model
    #     WHEN a new User is created with password
    #     THEN ensure set user.password calls pas
    #     """
    #     raise NotImplementedError
    def test_new_log(self):
        """
        GIVEN a Log model
        WHEN a new Log is created
        THEN ensure that all fields set correctly
        """
        # missing the date field
        log = Log(id=1, user_id=2, water_goal=5000, water_consumed=1,)

        assert log.id == 1
        assert log.user_id == 2
        assert log.water_goal == 5000
        assert log.water_consumed == 1

    def test_new_plant(self):
        """
        GIVEN a Plant model
        WHEN a new Plant is created
        THEN ensure that all fields set correctly
        """
        plant = Plant(id=1, type="type")

        assert plant.id == 1
        assert plant.type == "type"