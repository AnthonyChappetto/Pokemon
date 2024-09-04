#Represents Sinnoh region and all its routes for diamond
class Diamond:
    @staticmethod
    def route201():
        from sinnohmain import Sinnoh
        """
        Simulates an encounter with a wild pokemon on Route 201 in the Sinnoh region.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        current_route = "Route 201"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Starly": (50, ["morning", "day", "night"]), #pokemon starly is the key paired with the values chance (50%) and time (morning, day, night)
            "Bidoof": (50, ["morning", "day", "night"]),
            }

        return Sinnoh.encounter_pokemon(route_pokemon) #returns the pokemon to put into the list
    
    @staticmethod
    def route202():
        from sinnohmain import Sinnoh

        current_route = "Route 202"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "night"]:
            route_pokemon = {
                "Starly": (30, ["morning","night"]), 
                "Bidoof": (30, ["morning", "night"]),
                "Shinx": (30, ["morning", "night"]),
                "Kricketot": (10, ["morning", "night"])
            }
        else: #time of day = day
            route_pokemon = {
                "Starly": (40, ["day"]),
                "Bidoof": (30, ["day"]),
                "Shinx": (30, ["day"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route203():
        from sinnohmain import Sinnoh

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
                "Starly": (45, ["day"]),
                "Shinx": (25, ["day"]),
                "Abra": (15, ["day"]),
                "Bidoof": (15, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Starly": (35, ["night"]),
                "Shinx": (25, ["night"]),
                "Abra": (15, ["night"]),
                "Bidoof": (15, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route204():
        from sinnohmain import Sinnoh
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
                    "Budew": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (35, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Budew": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Zubat": (10, ["night"])
                }
        #North section of the routes encounters
        elif cardinality == "north":
            if time_of_day == "morning":
                route_pokemon = {
                    "Starly": (25, ["morning"]),
                    "Bidoof": (25, ["morning"]),
                    "Budew": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (35, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Budew": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Zubat": (10, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route205():
        from sinnohmain import Sinnoh
        current_route = "Route 205"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
                route_pokemon = {
                    "Shellos": (45, ["morning", "day", "night"]),
                    "Buizel": (35, ["morning", "day", "night"]),
                    "Bidoof": (10, ["morning", "day", "night"]),
                    "Pachirisu": (10, ["morning", "day", "night"])
                }
        #North section of the routes encounters
        elif cardinality == "north":
            route_pokemon = {
                "Bidoof": (45, ["morning", "night"]),
                "Buziel": (35, ["morning", "night"]),
                "Pachirisu": (10, ["morning", "day", "night"]),
                "Shellos": (10, ["morning", "day", "night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route206():
        from sinnohmain import Sinnoh

        current_route = "Route 206"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Ponyta": (35, ["morning"]),
                "Stunky": (25, ["morning"]),
                "Geodude": (10, ["morning"]),
                "Kricketune": (10, ["morning"]),
                "Bronzor": (10, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Ponyta": (45, ["day"]),
                "Stunky": (25, ["day"]),
                "Geodude": (10, ["day"]),
                "Kricketune": (10, ["day"]),
                "Bronzor": (10, ["day"])
            }
        else: #night
            route_pokemon = {
                "Ponyta": (35, ["night"]),
                "Stunky": (25, ["night"]),
                "Kricketune": (10, ["night"]),
                "Geodude": (10, ["night"]),
                "Bronzor": (10, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route207():
        from sinnohmain import Sinnoh

        current_route = "Route 207"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Geodude": (55, ["morning"]),
                "Machop": (35, ["morning"]),
                "Kricketot": (10, ["morning"]),
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Machop": (55, ["day"]),
                "Geodude": (45, ["day"]),
            }
        else: #night
            route_pokemon = {
                "Geodude": (55, ["night"]),
                "Machop": (35, ["night"]),
                "Zubat": (10, ["night"]),
            }
    @staticmethod
    def route208():
        from sinnohmain import Sinnoh

        current_route = "Route 208"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Psyduck": (30, ["morning", "day"]),
                "Machop": (20, ["morning", "day"]),
                "Meditite": (20, ["morning", "day"]),
                "Bidoof": (20, ["morning", "day"]),
                "Bibarel": (10, ["morning", "day"])
            }
        else: #night
            route_pokemon = {
                "Psyduck": (30, ["night"]),
                "Bidoof": (20, ["night"]),
                "Zubat": (20, ["night"]),
                "Machop": (10, ["night"]),
                "Meditite": (10, ["night"]),
                "Bibarel": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route209():
        from sinnohmain import Sinnoh

        current_route = "Route 209"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Bibarel": (35, ["morning"]),
                "Mime Jr.": (25, ["morning"]),
                "Starly": (20, ["morning"]),
                "Staravia": (15, ["morning"]),
                "Chansey": (5, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Bibarel": (45, ["day"]),
                "Staravia": (25, ["day"]),
                "Starly": (20, ["day"]),
                "Chansey": (5, ["day"]),
                "Mime Jr.": (5, ["day"])
            }
        else: #night
            route_pokemon = {
                "Bibarel": (35, ["night"]),
                "Starly": (20, ["night"]),
                "Staravia": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Gastly": (10, ["night"]),
                "Chansey": (5, ["night"]),
                "Mime Jr.": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route210():
        from sinnohmain import Sinnoh
        current_route = "Route 210"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Geodude": (30, ["morning"]),
                        "Ponyta": (30, ["morning"]),
                        "Mime Jr.": (25, ["morning"]),
                        "Kricketune": (10, ["morning"]),
                        "Chansey": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Ponyta": (50, ["day"]),
                        "Geodude": (30, ["day"]),
                        "Kricketune": (10, ["day"]),
                        "Chansey": (5, ["day"]),
                        "Mime Jr.": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Ponyta": (30, ["night"]),
                        "Kricketune": (30, ["night"]),
                        "Mime Jr.": (25, ["night"]),
                        "Geodude": (10, ["night"]),
                        "Chansey": (5, ["night"])
                    }
        #North section of the routes encounters
        elif cardinality == "north":
            if time_of_day in ["morning", "day"]:
                route_pokemon = {
                    "Meditite": (30, ["morning", "day"]),
                    "Psyduck": (20, ["morning", "day"]),
                    "Machop": (20, ["morning", "day"]),
                    "Bibarel": (20, ["morning", "day"]),
                    "Machoke": (10, ["morning", "day"])
                }
            else: #night
                route_pokemon = {
                    "Psyduck": (20, ["night"]),
                    "Meditite": (20, ["night"]),
                    "Bibarel": (20, ["night"]),
                    "Machop": (10, ["night"]),
                    "Machoke": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route211():
        from sinnohmain import Sinnoh
        current_route = "Route 211"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_eastwest(current_route)

        cardinality = Sinnoh.user_stored_location

        if cardinality == "east":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Meditite": (35, ["morning", "day"]),
                        "Machoke": (20, ["morning", "day"]),
                        "Graveler": (20, ["morning", "day"]),
                        "Ponyta": (15, ["morning", "day"]),
                        "Chingling": (10, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Meditite": (35, ["night"]),
                        "Graveler": (20, ["night"]),
                        "Machoke": (10, ["night"]),
                        "Chingling": (10, ["night"]),
                        "Zubat": (10, ["night"]),
                        "Noctowl": (10, ["night"]),
                        "Ponyta": (5, ["night"])
                    }
        else: #west
            if time_of_day in ["morning", "day"]:
                route_pokemon = {
                    "Meditite": (35, ["morning", "day"]),
                    "Bidoof": (20, ["morning", "day"]),
                    "Geodude": (20, ["morning", "day"]),
                    "Ponyta": (15, ["morning", "day"]),
                    "Chingling": (10, ["morning", "day"])
                }
            else: #night
                route_pokemon = {
                    "Meditite": (35, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Geodude": (10, ["night"]),
                    "Ponyta": (10, ["night"]),
                    "Chingling": (10, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Hoothoot": (10, ["night"])
                }                

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route212():
        from sinnohmain import Sinnoh
        current_route = "Route 212"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Bibarel": (35, ["morning", "day"]),
                        "Wooper": (30, ["morning", "day"]),
                        "Roselia": (25, ["morning", "day"]),
                        "Kricketune": (10, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (35, ["night"]),
                        "Kricketune": (20, ["night"]),
                        "Bibarel": (20, ["night"]),
                        "Roselia": (10, ["night"])
                    }
        else: #north
            if time_of_day == "morning":
                route_pokemon = {
                    "Budew": (30, ["morning"]),
                    "Starly": (20, ["morning"]),
                    "Kricketune": (20, ["morning"]),
                    "Staravia": (15, ["morning"]),
                    "Roselia": (15, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Budew": (30, ["day"]),
                    "Staravia": (25, ["day"]),
                    "Starly": (20, ["day"]),
                    "Roselia": (15, ["day"]),
                    "Kricketune": (10, ["day"])
                }
            else: #night
                route_pokemon = {
                    "Kricketune": (30, ["night"]),
                    "Budew": (30, ["night"]),
                    "Starly": (20, ["night"]),
                    "Roselia": (15, ["night"]),
                    "Staravia": (5, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route213():
        return
    @staticmethod
    def route214():
        return
    @staticmethod
    def route215():
        return
    @staticmethod
    def route216():
        return
    @staticmethod
    def route217():
        return
    @staticmethod
    def route218():
        return
    @staticmethod
    def route219():
        return
    @staticmethod
    def route220():
        return
    @staticmethod
    def route221():
        return
    @staticmethod
    def route222():
        return
    @staticmethod
    def route223():
        return
    @staticmethod
    def route224():
        return
    @staticmethod
    def route225():
        return
    @staticmethod
    def route226():
        return
    @staticmethod
    def route227():
        return
    @staticmethod
    def route228():
        return
    @staticmethod
    def route229():
        return
    @staticmethod
    def route230():
        return