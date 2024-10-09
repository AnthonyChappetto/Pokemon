import random
from shared import get_version
from kalosroutes import XY

class Kalos:  

    @staticmethod
    def encounter_pokemon(route_pokemon):
        """
        Simulates an encounter with a wild pokemon in the Kalos region.

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
    def kalosMain():

        """
        Prompts user to choose a route from Kalos and returns the function associated with that route.

        Returns:
            function: The function associated with the route the user selected.
        """
        version = get_version()

        route_methods = {
            1: XY.route1, 2: XY.route2, 3: XY.route3, 4: XY.route4, 5: XY.route5, 6: XY.route6, 7: XY.route7,
            8: XY.route8, 9: XY.route9, 10: XY.route10, 11: XY.route11, 12: XY.route12, 13: XY.route13, 14: XY.route14,
            15: XY.route15, 16: XY.route16, 17: XY.route17, 18: XY.route18, 19: XY.route19, 20: XY.route20, 
            21: XY.route21, 22: XY.route22

        }

        #Prompts user to choose a route
        while True:
            try:
                if version in ["x", "y"]:
                    print("Choose a route: \n1 2 3\n4 5 6\n7 8 9\n11 12 13\n14 15 16\n17 18 19\n20 21 22")

                route_choice = int(input("Enter route number: "))
                if route_choice == 1:
                    print("\n\nThis route has no pokemon!\n")
                    Kalos.kalosMain()
                route = route_methods.get(route_choice)

                if route:
                    return route
                else:
                    print("Invalid route number. Please choose a valid route.")
            except ValueError:
                #Error checking
                print("Invalid input. Numbers only.")