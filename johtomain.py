import random
from shared import get_version
from shared import grab_user_time
from johtoroutes import GoldSilver

class Johto:

    @staticmethod
    def encounter_pokemon(route_pokemon):
        """
        Simulates an encounter with a wild pokemon in the Johto region.

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
    
    @staticmethod
    def johtoMain():
        """
        Prompts user to choose a route from Johto and returns the function associated with that route.

        Returns:
        function: The function associated with the route the user selected.
        """
        
        route_methods = {
            29: GoldSilver.route29, 30: GoldSilver.route30, 31: GoldSilver.route31, 32: GoldSilver.route32, 33: GoldSilver.route33, 34: GoldSilver.route34,
            35: GoldSilver.route35, 36: GoldSilver.route36, 37: GoldSilver.route37, 38: GoldSilver.route38, 39: GoldSilver.route39, 40: GoldSilver.route40,
            41: GoldSilver.route41, 42: GoldSilver.route42, 43: GoldSilver.route43, 44: GoldSilver.route44, 45: GoldSilver.route45, 46: GoldSilver.route46,
            47: GoldSilver.route47, 48: GoldSilver.route48
        }

        #Prompts user to choose a route
        while True:
            try:
                if get_version() in ["gold", "silver", "crystal"]:
                    print("Choose a route: \n29 30 31\n32 33 34\n35 36 37\n38 39 40\n41 42 43\n44 45 46")
                elif get_version() in ["heartgold", "soulsilver"]:
                    print("Choose a route: \n29 30 31\n32 33 34\n35 36 37\n38 39 40\n41 42 43\n44 45 46\n47 48")

                route_choice = int(input("Enter route number: "))
                route = route_methods.get(route_choice)

                if route:
                    return route
                else:
                    print("Invalid route number. Please choose a valid route.")
            except ValueError:
                #Error checking
                print("Invalid input. Numbers only.")