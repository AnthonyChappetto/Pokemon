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