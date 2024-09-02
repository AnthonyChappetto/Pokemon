import random
from datetime import datetime # importing py functions
from sinnohplatinum import Platinum

class Sinnoh:  

    #variable to store which part of the route the user is currently exploring
    user_stored_location = None

    @staticmethod
    def set_route_cardinal_direction_northsouth(current_route):
        """
        Asks user which cardinal direction they are exploring on a route.

        Parameters:
            current_route (str): The route the user is currently exploring.

        Returns:
            None
        """
        while True:
            print(f"Which section of {current_route} are you exploring? ('north', 'south')")
            #converts input to lowercase to match clauses
            cardinality = input().lower()
            #checks for valid input
            if cardinality in ["north", "south"]:
                Sinnoh.user_stored_location = cardinality
                break
            else:
                print("Invalid choice, Please type a cardinal direction. ('north', 'south')")

    @staticmethod
    def set_route_cardinal_direction_eastwest(current_route):
        
        """
        Asks user which cardinal direction they are exploring on a route.

        Parameters:
            current_route (str): The route the user is currently exploring.

        Returns:
            None
        """
        while True:
            print(f"Which section of {current_route} are you exploring? ('east', 'west')")
            cardinality = input().lower()
            if cardinality in ["east", "west"]:
                Sinnoh.user_stored_location = cardinality
                break
            else:
                print("Invalid choice, Please type a cardinal direction. ('east', 'west')")

    @staticmethod
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

    @staticmethod
    def encounter_pokemon(route_pokemon):
        """
        Simulates an encounter with a wild pokemon in the Sinnoh region.

        Parameters:
            route_pokemon (dict): A dictionary of pokemon and their encounter rates, with time of day restrictions.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        time_of_day = Sinnoh.grab_user_time()   #grabs user time and stores in time_of_day
        pokemon_found = random.randint(1, 100)  #grabs random percentage and stores in pokemon_found

        for pokemon, (chance, times) in route_pokemon.items(): #goes through list of pokemon based on time of day and chance
            if time_of_day in times and pokemon_found <= chance: #checks if user time of day is equal to pokemon allowed to be out during that time based on the roll of the dice
                return pokemon
            pokemon_found -= chance
        return "No Pokemon found"

    @staticmethod
    def sinnohMain():
        from shinypokemon import select_region_version
        """
        Prompts user to choose a route from Sinnoh and returns the function associated with that route.

        Returns:
        function: The function associated with the route the user selected.
        """

        route_methods = {
            201: Platinum.route201,
            202: Platinum.route202,
            203: Platinum.route203,
            204: Platinum.route204,
            205: Platinum.route205,
            206: Platinum.route206,
            207: Platinum.route207,
            208: Platinum.route208,
            209: Platinum.route209,
            210: Platinum.route210,
            211: Platinum.route211,
            212: Platinum.route212,
            213: Platinum.route213,
            214: Platinum.route214,
            215: Platinum.route215,
            216: Platinum.route216,
            217: Platinum.route217,
            218: Platinum.route218,
            219: Platinum.route219,
            220: Platinum.route220,
            221: Platinum.route221,
            222: Platinum.route222,
            223: Platinum.route223,
            224: Platinum.route224,
            225: Platinum.route225,
            226: Platinum.route226,
            227: Platinum.route227,
            228: Platinum.route228,
            229: Platinum.route229,
            230: Platinum.route230
        }

        #Prompts user to choose a route
        while True:
            try:
                print("Choose a route: \n201 202 203\n204 205 206\n207 208 209\n210 211 212\n213 214 215\n216 217 218\n219 220 221\n222 223 224\n225 226 227\n228 229 230")
                route_choice = int(input("Enter route number: "))

                #grabs route from route_methods
                route = route_methods.get(route_choice)
                if route:
                    Sinnoh.user_stored_location = None
                    return route
                else:
                    print("Invalid route number. Please choose a valid route.")
            except ValueError:
                #Error checking
                print("Invalid input. Numbers only.")