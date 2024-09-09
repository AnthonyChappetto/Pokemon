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