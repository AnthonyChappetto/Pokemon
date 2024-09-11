from datetime import datetime 

version = None

def set_version(new_version):
    """
    Sets the global version variable to the given string.

    Parameters:
        new_version (str): The new version string to set.

    Returns:
        None
    """
    global version
    version = new_version

def get_version():
    """
    Grabs the current version of the game the user is playing in the Pokemon world.

    Returns:
        str: The current version of the game the user is playing.
    """
    return version

def grab_users_month():
    current_month = datetime.now().month

    if current_month in [1, 5, 9]:
        season = "spring"
    elif current_month in [2, 6, 10]:
        season = "summer"
    elif current_month in [3, 7, 11]:
        season = "fall"
    else:
        season = "winter"

    return season

def grab_user_time():
    """
    Grabs the user's current time and returns a string representing the current time of day.

    Returns:
        str: The current time of day, either "morning", "day", or "night".
    """
    now = datetime.now()    #grabs user datetime from built in py function
    current_hour = now.hour #grabs exact hour and places in current hour

    if 20 <= current_hour or current_hour < 4: #8:00pm to 3:59am
        return "night"
    elif 4 <= current_hour < 10: #4am to 9:59am
        return "morning"
    else:   #10AM to 7:59pm
        return "day"