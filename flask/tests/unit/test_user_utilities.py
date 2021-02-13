# flask/tests/unit/test_user_utilities.py
from unittest.mock import Mock
from pytest import mark
from app.models import User, Plant, Log
from app.user.utilities import (
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

    @mark.parametrize(
        "consumed, new_amount, expected_result",
        [
            (0, 200, 200),
            (100, 150, 250),
            (300, -200, 100),
            (0, -150, 0),
            (100, 0, 100),
        ]
    )
    def test_adjust_day_log_drink_total_given_existing_log(self, consumed, new_amount, expected_result, mocker):
        """
        GIVEN a user id, integer amount, existing log, and day
        WHEN the amount is adjusted for the given day
        THEN ensure that a log exists with correct sum upon return
        """

        # set up dependencies

        user = User(id=0, daily_goal_amount=4000)
        mock_today = mocker.patch("app.user.utilities.date.today")
        mock_db = mocker.patch("app.user.utilities.db")
        mock_log = mocker.patch("app.user.utilities.Log")
        mock_log.water_consumed = consumed

        mock_check_log_exist = mocker.patch(
            "app.user.utilities.check_user_day_entry_exists",
            return_value=mock_log)

        # call the functoin with the amount
        adjust_day_log_drink_total(user.id, new_amount, mock_today)

        # assert that check_user_today_entry_exists called
        mock_check_log_exist.assert_called_with(user.id, mock_today)

        # assert that create is called if not exist
        mock_db.session.add.assert_called_with(mock_log)
        mock_db.session.commit.assert_called_once()
        assert mock_log.water_consumed == expected_result

    @mark.parametrize(
        "water_consumed, new_amount, expected_result",
        [
            (0, 200, 200),
            (100, 150, 250),
            (300, -200, 100),
            (0, -150, 0),
            (100, 0, 100),
        ]
    )
    def test_adjust_day_log_drink_total_given_nonexisting_log(self, water_consumed, new_amount, expected_result, mocker):
        """
        GIVEN a user id, integer amount, non existing log, and day
        WHEN the amount is adjusted for the given day
        THEN ensure that a log is created and returns correct sum
        """
        # set up dependencies
        user = User(id=0, daily_goal_amount=4000)
        today = mocker.patch("app.user.utilities.date.today")
        mock_check_log_exist = mocker.patch(
            "app.user.utilities.check_user_day_entry_exists",
            return_value=None)

        # call the stuff
        adjust_day_log_drink_total(user.id, 200, today)
        raise NotImplementedError
        # assert

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
