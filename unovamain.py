import random
from shared import get_version
from unovaroutes import Black

class Unova:  

    @staticmethod
    def encounter_pokemon(route_pokemon):

        """
        Simulates an encounter with a wild pokemon in the Unova region.

        Parameters:
            route_pokemon (dict): A dictionary of pokemon and their encounter rates.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        pokemon_found = random.randint(1, 100)  

        for pokemon, chance in route_pokemon.items(): 
            if pokemon_found <= chance: 
                return pokemon
            pokemon_found -= chance
        return "No Pokemon found"

    @staticmethod
    def unovaMain():

        """
        Prompts user to choose a route from Unova and returns the function associated with that route.

        Returns:
            function: The function associated with the route the user selected.
        """
        version = get_version()

        route_methods = {
            1: Black.route1, 2: Black.route2, 3: Black.route3, 4: Black.route4, 5: Black.route5, 6: Black.route6, 7: Black.route7,
            8: Black.route8, 9: Black.route9, 10: Black.route10, 11: Black.route11, 12: Black.route12, 13: Black.route13, 14: Black.route14,
            15: Black.route15, 16: Black.route16, 17: Black.route17, 18: Black.route18, 19: Black.route19, 20: Black.route20, 
            21: Black.route21, 22: Black.route22, 23: Black.route23

        }

        #Prompts user to choose a route
        while True:
            try:
                if version in ["black", "white"]:
                    print("Choose a route: \n1 2 3\n4 5 6\n7 8 9\n10 11 12\n13 14 15\n16 17 18")
                elif version in ["black2", "white2"]:
                    print("Choose a route: \n1 2 3\n4 5 6\n7 8 9\n11 12 13\n14 15 16\n17 18 19\n20 21 22\n23")

                route_choice = int(input("Enter route number: "))
                route = route_methods.get(route_choice)

                if route:
                    return route
                else:
                    print("Invalid route number. Please choose a valid route.")
            except ValueError:
                #Error checking
                print("Invalid input. Numbers only.")