from datetime import date
from ..models import Log, User
from app import db

"""

Add plant to user's garden upon user's daily goal completed
Grow into different stages of plant as goals progress
Whither from user's garden if not 'watered' frequently enough
Evolve into each stage of 'dying'
"""


def adjust_day_log_drink_total(user_id, amount, date):
    """
    Add or subtract water amount in millilitres to user on given day
    """
    # check if user day log exists. create if not exist
    # make the change and update in the db
    log = check_user_day_entry_exists(user_id, date)
    if log is None:
        log = add_user_day_entry(user_id, date)

    sum = log.water_consumed + amount
    log.water_consumed = sum if sum > 0 else 0

    db.session.add(log)
    db.session.commit()


def check_user_day_entry_exists(user_id, date):
    """
    Check if there exists an entry for today for given user
    Return log if exists else none
    """
    log = Log.query.filter_by(user_id=user_id, date=date).first()
    return log


def add_user_day_entry(user_id, day):
    """
    Add a new user day log entry into the database
    Returns the log
    """
    user = User.query.get_or_404(user_id)
    log = Log(
        user_id=user_id,
        water_goal=user.daily_goal_amount,
        water_consumed=0,
        date=date.today()
    )
    db.session.add(log)
    db.session.commit()
    return log


def get_user_total_drank_today(user_id):
    """
    Calculate today's progress for given user
    """
    # check if log for today and user_id
    log = check_user_day_entry_exists(user_id, date.today)
    return log.water_consumed if log else None


def get_user_day_progress_percentage(user_id, date):
    """
    Calculate the user's progress for the given day
    user_id: the id of the given
    return: percentage of progress
    """
    # get user goal for that day

    # see if log exists for user and date
    log = Log.query.filter_by(user_id=user_id, date=date).first()

    return calculate_percentage(log.water_consumed, log.water_goal) if log else 0


def calculate_percentage(progress, goal):
    """
    Calculate the progress compared to today's goal
    """
    return (progress/goal) * 100


def set_user_water_daily_goal(user_id, amount):
    """
    Change the user's daily water goal for today's date moving forward
    """
    # change the user.daily_goal_amount
    # check if there's a log for that user
    # if the user's log has a daily goal amount, update it
    user = User.query.get_or_404(user_id)
    user.daily_goal_amount = amount
    log = check_user_day_entry_exists(user_id, date.today)
    if log:
        log.water_goal = amount
        db.session.add(log)
        db.commit()


def add_friend(user_id, friend_id):
    """
    Add a new friend to the user's profile
    """
    user = User.query.get_or_404(user_id)

    raise NotImplementedError
