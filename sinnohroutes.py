import random
from datetime import datetime # importing py functions

#Represents Sinnoh region and all its routes
class Sinnoh:
    
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
    def route201():
        """
        Simulates an encounter with a wild pokemon on Route 201 in the Sinnoh region.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "night"]: #morning and night have same odds so they're combined
            route_pokemon = {
                "Starly": (50, ["morning", "night"]), #pokemon starly is the key paired with the values chance (50%) and time (morning and night)
                "Bidoof": (40, ["morning", "night"]),
                "Kricketot": (10, ["morning", "night"])
            }
        elif time_of_day == "day": #if time is day
            route_pokemon = {
                "Starly": (50, ["day"]),
                "Bidoof": (50, ["day"]),
            }
        return Sinnoh.encounter_pokemon(route_pokemon) #returns the pokemon to put into the list

    @staticmethod
    def route202():
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "night"]: 
            route_pokemon = {
                "Starly": (30, ["morning", "night"]), 
                "Bidoof": (30, ["morning", "night"]),
                "Shinx": (30, ["morning", "night"]),
                "Kricketot": (10, ["morning", "night"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Starly": (30, ["day"]),
                "Bidoof": (50, ["day"]),
                "Shinx": (20, ["day"])
            }
        return Sinnoh.encounter_pokemon(route_pokemon) 

    @staticmethod
    def route203():
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning": 
            route_pokemon = {
                "Starly": (35, ["morning"]), 
                "Shinx": (25, ["morning"]),
                "Abra": (15, ["morning"]),
                "Bidoof": (15, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Starly": (35, ["day"]),
                "Bidoof": (25, ["day"]),
                "Shinx": (25, ["day"]),
                "Abra": (15, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Starly": (25, ["night"]),
                "Shinx": (25, ["night"]),
                "Abra": (15, ["night"]),
                "Bidoof": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Kricketot": (10, ["night"])
            }
        return Sinnoh.encounter_pokemon(route_pokemon) 
    
    #doesn't work properly handing north and south rn
    @staticmethod
    def route204():
        time_of_day = Sinnoh.grab_user_time()

        print("South or North section of Route 204?")
        north_south = input().lower()

        if north_south == "south":
            if time_of_day == "morning": 
                route_pokemon = {
                    "Starly": (25, ["morning"]), 
                    "Bidoof": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Budew": (15, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (25, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"]),
                    "Wurmple": (10, ["day"])
                }
            else: #time of day = night
                route_pokemon = {  
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Budew": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Kricketot": (10, ["night"])
                }
        else: #north
            if time_of_day == "morning": 
                route_pokemon = {
                    "Starly": (25, ["morning"]), 
                    "Bidoof": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Budew": (15, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (25, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"]),
                    "Wurmple": (10, ["day"])
                }
            else: #time of day = night
                route_pokemon = {  
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Budew": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Kricketot": (10, ["night"])
                }
        return Sinnoh.encounter_pokemon(route_pokemon)       

    @staticmethod
    def route205():
        time_of_day = Sinnoh.grab_user_time()

        print("South or North section of Route 205?")
        north_south = input().lower()

        if north_south == "south":
            if time_of_day == "morning" or time_of_day == "day" or time_of_day == "night":
                route_pokemon = {
                    "Shellos": (45, ["morning", "day", "night"]), 
                    "Buizel": (35, ["morning", "day", "night"]),
                    "Bidoof": (10, ["morning", "day", "night"]),
                    "Pachirisu": (10, ["morning", "day", "night"]),
                }
        else: #north
            if time_of_day == "morning" or time_of_day == "night":
                route_pokemon = {
                    "Bidoof": (30, ["morning"]),
                    "Budew ": (28, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Silcoon": (10, ["morning"]),
                    "Cascoon": (10, ["morning"]),
                    "Kricketot": (10, ["morning"]),
                    "Beautifly": (1, ["morning"]),
                    "Dustox": (1, ["morning"])
                }
            else: #daytime
                route_pokemon = {
                    "Budew": (38, ["morning"]),
                    "Bidoof ": (30, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Silcoon": (10, ["morning"]),
                    "Cascoon": (10, ["morning"]),
                    "Beautifly": (1, ["morning"]),
                    "Dustox": (1, ["morning"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route206():
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Geodude": (30, ["morning"]),
                "Machop": (20, ["morning"]),
                "Ponyta": (20, ["morning"]),
                "Gligar": (20, ["morning"]),
                "Kricketune": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Geodude": (30, ["day"]),
                "Ponyta": (30, ["day"]),
                "Machop": (20, ["day"]),
                "Gligar": (20, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Geodude": (30, ["night"]),
                "Machop": (20, ["night"]),
                "Ponyta": (20, ["night"]),
                "Zubat": (10, ["night"]),
                "Gligar": (10, ["night"]),
                "Kricketune": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route207():
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Machop": (35, ["morning"]),
                "Geodude": (30, ["morning"]),
                "Ponyta": (25, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Machop": (45, ["day"]),
                "Geodude": (30, ["day"]),
                "Ponyta": (25, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Machop": (35, ["night"]),
                "Geodude": (30, ["night"]),
                "Ponyta": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Kricketot": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route208():
        return
    def route209():
        return
    def route210():
        return
    def route211():
        return
    def route212():
        return
    def route213():
        return
    def route214():
        return
    def route215():
        return
    def route216():
        return
    def route217():
        return
    def route218():
        return
    def route219():
        return
    def route220():
        return
    def route221():
        return
    def route222():
        return
    def route223():
        return
    def route224():
        return
    def route225():
        return
    def route226():
        return
    def route227():
        return
    def route228():
        return
    def route229():
        return
    def route230():
        return

#References for calling all the routes when user inputs the identical route number
@staticmethod
def sinnohMain():
    """
    Prompts user to choose a route from Sinnoh and returns the function associated with that route.

    Returns:
        function: The function associated with the route the user selected.
    """
    route_methods = {
        201: Sinnoh.route201,
        202: Sinnoh.route202,
        203: Sinnoh.route203,
        204: Sinnoh.route204,
        205: Sinnoh.route205,
        206: Sinnoh.route206,
        207: Sinnoh.route207,
        208: Sinnoh.route208,
        209: Sinnoh.route209,
        210: Sinnoh.route210,
        211: Sinnoh.route211,
        212: Sinnoh.route212,
        213: Sinnoh.route213,
        214: Sinnoh.route214,
        215: Sinnoh.route215,
        216: Sinnoh.route216,
        217: Sinnoh.route217,
        218: Sinnoh.route218,
        219: Sinnoh.route219,
        220: Sinnoh.route220,
        221: Sinnoh.route221,
        222: Sinnoh.route222,
        223: Sinnoh.route223,
        224: Sinnoh.route224,
        225: Sinnoh.route225,
        226: Sinnoh.route226,
        227: Sinnoh.route227,
        228: Sinnoh.route228,
        229: Sinnoh.route229,
        230: Sinnoh.route230
    }

    #Prompts user to choose a route
    while True:
        try:
            print("Choose a route: \n201 202 203\n204 205 206\n207 208 209\n210 211 212\n213 214 215\n216 217 218\n219 220 221\n222 223 224\n225 226 227\n228 229 230")
            route_choice = int(input("Enter route number: "))
            #grabs route from route_methods
            route = route_methods.get(route_choice)   

            if route:
                return route
            else:
                print("Invalid route number. Please choose a valid route.")
        except ValueError:
            #Error checking
            print("Invalid input. Numbers only.")