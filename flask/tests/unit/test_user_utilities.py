# flask/tests/unit/test_user_utilities.py
from unittest.mock import Mock

from app.models import User, Plant, Log
from user.utilities import (
    adjust_day_log_drink_total,
    check_user_today_entry_exists,
    add_user_day_entry,
    get_user_total_drank_today,
    get_user_day_progress_percentage,
    calculate_percentage,
    set_user_water_daily_goal,
    add_friend,
)

@mark.log
class UtilityUnitTests:


    def test_adjust_day_log_drink_total(self, mocker):
        """
        GIVEN a user id, integer amount, and day
        WHEN the amount is adjusted for the given day
        THEN ensure that a log exists with correct sum upon return
        """
        
        # set up dependencies
        user = User(id=0, daily_goal_amount=4000)
        today = mocker.patch("app.user.utilities.date.today")
        mock_check_log_exist = mocker.patch("app.user.utilities.check_user_day_entry_exists",
            return_value=True)
        
        # call the functoin with the amount
        adjust_day_log_drink_total(user.id, 200, today)
        
        # assert that check_user_today_entry_exists called
        mock_check_log_exist.assert_called_with(user.id, today)
        
        # assert that create is called if not exist

        #     assert that db add and commit is called 
        # assert that new sum correctly applies addition/subtraction (min 0)

        raise NotImplementedError


    def test_check_user_today_entry_exists(self):
        """
        GIVEN a user id
        WHEN checking if a log exists for given user and today's date
        THEN return the log if it exists or None
        """
        raise NotImplementedError

    def test_add_user_day_entry(self):
        """
        GIVEN a user id and a date
        WHEN the log is added to the db
        THEN ensure a log is returned with proper user id and date
        """
        raise NotImplementedError

    def test_get_user_total_drank_today(self):
        """
        GIVEN a user id
        WHEN the user's log is queried to see today's total
        THEN ensure that either water amount is returned or None
        """
        raise NotImplementedError

    def test_get_user_day_progress_percentage(self):
        """
        GIVEN a user id and a date
        WHEN calculating the percentage
        THEN ensure that calculate percentage is called if log not empty
             else return 0
        """
        raise NotImplementedError

    def test_calculate_percentage(self):
        """
        GIVEN int progress and int goal
        WHEN the percentage is calculated
        THEN ensure that the result is returned
        """
        raise NotImplementedError

    def test_set_user_water_daily_goal(self):
        """
        GIVEN a user id and int amount
        WHEN set water daily goal is called
        THEN ensure that the user's goal is set to amount
        """
        raise NotImplementedError

    def test_add_friend(self):
        """
        GIVEN a user id and the friend's id
        WHEN the add friend function is called
        THEN ensure that the friend is added to the user's account
        """
        raise NotImplementedError