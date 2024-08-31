import random
from datetime import datetime # importing py functions

#Represents Sinnoh region and all its routes
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
    def route201():
        """
        Simulates an encounter with a wild pokemon on Route 201 in the Sinnoh region.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        current_route = "Route 201"
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
        current_route = "Route 202"
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
        current_route = "Route 203"
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
        current_route = "Route 204"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
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
        current_route = "Route 205"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
            route_pokemon = {
                "Shellos": (45, ["morning", "day", "night"]), 
                "Buizel": (35, ["morning", "day", "night"]),
                "Bidoof": (10, ["morning", "day", "night"]),
                "Pachirisu": (10, ["morning", "day", "night"]),
            }
        else: #north
            if time_of_day in ["morning", "night"]:
                route_pokemon = {
                    "Bidoof": (30, ["morning", "night"]),
                    "Budew": (28, ["morning", "night"]),
                    "Wurmple": (10, ["morning", "night"]),
                    "Silcoon": (10, ["morning", "night"]),
                    "Cascoon": (10, ["morning", "night"]),
                    "Kricketot": (10, ["morning", "night"]),
                    "Beautifly": (1, ["morning", "night"]),
                    "Dustox": (1, ["morning", "night"])
                }
            else: #daytime
                route_pokemon = {
                    "Budew": (38, ["day"]),
                    "Bidoof": (30, ["day"]),
                    "Wurmple": (10, ["day"]),
                    "Silcoon": (10, ["day"]),
                    "Cascoon": (10, ["day"]),
                    "Beautifly": (1, ["day"]),
                    "Dustox": (1, ["day"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route206():
        current_route = "Route 206"
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
        current_route = "Route 207"
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
        current_route = "Route 208"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Budew": (30, ["morning", "day"]),
                "Bidoof": (20, ["morning", "day"]),
                "Bibarel": (20, ["morning", "day"]),
                "Ralts": (15, ["morning", "day"]),
                "Roselia": (15, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Bidoof": (20, ["night"]),
                "Bibarel": (20, ["night"]),
                "Budew": (20, ["night"]),
                "Ralts": (15, ["night"]),
                "Roselia": (15, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route209():
        current_route = "Route 209"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Bibarel": (30, ["morning", "day"]),
                "Roselia": (25, ["morning", "day"]),
                "Ralts": (20, ["morning", "day"]),
                "Staravia": (20, ["morning", "day"]),
                "Chansey": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Bibarel": (30, ["night"]),
                "Roselia": (25, ["night"]),
                "Zubat": (10, ["night"]),
                "Ralts": (10, ["night"]),
                "Duskull": (10, ["night"]),
                "Staravia": (10, ["night"]),
                "Chansey": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route210():
        current_route = "Route 210"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
            if time_of_day == "morning":
                route_pokemon = {
                    "Ponyta": (25, ["morning"]),
                    "Geodude": (20, ["morning"]),
                    "Staravia": (20, ["morning"]),
                    "Scyther": (15, ["morning"]),
                    "Roselia": (15, ["morning"]),
                    "Chansey": (5, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Ponyta": (35, ["day"]),
                    "Geodude": (20, ["day"]),
                    "Roselia": (15, ["day"]),
                    "Staravia": (10, ["day"]),
                    "Chansey": (5, ["day"]),
                    "Scyther": (5, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Geodude": (20, ["night"]),
                    "Staravia": (20, ["night"]),
                    "Ponyta": (15, ["night"]),
                    "Roselia": (15, ["night"]),
                    "Scyther": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Chansey": (5, ["night"])
                }
        #North section of the routes encounters
        else:
            if time_of_day == "morning":
                route_pokemon = {
                    "Meditite": (20, ["morning"]),
                    "Swablu": (20, ["morning"]),
                    "Bibarel": (20, ["morning"]),
                    "Machop": (15, ["morning"]),
                    "Scyther": (15, ["morning"]),
                    "Machoke": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Swablu": (30, ["day"]),
                    "Meditite": (20, ["day"]),
                    "Bibarel": (20, ["day"]),
                    "Machop": (15, ["day"]),
                    "Machoke": (10, ["day"]),
                    "Scyther": (5, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Swablu": (20, ["night"]),
                    "Bibarel": (20, ["night"]),
                    "Machop": (15, ["night"]),
                    "Machoke": (10, ["night"]),
                    "Meditite": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Scyther": (5, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route211():
        current_route = "Route 211"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_eastwest(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "east":
            if time_of_day in ["morning", "day"]: 
                route_pokemon = {
                    "Meditite": (40, ["morning", "day"]),
                    "Graveler": (20, ["morning", "day"]),
                    "Machoke": (15, ["morning", "day"]),
                    "Chingling": (15, ["morning", "day"]),
                    "Bronzor": (10, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Graveler": (20, ["night"]),
                    "Meditite": (20, ["night"]),
                    "Machoke": (15, ["night"]),
                    "Chingling": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Bronzor": (5, ["night"])
                }
        else: #west section of the routes encounters
            if time_of_day in ["morning", "day"]:
                route_pokemon = {   
                    "Meditite": (40, ["morning", "day"]),
                    "Bidoof": (20, ["morning", "day"]),
                    "Machop": (15, ["morning", "day"]),
                    "Chingling": (15, ["morning", "day"]),
                    "Bronzor": (10, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Meditite": (20, ["night"]),
                    "Bidoof": (20, ["night"]),
                    "Machop": (15, ["night"]),
                    "Chingling": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Bronzor": (10, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route212():
        current_route = "Route 212"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "north":
            if time_of_day in ["morning", "day"]: 
                route_pokemon = {
                    "Roselia": (35, ["morning", "day"]),
                    "Marill": (25, ["morning", "day"]),
                    "Kirlia": (20, ["morning", "day"]),
                    "Staravia": (20, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Marill": (45, ["night"]),
                    "Roselia": (35, ["night"]),
                    "Kirlia": (10, ["night"]),
                    "Staravia": (10, ["night"])
                }
        else: #south section of the routes encounters
                route_pokemon = {
                    "Shellos": (45, ["morning", "day", "night"]),
                    "Quagsire": (30, ["morning", "day", "night"]),
                    "Buizel": (15, ["morning", "day", "night"]),
                    "Croagunk": (10, ["morning", "day", "night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route213():
        current_route = "Route 213"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Shellos": (35, ["morning", "day"]),
                "Buizel": (25, ["morning", "day"]),
                "Wingull": (20, ["morning", "day"]),
                "Chatot": (20, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Shellos": (45, ["night"]),
                "Buizel": (35, ["night"]),
                "Wingull": (20, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route214():
        current_route = "Route 214"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Graveler": (35, ["morning"]),
                "Rhyhorn": (30, ["morning"]),
                "Geodude": (20, ["morning"]),
                "Houndoor": (15, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
               "Graveler": (35, ["day"]),
               "Houndoor": (25, ["day"]),
               "Geodude": (20, ["day"]),
               "Rhyhorn": (20, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Rhyhorn": (30, ["night"]),
                "Graveler": (25, ["night"]),
                "Geodude": (20, ["night"]),
                "Houndoor": (15, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route215():
        current_route = "Route 215"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {   
                "Staravia": (30, ["morning"]),
                "Marill": (25, ["morning"]),
                "Scyther": (15, ["morning"]),
                "Abra": (10, ["morning"]),
                "Kadabra": (10, ["morning"]),
                "Lickitung": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Staravia": (40, ["day"]),
                "Marill": (25, ["day"]),
                "Abra": (10, ["day"]),
                "Kadabra": (10, ["day"]),
                "Lickitung": (10, ["day"]),
                "Scyther": (5, ["day"])    
            }
        else: #time of day = night
            route_pokemon = {
                "Marill": (45, ["night"]),
                "Staravia": (20, ["night"]),
                "Abra": (10, ["night"]),
                "Kadabra": (10, ["night"]),
                "Lickitung": (10, ["night"]),
                "Scyther": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
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
                Sinnoh.user_stored_location = None
                return route
            else:
                print("Invalid route number. Please choose a valid route.")
        except ValueError:
            #Error checking
            print("Invalid input. Numbers only.")

#Probably going to need a file for just routes because this file is getting too big