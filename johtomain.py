import random
from shared import get_version, grab_user_time
from datetime import datetime


class Johto:

    @staticmethod
    def encounter_pokemon(route_pokemon):
        """
        Simulates an encounter with a wild pokemon in the Sinnoh region.

        Parameters:
            route_pokemon (dict): A dictionary of pokemon and their encounter rates, with time of day restrictions.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        time_of_day = grab_user_time()   #grabs user time and stores in time_of_day
        pokemon_found = random.randint(1, 100)  #grabs random percentage and stores in pokemon_found

        for pokemon, (chance, times) in route_pokemon.items(): #goes through list of pokemon based on time of day and chance
            if time_of_day in times and pokemon_found <= chance: #checks if user time of day is equal to pokemon allowed to be out during that time based on the roll of the dice
                return pokemon
            pokemon_found -= chance
        return "No Pokemon found"