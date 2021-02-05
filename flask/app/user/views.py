from datetime import date
from . import Log, User
"""
User Key Actions:

Add a new water log entry
View today's water consumption goal progress
View week/month's progress and activity 
Set a daily goal *
Edit a daily goal *
View plants 
Add friend
Challenge friend
Plant Key Actions:

- 

Add plant to user's garden upon user's daily goal completed
Grow into different stages of plant as goals progress
Whither from user's garden if not 'watered' frequently enough
Evolve into each stage of 'dying'
"""
def adjust_day_log_drink_total(user_id, amount, day):
    """
    Add or subtract water amount in millilitres to user on given day
    """
    # check if user day log exists. create if not exist
    # make the change and update in the db
    raise NotImplementedError


def check_user_today_entry_exists(user_id):
    """
    Check if there exists an entry for today for given user
    Return log if exists else none
    """
    log = Log.query.filter_by(user_id=user_id, date=date.today()).first()
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
    return log.id


def get_user_total_drank_today(user_id):
    """
    Calculate today's progress for given user
    """
def get_user_day_progress_percentage(user_id, date):
    """
    Calculate the user's progress for the given day
    user_id: the id of the given
    request args - day: the date of which to check in the logs
    """
    raise NotImplementedError


def calculate_percentage(progress, goal):
    """
    Calculate the progress compared to today's goal
    """
def set_user_water_daily_goal(user_id, amount):
    """
    Change the user's daily water goal for today's date moving forward
    """
    # change the user.daily_goal_amount 
    # check if there's a log for that user
    # if the user's log has a daily goal amount, update it
    raise NotImplementedError


def add_friend(user_id, friend_id):
    """
    Add a new friend to the user's profile
    """
    raise NotImplementedError